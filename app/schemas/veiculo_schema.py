from pydantic import BaseModel

class VeiculoBase(BaseModel):
    motorista_id: int
    placa: str
    renavam: int
    chassis: str
    ano_fabricacao: int
    cor: str
    modelo: str
    foto_veiculo: bytes

class VeiculoCreate(VeiculoBase):
    pass

class Veiculo(VeiculoBase):
    veiculo_id: int

    class Config:
        from_attributes = True  # Alterado de 'orm_mode' para 'from_attributes'
