from sqlalchemy.orm import Session
from models.veiculo_model import VeiculoDB

class VeiculoRepository:
    @staticmethod
    def save(db: Session, veiculo: VeiculoDB) -> VeiculoDB:
        if veiculo.veiculo_id:
            db.merge(veiculo)
        else:
            db.add(veiculo)
        db.commit()
        return veiculo

    @staticmethod
    def find_by_id(db: Session, id: int) -> VeiculoDB:
        return db.query(VeiculoDB).filter(VeiculoDB.veiculo_id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(VeiculoDB).filter(VeiculoDB.veiculo_id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        veiculo = db.query(VeiculoDB).filter(VeiculoDB.veiculo_id == id).first()
        if veiculo is not None:
            db.delete(veiculo)
            db.commit()

    @staticmethod
    def find_all(db: Session) -> list[VeiculoDB]:
        return db.query(VeiculoDB).all()
