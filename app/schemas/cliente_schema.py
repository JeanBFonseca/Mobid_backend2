from pydantic import BaseModel
from datetime import date

class ClienteBase(BaseModel):
    nome: str
    cpf: str
    email: str
    senha: str
    cep: str
    telefone: str
    dt_nascimento: date
    sexo: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    cliente_id: int

    class Config:
        from_attributes = True  # Alterado de 'orm_mode' para 'from_attributes'
