from app.database import SessionLocal
from app.core.indexer import index_document

DOCS = [
    {"title": "AI Search PRD", "category": "prd",
     "text": "Цель AI Search — ускорить поиск по документам в 5 раз. Метрика: time to answer. Целевая аудитория — enterprise-клиенты."},
    {"title": "Q4 Research", "category": "research",
     "text": "NPS 32, retention D7 28%. Главная боль — сложный онбординг. 60% пользователей не доходят до first value."},
    {"title": "Roadmap Q4", "category": "roadmap",
     "text": "Планы Q4: AI Search, SSO, Mobile v2, Export PDF, Slack integration."},
    {"title": "Метрики продукта", "category": "metrics",
     "text": "DAU 15000, MAU 45000, stickiness 33%, churn 4.5%, ARPU 42."},
    {"title": "Конкуренты", "category": "competitors",
     "text": "Competitor_A лидирует по AI, Competitor_B — по цене, Competitor_C — по UX."},
    {"title": "Гипотеза онбординга", "category": "hypothesis",
     "text": "Если сократить онбординг на 3 шага, retention D7 вырастет на 15%."},
    {"title": "Сегменты", "category": "segments",
     "text": "Enterprise — 30% выручки, smb — 45%, consumer — 25%."},
    {"title": "Pricing", "category": "pricing",
     "text": "Basic 19, Pro 49, Enterprise 199. Средний ARPU 42."},
]

def seed():
    db = SessionLocal()
    try:
        for d in DOCS:
            index_document(db, d["title"], d["text"], d["category"])
        print(f"Seeded {len(DOCS)} documents")
    finally:
        db.close()

if __name__ == "__main__":
    seed()
