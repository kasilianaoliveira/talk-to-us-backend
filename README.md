# Projeto Tickets

Este é um projeto que utiliza FastAPI, SQLAlchemy e outras tecnologias para gerenciar tickets. O projeto utiliza o Poetry para gerenciamento de dependências e ambientes virtuais.

## Tecnologias Utilizadas

- **FastAPI**: Framework web para construir APIs rápidas e robustas.
- **SQLAlchemy**: ORM para interagir com o banco de dados.
- **psycopg2-binary**: Adaptador PostgreSQL para Python.
- **Alembic**: Biblioteca para migração de banco de dados.
- **Python-decouple**: Biblioteca para gerenciar variáveis de ambiente.

## Dependências

As principais dependências do projeto são:

- Dependências principais:

  - astapi[standard]: Versão >=0.115.11,<0.116.0
  - sqlalchemy: Versão >=2.0.39,<3.0.0
  - psycopg2-binary: Versão >=2.9.10,<3.0.0
  - alembic: Versão >=1.15.1,<2.0.0
  - python-decouple: Versão >=3.8,<4.0

- Dependências de desenvolvimento:
  - pytest: Framework para testes. Versão ^8.3.5
  - pytest-cov: Para cobertura de testes. Versão ^6.0.0
  - taskipy: Para automação de tarefas. Versão ^1.14.1
  - ruff: Linter para código Python. Versão ^0.11.0
  - httpx: Para testes com HTTP. Versão ^0.28.1

### Pré-requisitos

- [Poetry](https://python-poetry.org/) instalado.
- Python 3.9 ou superior.

### Passos para instalar e configurar o ambiente

1. Clone o repositório:

   ```bash
   git clone https://github.com/kasilianaoliveira/talk-to-us-backend.git
   cd projeto-tickets
   ```

2. Instale as dependências do projeto:  
   Se você ainda não tem o Poetry instalado, siga a documentação oficial para instalação. Uma vez com o Poetry instalado, execute o comando:

   ```bash
   poetry install
   ```

3. Para rodar o projeto, ative o ambiente virtual do Poetry:
   ```bash
   poetry shell
   ```

## Rodando o projeto

Para iniciar o servidor da aplicação, use o comando:

```bash
task run
```

Isso iniciará o servidor FastAPI, e você poderá acessar a aplicação no http://localhost:5000.

## Testes

O projeto utiliza pytest para realizar os testes. Para rodar os testes, use o comando:

```bash
task test
```

```bash
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin1245
POSTGRES_DB=main

PGADMIN_DEFAULT_EMAIL=admin@gmail.com
PGADMIN_DEFAULT_PASSWORD=admin1245
```

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```bash
projeto-tickets/
│
├── src/
│ └── __init__.py
│ └── app.py
│ └── tests/
│
├── pyproject.toml
├── README.md
└── test_app.py
```

## Variaveis de ambientes
