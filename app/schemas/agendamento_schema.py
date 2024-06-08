from pydantic import BaseModel
from datetime import date, time

class AgendamentoBase(BaseModel):
    motorista_id: int
    veiculo_id: int
    cliente_id: int
    data: date
    horario: time
    localizacao: str
    valor: float

class AgendamentoCreate(AgendamentoBase):
    pass

class Agendamento(AgendamentoBase):
    agendamento_id: int

    class Config:
        from_attributes = True  # Alterado de 'orm_mode' para 'from_attributes'
