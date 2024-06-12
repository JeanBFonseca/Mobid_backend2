from sqlalchemy import Column, Integer, String, Date, ForeignKey, BLOB
from sqlalchemy.orm import relationship
from config.database import Base

class MotoristaRepository:
    """
    Classe responsável por operações relacionadas à persistência de Motorista.
    """
    def __init__(self, db_session):
        """
        Inicializa a classe com uma sessão de banco de dados.
        """
        self.db_session = db_session
    
    def create_motorista(self, motorista_data):
        """
        Cria um novo motorista com os dados fornecidos.
        """
        # Lógica para criar um novo motorista no banco de dados
        # Retorna o motorista criado

    def get_motoristas(self, skip=0, limit=10):
        """
        Recupera uma lista de motoristas com paginação.
        """
        # Lógica para recuperar uma lista de motoristas do banco de dados com paginação
        # Retorna a lista de motoristas
    
    def get_motorista(self, motorista_id):
        """
        Recupera um único motorista pelo seu ID.
        """
        # Lógica para recuperar um motorista pelo ID do banco de dados
        # Retorna o motorista encontrado ou None se não for encontrado

    def delete_motorista(self, motorista_id):
        """
        Exclui um motorista pelo seu ID.
        """
        # Lógica para excluir um motorista do banco de dados
        # Retorna o motorista excluído

class Motorista(Base):
    """
    Classe de modelo que mapeia a tabela 'tb_motorista' no banco de dados.
    """
    __tablename__ = 'tb_motorista'

    id_motorista = Column(Integer, primary_key=True, index=True)
    nome_motorista = Column(String, nullable=False)
    cpf_motorista = Column(String, unique=True, nullable=False)
    email_motorista = Column(String, unique=True, nullable=False)
    senha_motorista = Column(String, nullable=False)
    rg_motorista = Column(String, nullable=False)
    cnh_motorista = Column(String, nullable=False)
    data_nascimento_motorista = Column(Date, nullable=False)
    sexo_motorista = Column(String, nullable=False)
    nome_mae_motorista = Column(String, nullable=False)
    cep_motorista = Column(String, ForeignKey("tb_endereco.cep"), nullable=False)
    telefone_motorista = Column(String, nullable=False)
    foto_motorista = Column(BLOB, nullable=False)

    endereco = relationship("Endereco", back_populates="motoristas")
    veiculos = relationship("Veiculo", back_populates="motorista")

    def __repr__(self):
        return f"Motorista(id_motorista={self.id_motorista}, nome={self.nome_motorista}, email={self.email_motorista})"

