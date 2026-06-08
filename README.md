# MedAlerta 💊

Sistema de alertas para controle e acompanhamento de medicamentos, desenvolvido como projeto do **BootCamp I 2026 — UNINTER**.

---

## Sobre o projeto

O MedAlerta é um sistema que permite ao usuário cadastrar seus medicamentos e receber alertas nos horários corretos de consumo, registrando o histórico de uso e confirmação de cada dose.

A ideia original do projeto, seus requisitos e modelagem foram preservados e respeitados integralmente conforme proposto no BootCamp.

---

## Contexto de entrega

Não participei do BootCamp no dia da realização. Como as entregas em grupo já estavam encerradas, optei por desenvolver o projeto individualmente, fora do prazo, como exercício de aprendizado e portfólio.

Por decisão própria, utilizei uma stack diferente da adotada:

| Item | Stack original | Minha stack |
|---|---|---|
| Linguagem | Java | Python 3.12 |
| Framework | Spring Boot | FastAPI |
| Banco de dados | MySQL | PostgreSQL 16 |
| ORM | Hibernate | SQLAlchemy + Alembic |
| Ambiente | Docker + Docker Compose | Docker + Docker Compose |

---

## Aulas de referência do BootCamp

- [Aula 1](https://www.youtube.com/watch?v=j6-r_D-2hcE&t=3426s)
- [Aula 2](https://www.youtube.com/watch?v=YwC35D2c8AQ)
- [Aula 3](https://www.youtube.com/watch?v=GQfJ06IDeTw&t=8123s)

---

## Stack

- **Python 3.12**
- **FastAPI** — framework web para construção da API REST
- **PostgreSQL 16** — banco de dados relacional
- **SQLAlchemy** — ORM para mapeamento objeto-relacional
- **Alembic** — controle de migrations do banco de dados
- **Docker + Docker Compose** — containerização e orquestração do ambiente

---

## Funcionalidades

- Cadastro de usuários
- Cadastro de medicamentos
- Vinculação de medicamentos a usuários com definição de tratamento
- Geração automática de alertas com base na data de início, intervalo de horas e duração do tratamento
- Confirmação de consumo com registro automático de horário
- Histórico de uso por medicamento

---

## Modelo de dados

O sistema é composto por 5 entidades principais:

```
Usuario ──────────────┐
                      ├── UsuarioMedicamento (tratamento)
Medicamento ──────────┘         └── Alerta (doses geradas automaticamente)
                                      └── RegistroUso (confirmação de consumo)
```

---

## Como rodar

### Pré-requisitos
- Docker
- Docker Compose

### Subindo o ambiente

```bash
git clone https://github.com/Alvhel/MedAlerta.git
cd MedAlerta
docker compose up --build
```

### Aplicando as migrations

```bash
docker compose exec api bash
alembic upgrade head
```

### Acessando a API

- API: [http://localhost:8000](http://localhost:8000)
- Documentação Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Estrutura do projeto

```
MedAlerta/
├── app/
│   ├── main.py
│   ├── database.py
│   └── models/
│       ├── usuario.py
│       ├── medicamento.py
│       ├── usuario_medicamento.py
│       ├── alerta.py
│       └── registro_uso.py
├── alembic/
│   └── versions/
├── docs/
│   ├── MER - MedAlerta.png
│   └── MR - MedAlerta.png
├── .env
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## Autor

Desenvolvido por **Hélio**, projeto original de UNINTER, BootCamp I 2026.
