from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ClienteDB(Base):
    __tablename__ = "tb_cliente"

    cliente_id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String(255), nullable=False)
    cpf: str = Column(String(11), nullable=False)
    email: str = Column(String(255), nullable=False)
    senha: str = Column(String(255), nullable=False)
    endereco: str = Column(String(255), nullable=False)
    telefone: str = Column(String(11), nullable=False)
    dt_nascimento: Date = Column(Date, nullable=False)
    sexo: str  = Column(String(9), nullable=False)