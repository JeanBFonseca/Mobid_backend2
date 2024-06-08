from sqlalchemy import Column, Integer, String, ForeignKey, BLOB
from sqlalchemy.orm import relationship
from config.database import Base

class Veiculo(Base):
    __tablename__ = 'tb_veiculo'

    veiculo_id = Column(Integer, primary_key=True, index=True)
    motorista_id = Column(Integer, ForeignKey("tb_motorista.motorista_id"), nullable=False)
    placa = Column(String, nullable=False)
    renavam = Column(Integer, nullable=False)
    chassis = Column(String, nullable=False)
    ano_fabricacao = Column(Integer, nullable=False)  # Usando Integer para representar o ano de fabricação
    cor = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    foto_veiculo = Column(BLOB, nullable=False)

    motorista = relationship("Motorista", back_populates="veiculos")
