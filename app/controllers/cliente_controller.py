from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import db
from repositories import cliente_repository
from schemas import cliente_schema
from typing import List

router = APIRouter()

@router.post("/clientes/", response_model=cliente_schema.Cliente)
def create_cliente(cliente: cliente_schema.ClienteCreate, db: Session = Depends(db.get_db)):
    return cliente_repository.create_cliente(db=db, cliente=cliente)

@router.get("/clientes/", response_model=List[cliente_schema.Cliente])
def read_clientes(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    return cliente_repository.get_clientes(db=db, skip=skip, limit=limit)

@router.get("/clientes/{cliente_id}", response_model=cliente_schema.Cliente)
def read_cliente(cliente_id: int, db: Session = Depends(db.get_db)):
    db_cliente = cliente_repository.get_cliente(db, cliente_id=cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return db_cliente

@router.delete("/clientes/{cliente_id}", response_model=cliente_schema.Cliente)
def delete_cliente(cliente_id: int, db: Session = Depends(db.get_db)):
    return cliente_repository.delete_cliente(db, cliente_id=cliente_id)
