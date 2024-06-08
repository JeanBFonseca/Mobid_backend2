from sqlalchemy.orm import Session
from models.cliente_model import Cliente
from schemas.cliente_schema import ClienteCreate
import bcrypt

def create_cliente(db: Session, cliente: ClienteCreate):
    hashed_password = bcrypt.hashpw(cliente.senha.encode('utf-8'), bcrypt.gensalt())
    db_cliente = Cliente(
        nome=cliente.nome,
        cpf=cliente.cpf,
        email=cliente.email,
        senha=hashed_password,
        cep=cliente.cep,
        telefone=cliente.telefone,
        dt_nascimento=cliente.dt_nascimento,
        sexo=cliente.sexo
    )
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def get_cliente(db: Session, cliente_id: int):
    return db.query(Cliente).filter(Cliente.cliente_id == cliente_id).first()

def get_clientes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Cliente).offset(skip).limit(limit).all()

def delete_cliente(db: Session, cliente_id: int):
    db_cliente = get_cliente(db, cliente_id)
    if db_cliente:
        db.delete(db_cliente)
        db.commit()
        return db_cliente
    return None
