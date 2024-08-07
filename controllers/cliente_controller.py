from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from fastapi.responses import Response
from dependencies.db import get_db
from schemas.cliente_schema import ClienteRequest, ClienteResponse
from models.cliente_model import ClienteDB
from repositories.cliente_repository import ClienteRepository
import bcrypt
def criptografar(senha:str)->str:
    senha_byte=senha.encode("utf-8")
    senha_criptografada=bcrypt.hashpw(senha_byte,bcrypt.gensalt())
    return senha_criptografada.decode("utf-8")

def create_cliente(request: ClienteRequest, db: Session = Depends(get_db)):
   criptografar_senha=criptografar(request.senha)
   cliente=ClienteDB(nome=request.nome, cpf=request.cpf, email=request.email, senha=criptografar_senha, cep=request.cep, telefone=request.telefone, dt_nascimento=request.dt_nascimento, sexo=request.sexo)
   db.add(cliente)
   db.commit()
   db.refresh(cliente)
   return cliente

def get_all_clientes(db: Session = Depends(get_db)):
    clientes = ClienteRepository.find_all(db)
    return [ClienteResponse.model_validate(cliente) for cliente in clientes]

def get_cliente_by_id(id: int, db: Session = Depends(get_db)):
    cliente = ClienteRepository.find_by_id(db, id)
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado"
        )
    return ClienteResponse.model_validate(cliente)

def delete_cliente_by_id(id: int, db: Session = Depends(get_db)):
    if not ClienteRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado"
        )
    ClienteRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def update_cliente(id: int, request: ClienteRequest, db: Session = Depends(get_db)):
    if not ClienteRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado"
        )
    cliente = ClienteRepository.save(db, ClienteDB(id=id, **request.model_dump.dict()))
    return ClienteResponse.model_validate(cliente)
