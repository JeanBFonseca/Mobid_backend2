from sqlalchemy import Column, Integer, String, Date, ForeignKey, BLOB
from sqlalchemy.orm import relationship
from config.database import Base

class Motorista(Base):
    __tablename__ = 'tb_motorista'

    motorista_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    rg = Column(String, nullable=False)
    chn = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    sexo = Column(String, nullable=False)
    nome_mae = Column(String, nullable=False)
    cep = Column(String, ForeignKey("tb_endereco.cep"), nullable=False)
    telefone = Column(String, nullable=False)
    foto = Column(BLOB, nullable=False)

    endereco = relationship("Endereco", back_populates="motoristas")
    veiculos = relationship("Veiculo", back_populates="motorista")
