from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Cliente(Base):
    __tablename__ = 'tb_cliente'

    cliente_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    cep = Column(String, ForeignKey("tb_endereco.cep"), nullable=False)
    telefone = Column(String, nullable=False)
    dt_nascimento = Column(Date, nullable=False)
    sexo = Column(String, nullable=False)

    endereco = relationship("Endereco", back_populates="clientes")
