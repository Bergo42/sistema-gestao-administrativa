# Sistema de Gestão Administrativa

## 1. Apresentação

O Sistema de Gestão Administrativa é uma aplicação web desenvolvida como parte do projeto acadêmico da disciplina Projeto de Software. A solução foi concebida para a empresa fictícia Organiza Serviços Administrativos, com o objetivo de facilitar o gerenciamento de clientes e solicitações de serviços.

## 2. Objetivo

Desenvolver uma aplicação web responsiva que permita organizar informações de clientes, registrar solicitações de serviços e acompanhar seus respectivos prazos e status.

## 3. Funcionalidades

- Cadastro e consulta de clientes.
- Armazenamento de nome, telefone e e-mail dos clientes.
- Cadastro de solicitações vinculadas aos clientes.
- Registro da descrição e do prazo de cada solicitação.
- Acompanhamento do status das solicitações: pendente, em andamento e concluída.

## 4. Tecnologias utilizadas

- Python 3.14
- Django 5.2 LTS
- SQLite
- HTML5
- CSS3
- Bootstrap 5.3
- Git e GitHub

## 5. Arquitetura

O sistema utiliza a arquitetura monolítica em camadas, seguindo o padrão MVT (Model-View-Template) do Django.

A aplicação está organizada em dois módulos principais:

- **clientes:** responsável pelo cadastro e consulta de clientes.
- **solicitacoes:** responsável pelo gerenciamento das solicitações de serviços.

## 6. Estrutura do projeto

- `config/`: configurações gerais do projeto Django.
- `clientes/`: funcionalidades relacionadas aos clientes.
- `solicitacoes/`: funcionalidades relacionadas às solicitações.
- `manage.py`: ferramenta de gerenciamento do Django.
- `db.sqlite3`: banco de dados local, não versionado no Git.

## 7. Instalação e execução

### Pré-requisitos

- Python instalado.
- Git instalado.

### Clonar o repositório

```bash
git clone https://github.com/Bergo42/sistema-gestao-administrativa.git
cd sistema-gestao-administrativa