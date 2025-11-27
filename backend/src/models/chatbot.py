
from pydantic import BaseModel
from typing import List, Optional

class ReaderQuery(BaseModel):
    id: Optional[str] = None # For session persistence, if a new session starts
    query_text: str
    timestamp: Optional[str] = None # Will be set by the service
    user_session_id: Optional[str] = None

class ChatbotResponse(BaseModel):
    id: Optional[str] = None # Will be set by the service
    response_text: str
    source_content_ids: List[int]
    timestamp: Optional[str] = None # Will be set by the service
    query_id: Optional[str] = None # Reference to ReaderQuery ID
    session_id: Optional[str] = None # For session persistence

class ChatQueryRequest(BaseModel):
    query_text: str
    session_id: Optional[str] = None

class ChatQueryWithContextRequest(BaseModel):
    query_text: str
    context_text: str
    session_id: Optional[str] = None

