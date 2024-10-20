from fastapi import APIRouter, HTTPException
from utilities.database import supabase
from schema.schema import User
from utilities.response import JSONResponse

router = APIRouter()
supabase = supabase()


@router.post("/signup")
async def signup(user: User):
    try:
        supabase.auth.sign_up({"email": user.email, "password": user.password})
        return JSONResponse(
            status_code=201, content={"message": "User signed up successfully"}
        )
    except Exception:
        raise HTTPException(status_code=409, detail="User already exists")


@router.post("/login")
async def login(user: User):
    try:
        supabase.auth.sign_in_with_password(
            {"email": user.email, "password": user.password}
        )
        token = supabase.auth.get_session().access_token
        return JSONResponse(
            status_code=200,
            content={"message": "User logged in successfully", "token": token},
        )
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid credentials")


@router.get("/user")
async def get_users():
    try:
        token = supabase.auth.get_session().access_token
        user = supabase.auth.get_user(token)
        return user
    except Exception:
        raise HTTPException(status_code=401, detail="Unauthorized User")

