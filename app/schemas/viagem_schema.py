from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ViagemBase(BaseModel):
    agendamento_id: int
    motorista_id: int
    cliente_id: int
    hora_inicio: datetime
    hora_termino: datetime
    distancia: float
    data: datetime
    forma_pagamento: str
    valor: float

class ViagemCreate(ViagemBase):
    pass

class Viagem(ViagemBase):
    viagem_id: int

    class Config:
        from_attributes = True  # Alterado de 'orm_mode' para 'from_attributes'
