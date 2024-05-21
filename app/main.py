from fastapi import FastAPI
from controllers.cliente_controller import *
from schemas.cliente_schema import ClienteRequest, ClienteResponse

app = FastAPI()

@app.post("/api/clientes", response_model=ClienteResponse, status_code=status.HTTP_201_CREATED)
def create(request: ClienteRequest, db: Session = Depends(get_db)):
    return create_cliente(request, db)

@app.get("/api/clientes", response_model=list[ClienteResponse])
def find_all(db: Session = Depends(get_db)):
    return get_all_clientes(db)

@app.get("/api/clientes/{id}", response_model=ClienteResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    return get_cliente_by_id(id, db)

@app.delete("/api/clientes/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    return delete_cliente_by_id(id, db)

@app.put("/api/clientes/{id}", response_model=ClienteResponse)
def update(id: int, request: ClienteRequest, db: Session = Depends(get_db)):
    return update_cliente(id, request, db)
