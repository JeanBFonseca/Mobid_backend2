from sqlalchemy.orm import Session
from models.motorista_model import MotoristaDB

class MotoristaRepository:
    @staticmethod
    def save(db: Session, motorista: MotoristaDB) -> MotoristaDB:
        if motorista.motorista_id:
            db.merge(motorista)
        else:
            db.add(motorista)
        db.commit()
        return motorista

    @staticmethod
    def find_by_id(db: Session, id: int) -> MotoristaDB:
        return db.query(MotoristaDB).filter(MotoristaDB.motorista_id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(MotoristaDB).filter(MotoristaDB.motorista_id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        motorista = db.query(MotoristaDB).filter(MotoristaDB.motorista_id == id).first()
        if motorista is not None:
            db.delete(motorista)
            db.commit()

    @staticmethod
    def find_all(db: Session) -> list[MotoristaDB]:
        return db.query(MotoristaDB).all()
