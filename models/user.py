# models.py: This file contains the database models for the application
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    email: str
    
    class Config:
        orm_mode = True
