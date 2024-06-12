from pydantic import BaseModel
from datetime import date

class Cliente(BaseModel):
    """
    Classe que representa um cliente.
    """
    nome: str  # Nome do cliente
    cpf: str  # CPF do cliente
    email: str  # Email do cliente
    senha: str  # Senha do cliente
    cep: str  # CEP do cliente
    telefone: str  # Telefone do cliente
    dt_nascimento: date  # Data de nascimento do cliente
    sexo: str  # Sexo do cliente
    cliente_id: int = None  # ID do cliente (opcional, será preenchido posteriormente)

    class Config:
        """
        Configuração da classe Cliente para permitir criar instâncias a partir de atributos.
        """
        from_attributes = True

