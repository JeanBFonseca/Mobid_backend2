from sqlalchemy import Column, Integer, String, Date, Time, Float, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class AgendamentoRepository:
    """
    Classe responsável por operações relacionadas à persistência de Agendamento.
    """
    def __init__(self, db_session):
        """
        Inicializa a classe com uma sessão de banco de dados.
        """
        self.db_session = db_session
    
    def create_agendamento(self, agendamento_data):
        """
        Cria um novo agendamento com os dados fornecidos.
        """
        # Lógica para criar um novo agendamento no banco de dados
        # Retorna o agendamento criado

    def get_agendamentos(self, skip=0, limit=10):
        """
        Recupera uma lista de agendamentos com paginação.
        """
        # Lógica para recuperar uma lista de agendamentos do banco de dados com paginação
        # Retorna a lista de agendamentos
    
    def get_agendamento(self, agendamento_id):
        """
        Recupera um único agendamento pelo seu ID.
        """
        # Lógica para recuperar um agendamento pelo ID do banco de dados
        # Retorna o agendamento encontrado ou None se não for encontrado

    def delete_agendamento(self, agendamento_id):
        """
        Exclui um agendamento pelo seu ID.
        """
        # Lógica para excluir um agendamento do banco de dados
        # Retorna o agendamento excluído

class Agendamento(Base):
    """
    Classe de modelo que mapeia a tabela 'tb_agendamento' no banco de dados.
    """
    __tablename__ = 'tb_agendamento'

    id_agendamento = Column(Integer, primary_key=True, index=True)
    id_motorista = Column(Integer, ForeignKey("tb_motorista.id_motorista"), nullable=False)
    id_veiculo = Column(Integer, ForeignKey("tb_veiculo.id_veiculo"), nullable=False)
    id_cliente = Column(Integer, ForeignKey("tb_cliente.id_cliente"), nullable=False)
    data_agendamento = Column(Date, nullable=False)
    horario_agendamento = Column(Time, nullable=False)
    localizacao_agendamento = Column(String, nullable=False)
    valor_agendamento = Column(Float, nullable=False)

    motorista = relationship("Motorista")
    veiculo = relationship("Veiculo")
    cliente = relationship("Cliente")