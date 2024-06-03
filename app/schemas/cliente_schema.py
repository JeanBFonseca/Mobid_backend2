from pydantic import BaseModel, ConfigDict
from datetime import date

class ClienteBase(BaseModel): 
    nome: str 
    cpf: str 
    email: str 
    senha: str 
    endereco: str 
    telefone: str 
    dt_nascimento: date
    sexo: str 

class ClienteRequest(ClienteBase):
    ...

class ClienteResponse(ClienteBase):
    cliente_id: int

    model_config = ConfigDict(from_attributes=True)
