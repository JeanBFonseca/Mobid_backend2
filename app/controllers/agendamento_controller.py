from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import db
from repositories import agendamento_repository
from schemas import agendamento_schema
from typing import List

router = APIRouter()

@router.post("/agendamentos/", response_model=agendamento_schema.Agendamento)
def create_agendamento(agendamento: agendamento_schema.AgendamentoCreate, db: Session = Depends(db.get_db)):
    return agendamento_repository.create_agendamento(db=db, agendamento=agendamento)

@router.get("/agendamentos/", response_model=List[agendamento_schema.Agendamento])
def read_agendamentos(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    return agendamento_repository.get_agendamentos(db=db, skip=skip, limit=limit)

@router.get("/agendamentos/{agendamento_id}", response_model=agendamento_schema.Agendamento)
def read_agendamento(agendamento_id: int, db: Session = Depends(db.get_db)):
    db_agendamento = agendamento_repository.get_agendamento(db, agendamento_id=agendamento_id)
    if db_agendamento is None:
        raise HTTPException(status_code=404, detail="Agendamento not found")
    return db_agendamento

@router.delete("/agendamentos/{agendamento_id}", response_model=agendamento_schema.Agendamento)
def delete_agendamento(agendamento_id: int, db: Session = Depends(db.get_db)):
    return agendamento_repository.delete_agendamento(db, agendamento_id=agendamento_id)
