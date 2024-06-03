from sqlalchemy import Column, Integer, String, Date, BLOB
from config.database import Base

class MotoristaDB(Base):
    __tablename__ = "tb_motorista"

    motorista_id: int = Column(Integer, primary_key=True, index=True)
    cpf: str = Column(String(11), nullable=False)
    rg: str = Column(String(9), nullable=False)
    chn: str = Column(String(9), nullable=False)
    data_nascimento: Date = Column(Date, nullable=False)
    sexo: str = Column(String(9), nullable=False)
    nome_mae: str = Column(String(255), nullable=False)
    endereco: str = Column(String(255), nullable=False)
    telefone: str = Column(String(11), nullable=False)
    foto: BLOB = Column(BLOB, nullable=True)
