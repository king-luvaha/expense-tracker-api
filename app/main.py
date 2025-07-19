from fastapi import FastAPI
from .database import Base, engine
from .routes import auth_routes, expense_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker API")
app.include_router(auth_routes.router)
app.include_router(expense_routes.router)