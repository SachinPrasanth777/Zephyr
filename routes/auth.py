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
        raise HTTPException(
            status_code=409, detail="User already exists"
        )
