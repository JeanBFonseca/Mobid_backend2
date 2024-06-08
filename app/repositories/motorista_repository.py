from sqlalchemy.orm import Session
from models.motorista_model import Motorista
from schemas.motorista_schema import MotoristaCreate
import bcrypt

def create_motorista(db: Session, motorista: MotoristaCreate):
    hashed_password = bcrypt.hashpw(motorista.senha.encode('utf-8'), bcrypt.gensalt())
    db_motorista = Motorista(
        nome=motorista.nome,
        cpf=motorista.cpf,
        email=motorista.email,
        senha=hashed_password,
        rg=motorista.rg,
        chn=motorista.chn,
        data_nascimento=motorista.data_nascimento,
        sexo=motorista.sexo,
        nome_mae=motorista.nome_mae,
        cep=motorista.cep,
        telefone=motorista.telefone,
        foto=motorista.foto
    )
    db.add(db_motorista)
    db.commit()
    db.refresh(db_motorista)
    return db_motorista

def get_motorista(db: Session, motorista_id: int):
    return db.query(Motorista).filter(Motorista.motorista_id == motorista_id).first()

def get_motoristas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Motorista).offset(skip).limit(limit).all()

def delete_motorista(db: Session, motorista_id: int):
    db_motorista = get_motorista(db, motorista_id)
    if db_motorista:
        db.delete(db_motorista)
        db.commit()
        return db
