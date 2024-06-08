from sqlalchemy.orm import Session
from models.veiculo_model import Veiculo
from schemas.veiculo_schema import VeiculoCreate

def create_veiculo(db: Session, veiculo: VeiculoCreate):
    db_veiculo = Veiculo(
        motorista_id=veiculo.motorista_id,
        placa=veiculo.placa,
        renavam=veiculo.renavam,
        chassis=veiculo.chassis,
        ano_fabricacao=veiculo.ano_fabricacao,
        cor=veiculo.cor,
        modelo=veiculo.modelo,
        foto_veiculo=veiculo.foto_veiculo
    )
    db.add(db_veiculo)
    db.commit()
    db.refresh(db_veiculo)
    return db_veiculo

def get_veiculo(db: Session, veiculo_id: int):
    return db.query(Veiculo).filter(Veiculo.veiculo_id == veiculo_id).first()

def get_veiculos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Veiculo).offset(skip).limit(limit).all()

def delete_veiculo(db: Session, veiculo_id: int):
    db_veiculo = get_veiculo(db, veiculo_id)
    if db_veiculo:
        db.delete(db_veiculo)
        db.commit()
        return db_veiculo
    return None
