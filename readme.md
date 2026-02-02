# API de Controle de Clientes e Placas

O sistema realiza o controle de clientes e suas respectivas placas de veículos,
utilizando FastAPI e PostgreSQL, com ambiente configurado via Docker.

---

## Tecnologias Utilizadas

- Python 3
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose
- Swagger (OpenAPI)

---

## Estrutura do Projeto

app/
- main.py
- crud.py
- models.py
- schemas.py
- database.py

Dockerfile  
docker-compose.yml  
requirements.txt  

---

##  Como Executar o Projeto

1. Clone o repositório:
```bash
git clone <URL_DO_REPOSITORIO>
```

2. Acesse a pasta do projeto:
```bash
cd Teste-Tecnico
```

3. Suba o ambiente com Docker:
```bash
docker compose up --build
```

---

## 🔗 Endpoints Disponíveis

- POST `/clientes/`
- GET `/clientes/`
- GET `/clientes/{cliente_id}`
- PUT `/clientes/{cliente_id}`
- DELETE `/clientes/{cliente_id}`
- GET `/consulta/final-placa/{numero}`

---

## Testes

Todos os endpoints foram testados manualmente utilizando o Swagger,
com dados reais, garantindo o correto funcionamento da API.

---

##  Documentação Adicional

O repositório contém uma documentação em PDF com prints do funcionamento
e testes realizados na aplicação.
