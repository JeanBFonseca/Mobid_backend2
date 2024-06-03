from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from fastapi.responses import Response
from dependencies.db import get_db
from schemas.veiculo_schema import VeiculoRequest, VeiculoResponse
from models.veiculo_model import VeiculoDB
from repositories.veiculo_repository import VeiculoRepository

def create_veiculo(request: VeiculoRequest, db: Session = Depends(get_db)):
    veiculo = VeiculoRepository.save(db, VeiculoDB(**request.model_dump()))
    return VeiculoResponse.model_validate(veiculo)

def get_all_veiculos(db: Session = Depends(get_db)):
    veiculos = VeiculoRepository.find_all(db)
    return [VeiculoResponse.model_validate(veiculo) for veiculo in veiculos]

def get_veiculo_by_id(id: int, db: Session = Depends(get_db)):
    veiculo = VeiculoRepository.find_by_id(db, id)
    if not veiculo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Veículo não encontrado"
        )
    return VeiculoResponse.model_validate(veiculo)

def delete_veiculo_by_id(id: int, db: Session = Depends(get_db)):
    if not VeiculoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Veículo não encontrado"
        )
    VeiculoRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def update_veiculo(id: int, request: VeiculoRequest, db: Session = Depends(get_db)):
    if not VeiculoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Veículo não encontrado"
        )
    veiculo = VeiculoRepository.save(db, VeiculoDB(id=id, **request.model_dump.dict()))
    return VeiculoResponse.model_validate(veiculo)
