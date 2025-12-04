from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    id: int
    username: str
    email: str

@router.get('/users/')
def read_users():
    return [{'id': 1, 'username': 'user1', 'email': 'user1@example.com'}]