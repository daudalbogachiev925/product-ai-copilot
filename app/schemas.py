from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel

class DocumentCreate(BaseModel):
    title: str
    category: Optional[str] = None
    text: str

class DocumentRead(DocumentCreate):
    id: int
    class Config:
        from_attributes = True

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    question: str
    answer: str
    sources: List[Dict[str, Any]]
    confidence: float

class ChatLogRead(BaseModel):
    id: int
    question: str
    answer: Optional[str]
    confidence: Optional[str]
    created_at: Optional[datetime]
    class Config:
        from_attributes = True

class StatsResponse(BaseModel):
    documents: int
    chats: int
    avg_confidence: float
