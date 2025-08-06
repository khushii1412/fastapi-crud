from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from blog_crud import schemas, crud
from blog_crud.database import get_db
from blog_crud.schemas import PaginatedResponse, ShowUser

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=schemas.ShowUser)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@router.get("/", response_model=PaginatedResponse[ShowUser])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    total = crud.get_users_count(db)
    return PaginatedResponse(
        total=total,
        skip=skip,
        limit=limit,
        data=users
    )


@router.get("/{user_id}", response_model=schemas.ShowUser)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=schemas.ShowUser)
def update_user(user_id: int, updated_user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, updated_user)


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)
