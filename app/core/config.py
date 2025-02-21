from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"
    APP_NAME: str = "FastAPI-Nest-Style"

settings = Settings()
