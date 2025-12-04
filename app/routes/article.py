from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Article(BaseModel):
    id: int
    title: str
    content: str

@router.post("/article/")
def create_article(article: Article):
    return {"message": "Article created successfully"}