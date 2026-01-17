from pydantic import BaseModel

class ClienteCreate(BaseModel):
    nome: str
    telefone: str
    cpf: str
    placa_carro: str

class ClienteResponse(ClienteCreate):
    id: int

    class Config:
        from_attributes = True
