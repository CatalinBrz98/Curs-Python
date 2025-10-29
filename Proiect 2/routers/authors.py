from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from schemas import AuthorCreate, AuthorInfo
from models import AuthorModel
from db import create_session

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get('')
def get_authors(db: Session = Depends(create_session)):
    authors: List[AuthorModel] = db.query(AuthorModel).all()
    return [AuthorInfo(name=author.name, birth_date=author.birth_date, death_date=author.death_date,
                       books_count=len(author.books)) for author in authors]


@router.get('/{name}')
def get_authors_by_name(name: str, db: Session = Depends(create_session)):
    authors: List[AuthorModel] = db.query(AuthorModel).filter(AuthorModel.name.ilike(f"%{name}%")).all()
    return [AuthorInfo(name=author.name, birth_date=author.birth_date, death_date=author.death_date,
                       books_count=len(author.books)) for author in authors]


@router.post('/create')
def create_author(new_author: AuthorCreate, db: Session = Depends(create_session)):
    existing_author = db.query(AuthorModel).filter(AuthorModel.name == new_author.name).first()
    if existing_author is None:
        author = AuthorModel(name=new_author.name, birth_date=new_author.birth_date, death_date=new_author.death_date)
        db.add(author)
        db.commit()
        return {"status": "Success"}
    else:
        raise HTTPException(status_code=422, detail="This author already exists")
