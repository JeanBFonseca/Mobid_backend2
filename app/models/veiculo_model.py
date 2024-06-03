from sqlalchemy import Column, Integer, String, Date, BLOB
from config.database import Base

class VeiculoDB(Base):
    __tablename__ = "tb_veiculo"

    veiculo_id: int = Column(Integer, primary_key=True, index=True)
    tb_motorista_motorista_id: int = Column(Integer, nullable=False)
    placa: str = Column(String(7), nullable=True)
    renavam: int = Column(Integer, nullable=True)
    chassis: str = Column(String(17), nullable=True)
    ano_fabricacao: Date = Column(Date, nullable=True)
    cor: str = Column(String(50), nullable=True)
    modelo: str = Column(String(100), nullable=True)
    foto_veiculo: BLOB = Column(BLOB, nullable=True)
