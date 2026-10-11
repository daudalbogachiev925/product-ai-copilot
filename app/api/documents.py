from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Document
from app.schemas import DocumentCreate, DocumentRead
from app.core.indexer import index_document, index_batch

router = APIRouter()

@router.post("", response_model=DocumentRead, status_code=201)
def create(payload: DocumentCreate, db: Session = Depends(get_db)):
    return index_document(db, payload.title, payload.text, payload.category)

@router.post("/batch", status_code=201)
def create_batch(payloads: List[DocumentCreate],
                 db: Session = Depends(get_db)):
    docs = [p.model_dump() for p in payloads]
    created = index_batch(db, docs)
    return {"inserted": len(created)}

@router.get("", response_model=List[DocumentRead])
def list_docs(db: Session = Depends(get_db), limit: int = 500):
    return db.query(Document).limit(limit).all()

@router.get("/{doc_id}", response_model=DocumentRead)
def get_one(doc_id: int, db: Session = Depends(get_db)):
    d = db.query(Document).get(doc_id)
    if not d:
        raise HTTPException(404, "Document not found")
    return d

@router.delete("/{doc_id}", status_code=204)
def delete(doc_id: int, db: Session = Depends(get_db)):
    d = db.query(Document).get(doc_id)
    if d:
        db.delete(d)
        db.commit()
