from fastapi import APIRouter

from app.routes import prediction

api_router = APIRouter()

api_router.include_router(prediction.router, tags=['Prediction'])
