from sqlalchemy.orm import Session
from app import models, schemas

def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = models.Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente) 
    return db_cliente

def get_clientes(db: Session):
    return db.query(models.Cliente).all()

def get_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

def delete_cliente(db: Session, cliente_id: int):
    cliente = get_cliente(db, cliente_id)
    if cliente:
        db.delete(cliente)
        db.commit()
    return cliente

def update_cliente(db: Session, cliente_id: int, cliente: schemas.ClienteCreate):
    # Busca o cliente pelo ID
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if not db_cliente:
        return None
    
    # Atualiza os dados do cliente
    db_cliente.nome = cliente.nome
    db_cliente.telefone = cliente.telefone
    db_cliente.cpf = cliente.cpf
    db_cliente.placa_carro = cliente.placa_carro

    db.commit()
    db.refresh(db_cliente)
    return db_cliente
