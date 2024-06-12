from sqlalchemy.orm import Session
from models.cliente_model import Cliente
from schemas.cliente_schema import ClienteCreate
import bcrypt

def criar_cliente(db: Session, dados_cliente: ClienteCreate):
    """
    Cria um novo cliente no banco de dados.

    :param db: Sessão do banco de dados
    :param dados_cliente: Dados do cliente a serem inseridos
    :return: Cliente criado
    """
    hashed_password = bcrypt.hashpw(dados_cliente.senha.encode('utf-8'), bcrypt.gensalt())
    db_cliente = Cliente(
        nome=dados_cliente.nome,
        cpf=dados_cliente.cpf,
        email=dados_cliente.email,
        senha=hashed_password,
        cep=dados_cliente.cep,
        telefone=dados_cliente.telefone,
        dt_nascimento=dados_cliente.dt_nascimento,
        sexo=dados_cliente.sexo
    )
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def buscar_cliente(db: Session, cliente_id: int):
    """
    Busca um cliente no banco de dados pelo seu ID.

    :param db: Sessão do banco de dados
    :param cliente_id: ID do cliente a ser buscado
    :return: Cliente encontrado, ou None se não encontrado
    """
    return db.query(Cliente).filter(Cliente.cliente_id == cliente_id).first()

def listar_clientes(db: Session, pular: int = 0, limite: int = 10):
    """
    Lista os clientes presentes no banco de dados.

    :param db: Sessão do banco de dados
    :param pular: Quantidade de registros a pular
    :param limite: Quantidade máxima de registros a serem retornados
    :return: Lista de clientes
    """
    return db.query(Cliente).offset(pular).limit(limite).all()

def deletar_cliente(db: Session, cliente_id: int):
    """
    Deleta um cliente do banco de dados.

    :param db: Sessão do banco de dados
    :param cliente_id: ID do cliente a ser deletado
    :return: Cliente deletado, ou None se não encontrado
    """
    db_cliente = buscar_cliente(db, cliente_id)
    if db_cliente:
        db.delete(db_cliente)
        db.commit()
        return db_cliente
    return None