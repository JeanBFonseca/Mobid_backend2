from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ViagemBaseModel(BaseModel):
    """
    Modelo base para viagenss.
    """
    agendamento_id: int
    motorista_id: int
    cliente_id: int
    hora_inicio: datetime
    hora_termino: datetime
    distancia: float
    data: datetime
    forma_pagamento: str
    valor: float

class ViagemCreateSchema(ViagemBaseModel):
    """
    Esquema para criação de viagens, baseado no modelo base.
    """
    pass

class ViagemModel(ViagemBaseModel):
    """
    Modelo completo para viagens, incluindo o ID da viagem.
    """
    viagem_id: int

class ViagemService:
    def __init__(self, db_session):
        self.db_session = db_session

    def criar_viagem(self, dados_viagem: ViagemCreateSchema):
        """
        Cria uma nova viagem no banco de dados.

        :param dados_viagem: Dados da viagem a serem inseridos
        :return: Viagem criada
        """
        db_viagem = ViagemModel(**dados_viagem.dict())
        self.db_session.add(db_viagem)
        self.db_session.commit()
        self.db_session.refresh(db_viagem)
        return db_viagem

    def buscar_viagem(self, viagem_id: int):
        """
        Busca uma viagem no banco de dados pelo seu ID.

        :param viagem_id: ID da viagem a ser buscada
        :return: Viagem encontrada, ou None se não encontrada
        """
        return self.db_session.query(ViagemModel).filter(ViagemModel.viagem_id == viagem_id).first()

    def listar_viagens(self, pular: int = 0, limite: int = 10):
        """
        Lista as viagens presentes no banco de dados.

        :param pular: Quantidade de registros a pular
        :param limite: Quantidade máxima de registros a serem retornados
        :return: Lista de viagens
        """
        return self.db_session.query(ViagemModel).offset(pular).limit(limite).all()

    def deletar_viagem(self, viagem_id: int):
        """
        Deleta uma viagem do banco de dados.

        :param viagem_id: ID da viagem a ser deletada
        :return: Viagem deletada, ou None se não encontrada
        """
        db_viagem = self.buscar_viagem(viagem_id)
        if db_viagem:
            self.db_session.delete(db_viagem)
            self.db_session.commit()
            return db_viagem
        return None
