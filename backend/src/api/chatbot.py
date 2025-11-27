
from fastapi import APIRouter, HTTPException, status
from typing import Optional

from backend.src.models.chatbot import ChatQueryRequest, ChatbotResponse, ReaderQuery
from backend.src.services.rag_service import RAGService

router = APIRouter()

# Initialize RAGService (in a real app, this would be dependency injected)
rag_service = RAGService()

@router.post("/query", response_model=ChatbotResponse)
async def chat_query(request: ChatQueryRequest):
    """Submit a query to the RAG chatbot."""
    reader_query = ReaderQuery(
        query_text=request.query_text,
        user_session_id=request.session_id # Pass session_id from request
    )
    response = await rag_service.process_query(reader_query)
    return response

@router.post("/query-with-context", response_model=ChatbotResponse)
async def chat_query_with_context(request: ChatQueryWithContextRequest):
    """Submit a query with selected text context to the RAG chatbot."""
    reader_query = ReaderQuery(
        query_text=request.query_text,
        user_session_id=request.session_id
    )
    response = await rag_service.process_query_with_context(reader_query, request.context_text)
    return response
