from pydantic import BaseModel
from datetime import date

class Motorista(BaseModel):
    """
    Classe que representa um motorista.
    """
    nome: str  # Nome do motorista
    cpf: str  # CPF do motorista
    email: str  # Email do motorista
    senha: str  # Senha do motorista
    rg: str  # RG do motorista
    chn: str  # CNH do motorista
    data_nascimento: date  # Data de nascimento do motorista
    sexo: str  # Sexo do motorista
    nome_mae: str  # Nome da mãe do motorista
    cep: str  # CEP do motorista
    telefone: str  # Telefone do motorista
    foto: bytes  # Foto do motorista, armazenada como bytes
    motorista_id: int = None  # ID do motorista (opcional, será preenchido posteriormente)

    class Config:
        """
        Configuração da classe Motorista para permitir criar instâncias a partir de atributos.
        """
        from_attributes = True
