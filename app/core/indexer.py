from sqlalchemy.orm import Session
from app.models import Document
from app.core.embedder import embed

def index_document(db: Session, title: str, text: str, category: str = None):
    vec = embed([text])[0]
    doc = Document(title=title, text=text, category=category,
                   embedding=vec.tolist())
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc

def index_batch(db: Session, docs: list):
    texts = [d["text"] for d in docs]
    vectors = embed(texts)
    created = []
    for d, v in zip(docs, vectors):
        doc = Document(title=d["title"], text=d["text"],
                        category=d.get("category"),
                        embedding=v.tolist())
        db.add(doc)
        created.append(doc)
    db.commit()
    return created
