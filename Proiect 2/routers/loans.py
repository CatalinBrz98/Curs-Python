from typing import List, Tuple

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import func, Row
from sqlalchemy.orm import Session

from schemas import BookStat, UserLogin
from dependencies import auth_user
from db import create_session
from models import BookModel, UserModel, LoanModel

router = APIRouter(prefix="/loans", tags=["loans"])


@router.post('/{title}')
def loan_book(title: str, login_user: UserLogin, db: Session = Depends(create_session)):
    if not auth_user(login_user, db):
        raise HTTPException(status_code=401, detail="Wrong user details")
    user: UserModel | None = db.query(UserModel).filter(UserModel.username == login_user.username).first()
    book: BookModel | None = db.query(BookModel).filter(BookModel.title == title).first()

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    if not book.available():
        raise HTTPException(status_code=422, detail="Book is still loaned")

    loan = LoanModel(book=book, user=user)
    db.add(loan)
    db.commit()
    return {"status": "Success"}


@router.post('/{title}/return')
def return_book(title: str, login_user: UserLogin, db: Session = Depends(create_session)):
    if not auth_user(login_user, db):
        raise HTTPException(status_code=401, detail="Wrong user details")
    user: UserModel | None = db.query(UserModel).filter(UserModel.username == login_user.username).first()
    book: BookModel | None = db.query(BookModel).filter(BookModel.title == title).first()

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    loan: LoanModel | None = db.query(LoanModel).filter(LoanModel.book_id == book.id,
                                                        LoanModel.is_active == True).first()

    if loan is None:
        raise HTTPException(status_code=422, detail="Book is not currently loaned")
    elif loan.user.id != user.id:
        raise HTTPException(status_code=422, detail="Book is loaned by someone else")

    loan.is_active = False
    db.commit()
    return {"status": "Success"}


@router.get('/stats/top-books')
def get_top_books(db: Session = Depends(create_session)):
    top_stats: List[Row[Tuple[BookModel, int]]] = db.query(BookModel, func.count(LoanModel.book_id)).group_by(LoanModel.book_id).join(
        LoanModel.book).order_by(func.count(LoanModel.book_id).desc()).limit(5).all()
    return [BookStat(title=top_stat[0].title, loan_count=top_stat[1]) for top_stat in top_stats]
