from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db
from app.models import Document, ChatLog
from app.schemas import StatsResponse

router = APIRouter()

@router.get("/stats", response_model=StatsResponse)
def stats(db: Session = Depends(get_db)):
    docs = db.query(Document).count()
    chats = db.query(ChatLog).count()
    rows = db.query(ChatLog).all()
    confs = []
    for r in rows:
        try:
            confs.append(float(r.confidence))
        except (ValueError, TypeError):
            continue
    avg = round(sum(confs) / len(confs), 4) if confs else 0.0
    return StatsResponse(documents=docs, chats=chats, avg_confidence=avg)

@router.get("/logs")
def logs(db: Session = Depends(get_db), limit: int = 100):
    rows = db.query(ChatLog).order_by(ChatLog.id.desc()).limit(limit).all()
    return [{"id": r.id, "question": r.question,
             "answer": (r.answer or "")[:200],
             "confidence": r.confidence} for r in rows]

@router.delete("/logs", status_code=204)
def clear_logs(db: Session = Depends(get_db)):
    db.query(ChatLog).delete()
    db.commit()
