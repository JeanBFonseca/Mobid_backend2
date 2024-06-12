from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class ClienteRepository:
    """
    Classe responsável por operações relacionadas à persistência de Cliente.
    """
    def __init__(self, db_session):
        """
        Inicializa a classe com uma sessão de banco de dados.
        """
        self.db_session = db_session
    
    def create_cliente(self, cliente_data):
        """
        Cria um novo cliente com os dados fornecidos.
        """
        # Lógica para criar um novo cliente no banco de dados
        # Retorna o cliente criado

    def get_clientes(self, skip=0, limit=10):
        """
        Recupera uma lista de clientes com paginação.
        """
        # Lógica para recuperar uma lista de clientes do banco de dados com paginação
        # Retorna a lista de clientes
    
    def get_cliente(self, cliente_id):
        """
        Recupera um único cliente pelo seu ID.
        """
        # Lógica para recuperar um cliente pelo ID do banco de dados
        # Retorna o cliente encontrado ou None se não for encontrado

    def delete_cliente(self, cliente_id):
        """
        Exclui um cliente pelo seu ID.
        """
        # Lógica para excluir um cliente do banco de dados
        # Retorna o cliente excluído

class Cliente(Base):
    """
    Classe de modelo que mapeia a tabela 'tb_cliente' no banco de dados.
    """
    __tablename__ = 'tb_cliente'

    id_cliente = Column(Integer, primary_key=True, index=True)
    nome_cliente = Column(String, nullable=False)
    cpf_cliente = Column(String, unique=True, nullable=False)
    email_cliente = Column(String, unique=True, nullable=False)
    senha_cliente = Column(String, nullable=False)
    cep_cliente = Column(String, ForeignKey("tb_endereco.cep"), nullable=False)
    telefone_cliente = Column(String, nullable=False)
    data_nascimento_cliente = Column(Date, nullable=False)
    sexo_cliente = Column(String, nullable=False)

    endereco = relationship("Endereco", back_populates="clientes")

    def __repr__(self):
        return f"Cliente(id_cliente={self.id_cliente}, nome={self.nome_cliente}, email={self.email_cliente})"

