from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import ChatLog
from app.schemas import ChatRequest, ChatResponse
from app.core.retriever import answer

router = APIRouter()

@router.post("", response_model=ChatResponse)
def chat(payload: ChatRequest, db: Session = Depends(get_db)):
    if not payload.question.strip():
        raise HTTPException(400, "Question required")
    result = answer(db, payload.question)
    log = ChatLog(question=payload.question, answer=result["answer"],
                   sources=result["sources"],
                   confidence=str(result["confidence"]))
    db.add(log)
    db.commit()
    return result
