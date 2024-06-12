from sqlalchemy.orm import Session
from models import Viagem

class ViagemRepository:
    """
    Classe responsável por operações relacionadas à persistência de Viagem.
    """
    def __init__(self, db_session: Session):
        """
        Inicializa a classe com uma sessão de banco de dados.
        """
        self.db_session = db_session
    
    def create_viagem(self, viagem_data):
        """
        Cria uma nova viagem com os dados fornecidos.
        """
        nova_viagem = Viagem(**viagem_data)
        self.db_session.add(nova_viagem)
        self.db_session.commit()
        return nova_viagem

    def get_viagens(self, skip=0, limit=10):
        """
        Recupera uma lista de viagens com paginação.
        """
        return self.db_session.query(Viagem).offset(skip).limit(limit).all()
    
    def get_viagem(self, viagem_id):
        """
        Recupera uma única viagem pelo seu ID.
        """
        return self.db_session.query(Viagem).filter(Viagem.id_viagem == viagem_id).first()

    def delete_viagem(self, viagem_id):
        """
        Exclui uma viagem pelo seu ID.
        """
        viagem = self.get_viagem(viagem_id)
        if viagem:
            self.db_session.delete(viagem)
            self.db_session.commit()
            return viagem
        return None

