from sqlalchemy.orm import Session
from fastapi import HTTPException
from blog_crud import models, schemas

# --- USERS ---
def create_user(db: Session, user: schemas.UserCreate):
    existing = db.query(models.User).filter(models.User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user_model = models.User(name=user.name, email=user.email)
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    return user_model

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_users_count(db: Session):
    return db.query(models.User).count()

def get_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def update_user(db: Session, user_id: int, data: schemas.UserCreate):
    user = get_user(db, user_id)
    user.name = data.name
    user.email = data.email
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    db.delete(user)
    db.commit()
    return {"msg": "User deleted"}

# --- BLOGS ---
def create_blog(db: Session, blog: schemas.BlogCreate):
    blog_model = models.Blog(title=blog.title, content=blog.content, user_id=blog.user_id)
    db.add(blog_model)
    db.commit()
    db.refresh(blog_model)
    return blog_model

def get_blogs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Blog).offset(skip).limit(limit).all()

def get_blog(db: Session, blog_id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

def update_blog(db: Session, blog_id: int, data: schemas.BlogCreate):
    blog = get_blog(db, blog_id)
    blog.title = data.title
    blog.content = data.content
    blog.user_id = data.user_id
    db.commit()
    db.refresh(blog)
    return blog

def delete_blog(db: Session, blog_id: int):
    blog = get_blog(db, blog_id)
    db.delete(blog)
    db.commit()
    return {"msg": "Blog deleted"}
    
# Add this to crud.py
def get_users_count(db: Session):
    return db.query(models.User).count()
