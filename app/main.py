from fastapi import FastAPI
from app.modules.user.controllers import router as user_router
from app.core.database import Base, engine

# Database Initialization
Base.metadata.create_all(bind=engine)

# App Initialization
app = FastAPI(title="FastAPI-Nest-Style")

# Register Routes
app.include_router(user_router, prefix="/api")
