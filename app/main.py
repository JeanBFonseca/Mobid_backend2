from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from controllers.cliente_controller import *
from controllers.motorista_controller import *
from controllers.veiculo_controller import *
from schemas.cliente_schema import ClienteRequest, ClienteResponse
from schemas.motorista_schema import MotoristaRequest, MotoristaResponse
from schemas.veiculo_schema import VeiculoRequest, VeiculoResponse
from dependencies.db import get_db

app = FastAPI()

# Rotas Cliente
@app.post("/api/clientes", response_model=ClienteResponse, status_code=status.HTTP_201_CREATED)
def create_cliente(request: ClienteRequest, db: Session = Depends(get_db)):
    return create_cliente(request, db)

@app.get("/api/clientes", response_model=list[ClienteResponse])
def find_all_clientes(db: Session = Depends(get_db)):
    return get_all_clientes(db)

@app.get("/api/clientes/{id}", response_model=ClienteResponse)
def find_cliente_by_id(id: int, db: Session = Depends(get_db)):
    return get_cliente_by_id(id, db)

@app.delete("/api/clientes/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cliente_by_id(id: int, db: Session = Depends(get_db)):
    return delete_cliente_by_id(id, db)

@app.put("/api/clientes/{id}", response_model=ClienteResponse)
def update_cliente(id: int, request: ClienteRequest, db: Session = Depends(get_db)):
    return update_cliente(id, request, db)

# Rotas Motorista
@app.post("/api/motoristas", response_model=MotoristaResponse, status_code=status.HTTP_201_CREATED)
def create_motorista(request: MotoristaRequest, db: Session = Depends(get_db)):
    return create_motorista(request, db)

@app.get("/api/motoristas", response_model=list[MotoristaResponse])
def find_all_motoristas(db: Session = Depends(get_db)):
    return get_all_motoristas(db)

@app.get("/api/motoristas/{id}", response_model=MotoristaResponse)
def find_motorista_by_id(id: int, db: Session = Depends(get_db)):
    return get_motorista_by_id(id, db)

@app.delete("/api/motoristas/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_motorista_by_id(id: int, db: Session = Depends(get_db)):
    return delete_motorista_by_id(id, db)

@app.put("/api/motoristas/{id}", response_model=MotoristaResponse)
def update_motorista(id: int, request: MotoristaRequest, db: Session = Depends(get_db)):
    return update_motorista(id, request, db)

# Rotas Veiculo
@app.post("/api/veiculos", response_model=VeiculoResponse, status_code=status.HTTP_201_CREATED)
def create_veiculo(request: VeiculoRequest, db: Session = Depends(get_db)):
    return create_veiculo(request, db)

@app.get("/api/veiculos", response_model=list[VeiculoResponse])
def find_all_veiculos(db: Session = Depends(get_db)):
    return get_all_veiculos(db)

@app.get("/api/veiculos/{id}", response_model=VeiculoResponse)
def find_veiculo_by_id(id: int, db: Session = Depends(get_db)):
    return get_veiculo_by_id(id, db)

@app.delete("/api/veiculos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_veiculo_by_id(id: int, db: Session = Depends(get_db)):
    return delete_veiculo_by_id(id, db)

@app.put("/api/veiculos/{id}", response_model=VeiculoResponse)
def update_veiculo(id: int, request: VeiculoRequest, db: Session = Depends(get_db)):
    return update_veiculo(id, request, db)
