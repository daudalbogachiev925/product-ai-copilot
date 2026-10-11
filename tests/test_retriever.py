from app.core.indexer import index_document
from app.core.retriever import retrieve, answer

def test_retrieve_empty(db):
    assert retrieve(db, "test") == []

def test_retrieve_basic(db):
    index_document(db, "AI Intro", "Искусственный интеллект — это область CS", "tech")
    index_document(db, "Pricing", "Стратегия ценообразования", "business")
    hits = retrieve(db, "что такое AI", k=2)
    assert len(hits) >= 1
    assert hits[0]["title"] == "AI Intro"

def test_answer_no_match(db):
    r = answer(db, "совсем не по теме 123")
    assert r["confidence"] == 0.0
