from fastapi import FastAPI
from sqlalchemy import text
from app.database import engine

app = FastAPI(title="MedAlerta", version="0.1.0")


@app.get("/")
def root():
    return {"mensagem": "MedAlerta online."}


@app.get("/db-check")
def db_check():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"banco": "conectado!"}
    