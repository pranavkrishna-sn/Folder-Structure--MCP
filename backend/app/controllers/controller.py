from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi import HTTPException
from backend.app.services.article_service import ArticleService
from backend.app.services.user_service import UserService

app = FastAPI()
article_service = ArticleService()
user_service = UserService()