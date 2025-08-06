from fastapi import FastAPI
from blog_crud.routes import users, blogs, auth

app = FastAPI()

app.include_router(users.router)
app.include_router(blogs.router)
app.include_router(auth.router)  # ✅ Add this line
