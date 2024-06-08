from sqlalchemy import Column, Integer, String, ForeignKey, Float, Time, Date
from sqlalchemy.orm import relationship  # Importe a função relationship

from config.database import Base

class Viagem(Base):
    __tablename__ = 'tb_viagem'

    viagem_id = Column(Integer, primary_key=True, index=True)
    tb_agendamento_agendamento_id = Column(Integer, ForeignKey("tb_agendamento.agendamento_id"), nullable=False)
    tb_motorista_motorista_id = Column(Integer, ForeignKey("tb_motorista.motorista_id"), nullable=False)
    tb_cliente_cliente_id = Column(Integer, ForeignKey("tb_cliente.cliente_id"), nullable=False)
    hora_inicio = Column(Time, nullable=False)
    hora_termino = Column(Time, nullable=False)
    distancia = Column(Float, nullable=False)
    data_2 = Column(Date, nullable=False)
    forma_pagamento = Column(String, nullable=False)
    valor = Column(Float, nullable=False)

    agendamento = relationship("Agendamento")  # Adicione a definição do relacionamento
