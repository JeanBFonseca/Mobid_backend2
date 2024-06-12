from sqlalchemy.orm import Session
from models.agendamento_model import Agendamento
from schemas.agendamento_schema import AgendamentoCreate

class AgendamentoRepository:
    """
    Classe responsável por operações relacionadas à persistência de Agendamento.
    """
    def __init__(self, db: Session):
        """
        Inicializa a classe com uma sessão de banco de dados.
        """
        self.db = db
    
    def criar_agendamento(self, dados_agendamento: AgendamentoCreate):
        """
        Cria um novo agendamento no banco de dados.

        :param dados_agendamento: Dados do agendamento a serem inseridos
        :return: Agendamento criado
        """
        db_agendamento = Agendamento(
            motorista_id=dados_agendamento.motorista_id,
            veiculo_id=dados_agendamento.veiculo_id,
            cliente_id=dados_agendamento.cliente_id,
            data=dados_agendamento.data,
            horario=dados_agendamento.horario,
            localizacao=dados_agendamento.localizacao,
            valor=dados_agendamento.valor
        )
        self.db.add(db_agendamento)
        self.db.commit()
        self.db.refresh(db_agendamento)
        return db_agendamento

    def buscar_agendamento(self, agendamento_id: int):
        """
        Busca um agendamento no banco de dados pelo seu ID.

        :param agendamento_id: ID do agendamento a ser buscado
        :return: Agendamento encontrado, ou None se não encontrado
        """
        return self.db.query(Agendamento).filter(Agendamento.agendamento_id == agendamento_id).first()

    def listar_agendamentos(self, pular: int = 0, limite: int = 10):
        """
        Lista os agendamentos presentes no banco de dados.

        :param pular: Quantidade de registros a pular
        :param limite: Quantidade máxima de registros a serem retornados
        :return: Lista de agendamentos
        """
        return self.db.query(Agendamento).offset(pular).limit(limite).all()

    def deletar_agendamento(self, agendamento_id: int):
        """
        Deleta um agendamento do banco de dados.

        :param agendamento_id: ID do agendamento a ser deletado
        :return: Agendamento deletado, ou None se não encontrado
        """
        db_agendamento = self.buscar_agendamento(agendamento_id)
        if db_agendamento:
            self.db.delete(db_agendamento)
            self.db.commit()
            return db_agendamento
        return None