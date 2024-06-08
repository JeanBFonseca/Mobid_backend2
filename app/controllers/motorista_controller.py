from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import db
from repositories import motorista_repository
from schemas import motorista_schema
from typing import List

router = APIRouter()

@router.post("/motoristas/", response_model=motorista_schema.Motorista)
def create_motorista(motorista: motorista_schema.MotoristaCreate, db: Session = Depends(db.get_db)):
    return motorista_repository.create_motorista(db=db, motorista=motorista)

@router.get("/motoristas/", response_model=List[motorista_schema.Motorista])
def read_motoristas(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    return motorista_repository.get_motoristas(db=db, skip=skip, limit=limit)

@router.get("/motoristas/{motorista_id}", response_model=motorista_schema.Motorista)
def read_motorista(motorista_id: int, db: Session = Depends(db.get_db)):
    db_motorista = motorista_repository.get_motorista(db, motorista_id=motorista_id)
    if db_motorista is None:
        raise HTTPException(status_code=404, detail="Motorista not found")
    return db_motorista

@router.delete("/motoristas/{motorista_id}", response_model=motorista_schema.Motorista)
def delete_motorista(motorista_id: int, db: Session = Depends(db.get_db)):
    return motorista_repository.delete_motorista(db, motorista_id=motorista_id)
