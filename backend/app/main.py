from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi import HTTPException
from backend.app.services.article_service import ArticleService
from backend.app.services.user_service import UserService

app = FastAPI()
article_service = ArticleService()
user_service = UserService()

@app.post("/article")
def create_article(article: Article):
    article_service.create_article(article)
    return JSONResponse(content={"message": "Article created successfully"}, status_code=201)

@app.post("/user")
def create_user(user: User):
    user_service.create_user(user)
    return JSONResponse(content={"message": "User created successfully"}, status_code=201)