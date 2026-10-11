from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.sql import func
from app.database import Base

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True, nullable=False)
    category = Column(String, index=True)
    text = Column(Text, nullable=False)
    embedding = Column(JSON)
    created_at = Column(DateTime, server_default=func.now())

class ChatLog(Base):
    __tablename__ = "chat_logs"
    id = Column(Integer, primary_key=True)
    question = Column(Text, nullable=False)
    answer = Column(Text)
    sources = Column(JSON)
    confidence = Column(String)
    created_at = Column(DateTime, server_default=func.now(), index=True)
