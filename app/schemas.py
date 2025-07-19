from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class ExpenseBase(BaseModel):
    title: str
    amount: float
    date: datetime
    category: Literal[
        'Groceries', 'Leisure', 'Electronics', 'Utilities', 'Clothing', 'Health', 'Others']

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseUpdate(ExpenseBase):
    pass

class ExpenseOut(ExpenseBase):
    id: int
    class Config:
        orm_mode = True