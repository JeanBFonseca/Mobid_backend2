from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

class Endereco(Base):
    __tablename__ = 'tb_endereco'
    cep = Column(String, primary_key=True)
    logradouro = Column(String(255), nullable=False)
    bairro = Column(String(255), nullable=False)
    localidade = Column(String(255), nullable=False)
    uf = Column(String(255), nullable=False)