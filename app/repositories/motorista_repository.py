from sqlalchemy.orm import Session
from models.motorista_model import Motorista
from schemas.motorista_schema import MotoristaCreate
import bcrypt

class MotoristaService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def criar_motorista(self, dados_motorista: MotoristaCreate):
        """
        Cria um novo motorista no banco de dados.

        :param dados_motorista: Dados do motorista a serem inseridos
        :return: Motorista criado
        """
        hashed_password = bcrypt.hashpw(dados_motorista.senha.encode('utf-8'), bcrypt.gensalt())
        db_motorista = Motorista(
            nome=dados_motorista.nome,
            cpf=dados_motorista.cpf,
            email=dados_motorista.email,
            senha=hashed_password,
            rg=dados_motorista.rg,
            chn=dados_motorista.chn,
            data_nascimento=dados_motorista.data_nascimento,
            sexo=dados_motorista.sexo,
            nome_mae=dados_motorista.nome_mae,
            cep=dados_motorista.cep,
            telefone=dados_motorista.telefone,
            foto=dados_motorista.foto
        )
        self.db_session.add(db_motorista)
        self.db_session.commit()
        self.db_session.refresh(db_motorista)
        return db_motorista

    def buscar_motorista(self, motorista_id: int):
        """
        Busca um motorista no banco de dados pelo seu ID.

        :param motorista_id: ID do motorista a ser buscado
        :return: Motorista encontrado, ou None se não encontrado
        """
        return self.db_session.query(Motorista).filter(Motorista.motorista_id == motorista_id).first()

    def listar_motoristas(self, pular: int = 0, limite: int = 10):
        """
        Lista os motoristas presentes no banco de dados.

        :param pular: Quantidade de registros a pular
        :param limite: Quantidade máxima de registros a serem retornados
        :return: Lista de motoristas
        """
        return self.db_session.query(Motorista).offset(pular).limit(limite).all()

    def deletar_motorista(self, motorista_id: int):
        """
        Deleta um motorista do banco de dados.

        :param motorista_id: ID do motorista a ser deletado
        :return: Motorista deletado, ou None se não encontrado
        """
        db_motorista = self.buscar_motorista(motorista_id)
        if db_motorista:
            self.db_session.delete(db_motorista)
            self.db_session.commit()
            return db_motorista
        return None
