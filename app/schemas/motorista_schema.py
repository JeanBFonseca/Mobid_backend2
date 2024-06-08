from pydantic import BaseModel
from datetime import date

class MotoristaBase(BaseModel):
    nome: str
    cpf: str
    email: str
    senha: str
    rg: str
    chn: str
    data_nascimento: date
    sexo: str
    nome_mae: str
    cep: str
    telefone: str
    foto: bytes

class MotoristaCreate(MotoristaBase):
    pass

class Motorista(MotoristaBase):
    motorista_id: int

    class Config:
        from_attributes = True  # Alterado de 'orm_mode' para 'from_attributes'
