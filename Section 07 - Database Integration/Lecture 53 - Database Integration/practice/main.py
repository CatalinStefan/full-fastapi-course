from fastapi import FastAPI
from practice.routers.book_router import book_router
from practice.routers.user_router import user_router

app = FastAPI()

app.include_router(book_router)
app.include_router(user_router)
