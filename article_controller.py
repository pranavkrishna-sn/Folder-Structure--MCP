from fastapi import APIRouter, Depends
from pydantic import BaseModel

router = APIRouter()

class Article(BaseModel):
    id: int
    title: str
    content: str

@router.get('/articles')
def get_articles():
    return [{'id': 1, 'title': 'Article 1', 'content': 'This is article 1'}]