from fastapi import FastAPI
from config.database import engine
from models import cliente_model, motorista_model, veiculo_model, agendamento_model, viagem_model
from controllers import cliente_controller, motorista_controller, veiculo_controller, agendamento_controller, viagem_controller

app = FastAPI()

# Cria as tabelas no banco de dados
cliente_model.Base.metadata.create_all(bind=engine)
motorista_model.Base.metadata.create_all(bind=engine)
veiculo_model.Base.metadata.create_all(bind=engine)
agendamento_model.Base.metadata.create_all(bind=engine)
viagem_model.Base.metadata.create_all(bind=engine)

# Inclui os routers dos controladores
app.include_router(cliente_controller.router)
app.include_router(motorista_controller.router)
app.include_router(veiculo_controller.router)
app.include_router(agendamento_controller.router)
app.include_router(viagem_controller.router)
