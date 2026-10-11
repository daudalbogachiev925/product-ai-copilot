from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:pass@db:5432/copilot"
    EMBED_MODEL: str = "paraphrase-multilingual-MiniLM-L12-v2"
    TOP_K: int = 3
    MIN_SCORE: float = 0.2
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
