from pydantic import BaseModel, ConfigDict
from datetime import date

class MotoristaBase(BaseModel):
    cpf: str
    rg: str
    chn: str
    data_nascimento: date
    sexo: str
    nome_mae: str
    endereco: str
    telefone: str
    foto: bytes = None

class MotoristaRequest(MotoristaBase):
    ...

class MotoristaResponse(MotoristaBase):
    motorista_id: int

    model_config = ConfigDict(from_attributes=True)
