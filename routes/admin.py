## Note: This file contains the routes for the admin panel
## These routes should be deployed in a separate endpoint

from utilities.admin import supabase
from fastapi import APIRouter
from utilities.response import JSONResponse
from schema.schema import CreateUser

admin_router = APIRouter()


@admin_router.get("/user/{id}")
async def get_user(id: str):
    try:
        user = supabase.auth.admin.get_user_by_id(id)
        return user
    except Exception:
        return JSONResponse(status_code=404, content={"message": "User not found"})


@admin_router.get("/users")
async def get_users():
    try:
        users = supabase.auth.admin.list_users()
        return users
    except Exception:
        return JSONResponse(status_code=404, content={"message": "Users not found"})


@admin_router.post("/create")
async def create(user: CreateUser):
    try:
        user = supabase.auth.admin.create_user(
            {
                "email": user.email,
                "password": user.password,
                "user_metadata": {"name": user.name},
            }
        )
        return user
    except Exception:
        return JSONResponse(status_code=409, content={"message": "User already exists"})


@admin_router.delete("/delete/{id}")
async def delete_user(id: str):
    try:
        user = supabase.auth.admin.delete_user(id)
        return JSONResponse(
            status_code=200, content={"message": "User deleted successfully"}
        )
    except Exception:
        return JSONResponse(status_code=404, content={"message": "User not found"})
