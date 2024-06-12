from sqlalchemy import Column, Integer, String, ForeignKey, BLOB
from sqlalchemy.orm import relationship
from config.database import Base

class VeiculoRepository:
    """
    Classe responsável por operações relacionadas à persistência de Veiculo.
    """
    def __init__(self, db_session):
        """
        Inicializa a classe com uma sessão de banco de dados.
        """
        self.db_session = db_session
    
    def create_veiculo(self, veiculo_data):
        """
        Cria um novo veículo com os dados fornecidos.
        """
        # Lógica para criar um novo veículo no banco de dados
        # Retorna o veículo criado

    def get_veiculos(self, skip=0, limit=10):
        """
        Recupera uma lista de veículos com paginação.
        """
        # Lógica para recuperar uma lista de veículos do banco de dados com paginação
        # Retorna a lista de veículos
    
    def get_veiculo(self, veiculo_id):
        """
        Recupera um único veículo pelo seu ID.
        """
        # Lógica para recuperar um veículo pelo ID do banco de dados
        # Retorna o veículo encontrado ou None se não for encontrado

    def delete_veiculo(self, veiculo_id):
        """
        Exclui um veículo pelo seu ID.
        """
        # Lógica para excluir um veículo do banco de dados
        # Retorna o veículo excluído

class Veiculo(Base):
    """
    Classe de modelo que mapeia a tabela 'tb_veiculo' no banco de dados.
    """
    __tablename__ = 'tb_veiculo'

    id_veiculo = Column(Integer, primary_key=True, index=True)
    id_motorista = Column(Integer, ForeignKey("tb_motorista.id_motorista"), nullable=False)
    placa_veiculo = Column(String, nullable=False)
    renavam_veiculo = Column(Integer, nullable=False)
    chassis_veiculo = Column(String, nullable=False)
    ano_fabricacao_veiculo = Column(Integer, nullable=False)
    cor_veiculo = Column(String, nullable=False)
    modelo_veiculo = Column(String, nullable=False)
    foto_veiculo = Column(BLOB, nullable=False)

    motorista = relationship("Motorista", back_populates="veiculos")

    def __repr__(self):
        return f"Veiculo(id_veiculo={self.id_veiculo}, placa={self.placa_veiculo}, modelo={self.modelo_veiculo})"
