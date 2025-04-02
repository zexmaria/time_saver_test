# Projeto Agenda Online
### TESTE PARA A EMPRESA  TIME SAVER | CRUD FEITO EM FLASK

## 💻 Sobre o Projeto
***

Este é um projeto feito com Python, Flask e Bootstrap. O projeto é um teste da empresa Time Saver onde precisei criar uma página para registrar agendamentos de atividades (CRUD) e buscar por filtros (nome, serviço e data).
Aqui você encontra um passo a passo para **clonar**, **instalar** e **rodar** o projeto no seu computador.
## Observações iniciais:
* O site foi desenvolvido baseado na versão **<u>Desktop</u>** e para rodar perfeitamente apenas nesta resolução(1024px). Não é garantido que funcionará bem em resolução diferente (tablet ou mobile).

* Esta aplicação foi constrída para funcionar de forma dinâmica onde o banco de dados precisará ser populado para que seja apresentado de forma correta.
* Foi construído um *Script* para popular o banco automaticamente.

* O tutorial a seguir foi pensado para sistemas Linux, não testado para Windows ou macOS.

***
## Pré-requisitos
***

* Python 3.12+
* Flask 2.2.1
* SQLAlchemy 2.0.40
* PIP
* Venv
* Git


***

## 🛠️  Instalações necessárias:

### 🐍Python 3.12 ou superior
1. Verifique se o Python está instalado.
Em todos os Linux Debian Based, já temos o python3 instalado nativamente.
2. No terminal execute o comando abaixo:

``` python --version```

Se aparecer Python 3.12 ou maior, você já tem! Se não, baixe o python para seu sistema:

3. Baixe e instale o Python 3.12:

https://www.python.org/downloads/release/python-3120/

4. Verifique se o PIP está instalado:

``` pip --version```

Se não estiver instalado, siga os passos abaixo para baixar e instalar:

https://pypi.org/project/pip/


### 🧩Git

1. Verifique se o Git está instalado.

No terminal digite: 

````git --version````

* Caso não apareça nenhuma versão instalada, digite:

````sudo apt install git -y````


***
## 🛠️ Instalando Aplicação Localmente

### 1. Clone o repositório
No terminal, clone o repositório usando um dos métodos abaixo:

Clone com HTTPS:

````https://github.com/zexmaria/time_saver_test.git````

Clone com SSH:

````git@github.com:zexmaria/time_saver_test.git````

### 2. Acesse a Pasta do Projeto
Navegue até a pasta do projeto:

````cd time_saver_test````

### 3. Crie um ambiente virtual com VENV
Instale um ambente virtual com  o nome de sua preferência. Como exemplo estarei usando o nome ".meuvenv"

````python3 -m venv .meuvenv````

Ative o ambiente virtual:

````source .meuvenv/bin/activate````


### 4. Instale as dependências
Com ambiente virtual ativo, instale as dependências do projeto com o comando abaixo:

````pip install -r requirements.txt````

***
## ⚙️Rodando o Projeto Localmente

1. Popule o banco de dados com agendamentos fictícios executando o comando:

````python popular_banco.py````

OBS: Você poderá adicionar outros agendamentos manualmente com a página rodando.

2. Inicie o servidor local:

```python run.py```

3. Acesse seu localhost pelo browser pelo endereço informado no terminal:

ex: http://127.0.0.1:5000/

***



