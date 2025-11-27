import logging
from collections import deque
import time
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI()

# --- In-memory Rate Limiting Configuration ---
# This is a simple, in-memory rate limiter for demonstration purposes.
# For production, a more robust solution (e.g., Redis-backed) is recommended.
RATE_LIMIT_CALLS = 5 # Max 5 calls
RATE_LIMIT_PERIOD = 60 # per 60 seconds

# Dictionary to store call timestamps for each client (identified by IP)
client_requests = {}

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    if request.url.path.startswith("/chat/") or request.url.path.startswith("/api/v1/chat/"):
        client_ip = request.client.host
        current_time = time.time()

        if client_ip not in client_requests:
            client_requests[client_ip] = deque()

        # Remove old timestamps outside the rate limit period
        while client_requests[client_ip] and client_requests[client_ip][0] < current_time - RATE_LIMIT_PERIOD:
            client_requests[client_ip].popleft()

        if len(client_requests[client_ip]) >= RATE_LIMIT_CALLS:
            logger.warning(f"Rate limit exceeded for IP: {client_ip} on path: {request.url.path}")
            return JSONResponse(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                content={
                    "success": False,
                    "message": "Rate limit exceeded. Please try again later.",
                    "statusCode": status.HTTP_429_TOO_MANY_REQUESTS,
                },
            )
        client_requests[client_ip].append(current_time)
    response = await call_next(request)
    return response
# --- End In-memory Rate Limiting Configuration ---

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTP Exception: {exc.status_code} - {exc.detail} for URL: {request.url}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail,
            "statusCode": exc.status_code
        },
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.exception(f"Unhandled Exception for URL: {request.url}")
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "An internal server error occurred.",
            "statusCode": 500
        },
    )

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Outgoing Response: {request.method} {request.url} - Status: {response.status_code}")
    return response

@app.get("/")
async def read_root():
    return {"message": "Welcome to the AI Book Backend!"}
