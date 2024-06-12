from pydantic import BaseModel
from datetime import datetime

class Viagem(BaseModel):
    """
    Classe que representa uma viagem.
    """
    agendamento_id: int  # ID do agendamento associado à viagem
    motorista_id: int  # ID do motorista responsável pela viagem
    cliente_id: int  # ID do cliente que solicitou a viagem
    hora_inicio: datetime  # Hora de início da viagem
    hora_termino: datetime  # Hora de término da viagem
    distancia: float  # Distância percorrida na viagem
    data: datetime  # Data da viagem
    forma_pagamento: str  # Forma de pagamento da viagem
    valor: float  # Valor da viagem
    viagem_id: int = None  # ID da viagem (opcional, será preenchido posteriormente)

    class Config:
        """
        Configuração da classe Viagem para permitir criar instâncias a partir de atributos.
        """
        from_attributes = True
