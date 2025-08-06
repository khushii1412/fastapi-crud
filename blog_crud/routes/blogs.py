from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from blog_crud import schemas, models, database
from typing import List

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)

@router.get("/", response_model=List[schemas.ShowBlog])
def get_blogs(
    db: Session = Depends(database.get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100)
):
    return db.query(models.Blog).offset(skip).limit(limit).all()
