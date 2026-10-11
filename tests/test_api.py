def test_health(client):
    assert client.get("/health").json()["status"] == "ok"

def test_add_document(client):
    r = client.post("/api/documents", json={
        "title": "Roadmap Q4", "category": "roadmap",
        "text": "AI Search, SSO, Mobile v2"})
    assert r.status_code == 201

def test_chat(client):
    client.post("/api/documents", json={
        "title": "AI Intro", "text": "AI is artificial intelligence"})
    r = client.post("/api/chat", json={"question": "What is AI?"})
    assert r.status_code == 200
    assert "answer" in r.json()

def test_admin_stats(client):
    r = client.get("/api/admin/stats")
    assert r.status_code == 200
    assert "documents" in r.json()

def test_empty_question(client):
    r = client.post("/api/chat", json={"question": "   "})
    assert r.status_code == 400
