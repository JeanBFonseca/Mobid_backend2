from sqlalchemy.orm import Session
from models.agendamento_model import Agendamento
from schemas.agendamento_schema import AgendamentoCreate

def create_agendamento(db: Session, agendamento: AgendamentoCreate):
    db_agendamento = Agendamento(
        motorista_id=agendamento.motorista_id,
        veiculo_id=agendamento.veiculo_id,
        cliente_id=agendamento.cliente_id,
        data=agendamento.data,
        horario=agendamento.horario,
        localizacao=agendamento.localizacao,
        valor=agendamento.valor
    )
    db.add(db_agendamento)
    db.commit()
    db.refresh(db_agendamento)
    return db_agendamento

def get_agendamento(db: Session, agendamento_id: int):
    return db.query(Agendamento).filter(Agendamento.agendamento_id == agendamento_id).first()

def get_agendamentos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Agendamento).offset(skip).limit(limit).all()

def delete_agendamento(db: Session, agendamento_id: int):
    db_agendamento = get_agendamento(db, agendamento_id)
    if db_agendamento:
        db.delete(db_agendamento)
        db.commit()
        return db_agendamento
    return None
