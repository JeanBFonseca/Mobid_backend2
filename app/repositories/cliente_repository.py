from sqlalchemy.orm import Session
from models.cliente_model import ClienteDB

class ClienteRepository:
    @staticmethod
    def save(db: Session, cliente: ClienteDB) -> ClienteDB:
        if cliente.cliente_id:
            db.merge(cliente)
        else:
            db.add(cliente)
        db.commit()
        return cliente

    @staticmethod
    def find_by_id(db: Session, id: int) -> ClienteDB:
        return db.query(ClienteDB).filter(ClienteDB.cliente_id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(ClienteDB).filter(ClienteDB.cliente_id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        cliente = db.query(ClienteDB).filter(ClienteDB.cliente_id == id).first()
        if cliente is not None:
            db.delete(cliente)
            db.commit()