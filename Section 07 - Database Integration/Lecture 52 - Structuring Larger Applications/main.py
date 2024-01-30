#main.py
from fastapi import FastAPI
from routers.book_router import book_router
from routers.user_router import user_router


app = FastAPI()

# Including routers for different functionalities
app.include_router(book_router)
app.include_router(user_router)