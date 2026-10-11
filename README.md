# product-ai-copilot
AI-ассистент Product Manager на базе RAG. Отвечает на вопросы по продуктовой базе (PRD, ресёрч, метрики, roadmap, гипотезы). Semantic search, FAQ-генерация, логирование диалогов, confidence-скоринг.  Стек: FastAPI, PostgreSQL, sentence-transformers, FAISS-like similarity, Streamlit, Docker, GitHub Actions.

# product-ai-copilot

AI-ассистент Product Manager на базе RAG.

## Возможности
- Загрузка документов (PRD, ресёрч, метрики)
- Semantic search по продуктовой базе
- Q&A с указанием источников и confidence
- Логирование диалогов
- Статистика использования
- Streamlit-дашборд

## Быстрый старт
cp .env.example .env
docker-compose up --build

API: http://localhost:8000/docs
Dashboard: http://localhost:8501

## Пример
curl -X POST http://localhost:8000/api/documents \
  -H "Content-Type: application/json" \
  -d '{"title":"AI Search PRD","category":"prd","text":"Цель: ускорить поиск в 5 раз"}'

curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"question":"Что такое AI Search?"}'

## Тесты
pytest tests/ -v

## Лицензия
MIT
