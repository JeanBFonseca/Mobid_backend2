from pydantic import BaseModel

class Veiculo(BaseModel):
    """
    Classe que representa um veículo.
    """
    motorista_id: int  # ID do motorista associado ao veículo
    placa: str  # Placa do veículo
    renavam: int  # Renavam do veículo
    chassis: str  # Chassis do veículo
    ano_fabricacao: int  # Ano de fabricação do veículo
    cor: str  # Cor do veículo
    modelo: str  # Modelo do veículo
    foto_veiculo: bytes  # Foto do veículo, armazenada como bytes
    veiculo_id: int = None  # ID do veículo (opcional, será preenchido posteriormente)

    class Config:
        """
        Configuração da classe Veiculo para permitir criar instâncias a partir de atributos.
        """
        from_attributes = True
