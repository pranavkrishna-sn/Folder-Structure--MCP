from fastapi import APIRouter
from services import sample_service

router = APIRouter()

@router.get("/sample")
async def read_sample():
    return sample_service.sample_function()
