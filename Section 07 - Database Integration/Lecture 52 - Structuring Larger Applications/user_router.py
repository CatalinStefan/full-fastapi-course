from fastapi import APIRouter


user_router = APIRouter()

# Sample data
users = [{"id": 1, "name": "Fred Decker", "email": "Fredeck@example.com"}]

@user_router.get("/users/")
async def get_users():
    return users

@user_router.post("/users/")
async def add_user(user_id: int, name: str, email: str):
    new_user = {"id": user_id, "name": name, "email": email}
    users.append(new_user)
    return new_user