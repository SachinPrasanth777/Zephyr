from fastapi import FastAPI
from routes.auth import router
from routes.admin import admin_router

app = FastAPI()

app.include_router(router, prefix="/auth")
app.include_router(admin_router, prefix="/admin")