from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timedelta, date
from .. import models, schemas, database, deps

router = APIRouter(prefix="/expenses", tags=["expenses"])

@router.get("/", response_model=List[schemas.ExpenseOut])
def list_expenses(
    filter: Optional[str] = None, 
    start: Optional[date] = None, 
    end: Optional[date] = None,
    db: Session = Depends(database.get_db), 
    user: models.User = Depends(deps.get_current_user)):

    # Base query filtered by owner
    query = db.query(models.Expense).filter(models.Expense.owner_id == user.id)
    now = datetime.utcnow()

    # Apply filters based on parameters
    if filter == "week":
        start_date = now - timedelta(days=7)
        return query.filter(models.Expense.date >= start_date).all()
    elif filter == "month":
        start_date = now - timedelta(days=30)
        return query.filter(models.Expense.date >= start_date).all()
    elif filter == "3months":
        start_date = now - timedelta(days=90)
        return query.filter(models.Expense.date >= start_date).all()
    elif start and end:
        return query.filter(models.Expense.date.between(start, end)).all()
    return query.all()


# -------------- Create Expense Data ------------
@router.post("/", response_model=schemas.ExpenseOut)
def create_expense(
    expense: schemas.ExpenseCreate, 
    db: Session = Depends(database.get_db),
    user: models.User = Depends(deps.get_current_user)):

    # Convert Pydantic model to SQLAlchemy model
    db_expense = models.Expense(**expense.dict(), owner_id=user.id)

    # Database operations
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

# --------------- Update Expense Data --------------------
@router.put("/{expense_id}", response_model=schemas.ExpenseOut)
def update_expense(expense_id: int, expense: schemas.ExpenseUpdate, db: Session = Depends(database.get_db),
                   user: models.User = Depends(deps.get_current_user)):
    db_expense = db.query(models.Expense).filter_by(id=expense_id, owner_id=user.id).first()
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    for k, v in expense.dict().items():
        setattr(db_expense, k, v)
    db.commit()
    db.refresh(db_expense)
    return db_expense

# ----------------- Delete Expense Data --------------
@router.delete("/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(database.get_db),
                   user: models.User = Depends(deps.get_current_user)):
    db_expense = db.query(models.Expense).filter_by(id=expense_id, owner_id=user.id).first()
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    db.delete(db_expense)
    db.commit()
    return {"detail": "Deleted"}