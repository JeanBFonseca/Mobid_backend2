from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import db
from repositories import veiculo_repository
from schemas import veiculo_schema
from typing import List

router = APIRouter()

@router.post("/veiculos/", response_model=veiculo_schema.Veiculo)
def create_veiculo(veiculo: veiculo_schema.VeiculoCreate, db: Session = Depends(db.get_db)):
    return veiculo_repository.create_veiculo(db=db, veiculo=veiculo)

@router.get("/veiculos/", response_model=List[veiculo_schema.Veiculo])
def read_veiculos(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    return veiculo_repository.get_veiculos(db=db, skip=skip, limit=limit)

@router.get("/veiculos/{veiculo_id}", response_model=veiculo_schema.Veiculo)
def read_veiculo(veiculo_id: int, db: Session = Depends(db.get_db)):
    db_veiculo = veiculo_repository.get_veiculo(db, veiculo_id=veiculo_id)
    if db_veiculo is None:
        raise HTTPException(status_code=404, detail="Veiculo not found")
    return db_veiculo

@router.delete("/veiculos/{veiculo_id}", response_model=veiculo_schema.Veiculo)
def delete_veiculo(veiculo_id: int, db: Session = Depends(db.get_db)):
    return veiculo_repository.delete_veiculo(db, veiculo_id=veiculo_id)
