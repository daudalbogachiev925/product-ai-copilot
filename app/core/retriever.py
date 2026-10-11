import numpy as np
from sqlalchemy.orm import Session
from app.models import Document
from app.core.embedder import embed
from app.config import settings

def retrieve(db: Session, query: str, k: int = None):
    k = k or settings.TOP_K
    docs = db.query(Document).filter(Document.embedding.isnot(None)).all()
    if not docs:
        return []
    q_vec = embed([query])[0]
    scored = []
    for d in docs:
        v = np.array(d.embedding)
        score = float(np.dot(q_vec, v))
        scored.append((score, d))
    scored.sort(key=lambda x: -x[0])
    return [{"doc_id": d.id, "title": d.title, "text": d.text,
             "category": d.category, "score": round(s, 4)}
            for s, d in scored[:k] if s >= settings.MIN_SCORE]

def answer(db: Session, query: str):
    hits = retrieve(db, query)
    if not hits:
        return {"question": query,
                "answer": "Нет релевантных документов в базе.",
                "sources": [], "confidence": 0.0}
    ctx = hits[0]
    answer_text = f"[{ctx['title']}] {ctx['text'][:400]}"
    return {"question": query, "answer": answer_text,
            "sources": [{"title": h["title"], "score": h["score"]}
                        for h in hits],
            "confidence": round(ctx["score"], 4)}
