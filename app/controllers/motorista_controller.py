from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from fastapi.responses import Response
from dependencies.db import get_db
from schemas.motorista_schema import MotoristaRequest, MotoristaResponse
from models.motorista_model import MotoristaDB
from repositories.motorista_repository import MotoristaRepository

def create_motorista(request: MotoristaRequest, db: Session = Depends(get_db)):
    motorista = MotoristaRepository.save(db, MotoristaDB(**request.model_dump()))
    return MotoristaResponse.model_validate(motorista)

def get_all_motoristas(db: Session = Depends(get_db)):
    motoristas = MotoristaRepository.find_all(db)
    return [MotoristaResponse.model_validate(motorista) for motorista in motoristas]

def get_motorista_by_id(id: int, db: Session = Depends(get_db)):
    motorista = MotoristaRepository.find_by_id(db, id)
    if not motorista:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Motorista não encontrado"
        )
    return MotoristaResponse.model_validate(motorista)

def delete_motorista_by_id(id: int, db: Session = Depends(get_db)):
    if not MotoristaRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Motorista não encontrado"
        )
    MotoristaRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def update_motorista(id: int, request: MotoristaRequest, db: Session = Depends(get_db)):
    if not MotoristaRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Motorista não encontrado"
        )
    motorista = MotoristaRepository.save(db, MotoristaDB(id=id, **request.model_dump.dict()))
    return MotoristaResponse.model_validate(motorista)
