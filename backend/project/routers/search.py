from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define the OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

# Define the search model
class Search(BaseModel):
    query: str

# Define the route for searching articles
@app.get('/search/')
def search_articles(search: Search, token: str = Depends(oauth2_scheme)):
    # Implement the logic for searching articles
    return []

# Define the route for searching users
@app.get('/search/users/')
def search_users(search: Search, token: str = Depends(oauth2_scheme)):
    # Implement the logic for searching users
    return {}