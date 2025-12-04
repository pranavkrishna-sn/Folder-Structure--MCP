from fastapi import FastAPI
from routers import sample_router

app = FastAPI()

app.include_router(sample_router.router)
