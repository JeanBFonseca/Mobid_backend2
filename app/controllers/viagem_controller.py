from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import db
from repositories import viagem_repository
from schemas import viagem_schema
from typing import List

router = APIRouter()

@router.post("/viagens/", response_model=viagem_schema.Viagem)
def create_viagem(viagem: viagem_schema.ViagemCreate, db: Session = Depends(db.get_db)):
    return viagem_repository.create_viagem(db=db, viagem=viagem)

@router.get("/viagens/", response_model=List[viagem_schema.Viagem])
def read_viagens(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    return viagem_repository.get_viagens(db=db, skip=skip, limit=limit)

@router.get("/viagens/{viagem_id}", response_model=viagem_schema.Viagem)
def read_viagem(viagem_id: int, db: Session = Depends(db.get_db)):
    db_viagem = viagem_repository.get_viagem(db, viagem_id=viagem_id)
    if db_viagem is None:
        raise HTTPException(status_code=404, detail="Viagem not found")
    return db_viagem

@router.delete("/viagens/{viagem_id}", response_model=viagem_schema.Viagem)
def delete_viagem(viagem_id: int, db: Session = Depends(db.get_db)):
    return viagem_repository.delete_viagem(db, viagem_id=viagem_id)
