from sqlalchemy import Column, Integer, String, Date, Time, Float, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Agendamento(Base):
    __tablename__ = 'tb_agendamento'

    agendamento_id = Column(Integer, primary_key=True, index=True)
    motorista_id = Column(Integer, ForeignKey("tb_motorista.motorista_id"), nullable=False)
    veiculo_id = Column(Integer, ForeignKey("tb_veiculo.veiculo_id"), nullable=False)
    cliente_id = Column(Integer, ForeignKey("tb_cliente.cliente_id"), nullable=False)
    data = Column(Date, nullable=False)
    horario = Column(Time, nullable=False)
    localizacao = Column(String, nullable=False)
    valor = Column(Float, nullable=False)

    motorista = relationship("Motorista")
    veiculo = relationship("Veiculo")
    cliente = relationship("Cliente")
