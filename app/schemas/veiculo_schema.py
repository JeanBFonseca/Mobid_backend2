from pydantic import BaseModel, ConfigDict
from datetime import date

class VeiculoBase(BaseModel):
    tb_motorista_motorista_id: int
    placa: str
    renavam: int
    chassis: str
    ano_fabricacao: date
    cor: str
    modelo: str
    foto_veiculo: bytes = None

class VeiculoRequest(VeiculoBase):
    ...

class VeiculoResponse(VeiculoBase):
    veiculo_id: int

    model_config = ConfigDict(from_attributes=True)
