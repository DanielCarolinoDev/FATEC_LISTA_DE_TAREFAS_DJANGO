# FATEC_LISTA_DE_TAREFAS_DJANGO

## Descrição
Este projeto foi desenvolvido como parte do Projeto Integrador da FATEC, utilizando o framework Django (Python).
A aplicação consiste em um sistema de Lista de Tarefas (To-Do List) com funcionalidades completas de CRUD, além de autenticação de usuários (login/logout).

## Objetivo
Desenvolver uma aplicação web completa utilizando Django, aplicando conceitos de:
- Arquitetura MVC (MTV no Django)
- Autenticação de usuários
- CRUD com banco de dados
- Organização de projeto backend

## Funcionalidades
- Cadastro de tarefas
- Listagem de tarefas
- Edição de tarefas
- Exclusão de tarefas
- Sistema de login e logout
- Área administrativa do Django

## Tecnologias Utilizadas
- Python
- Django
- SQLite
- HTML / CSS
- Bootstrap (opcional)

## Acesso Administrativo
Usuário: administrador
Senha: administrador

(Recomenda-se alterar em produção)

## Estrutura do Projeto
/projeto
│── manage.py
│── db.sqlite3
├── app/
│   │── models.py
│   │── views.py
│   │── urls.py
│   │── forms.py
│   │── templates/
│   │── static/
├── projeto/
│   │── settings.py
│   │── urls.py
│   │── wsgi.py

## Como Executar
1. Clone o repositório
2. cd PYTHON-DJANGO_FATEC_Projeto_integrador_Lista-de-tarefas
3. python -m venv venv
4. Ative o ambiente virtual
5. pip install django
6. python manage.py migrate
7. python manage.py runserver
8. Acesse: http://127.0.0.1:8000/

## Segurança
- Autenticação nativa do Django
- Proteção CSRF
- ORM evita SQL Injection

## Conceitos Aplicados
- CRUD completo
- Django ORM
- Templates e rotas
- Autenticação

## Autor
Daniel Carolino
Estudante de Desenvolvimento de Software Multiplataforma – FATEC
