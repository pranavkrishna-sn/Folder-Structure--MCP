from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Article(BaseModel):
    title: str
    content: str

@router.post("/articles/")
def create_article(article: Article):
    return {"message": "Article created"}
