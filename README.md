# Sempre Seguro: Uma plataforma de Controle de Despesas Pessoais

# Sobre o Projeto

Sempre Seguro é uma aplicação web voltada para usuários que desejam uma plataforma fácil e prática para controlar suas despesas. [Visualize a aplicação aqui](https://sempreseguro-production.up.railway.app/sempreseguro/).

## Funcionalidades

* Informe todas as suas despesas e recebimentos, que serão analisados e após isso será gerado um relatório os detalhando e retornando o seu saldo final.
* Estes relatórios podem ser salvos para serem consultados posteriormente, também é possível excluí-los, caso o mesmo não seja mais proveitoso.
* Caso o usuário tenha interesse em determinado produto, o mesmo pode salvá-lo informando o nome do produto e seu valor, também pode ser informado o link do produto, para que o usuário ao clicar sobre o item gerado na lista de compras seja redirecionado a página responsável pelo mesmo.
* O usuário também pode armazenar suas contas em aberto, informando a descrição, valor e a data de vencimento. Assim o sistema irá enviar um e-mail para o usuário no dia do vencimento como lembrete.
  
OBS: Para utilizar dessas funcionalidades o usuário deverá estar logado a plataforma.

# Tecnologias

## Back-End
* Python
* Django

## Front-End
* HTML5 / CSS3
* JavaScript
* Bootstrap 5
* Tailwind CSS

## Banco de Dados
* PostgreSQL


## HomePage
![Homepage](https://github.com/DiogoMelloDM7/Sempre_Seguro/assets/136912625/f8320ead-c3cc-4995-be65-a612675e5a3f)


## Baixando e rodando a aplicação localmente

Para começar, siga estas etapas para baixar o código-fonte do projeto localmente:

1. Abra o terminal no seu computador.
2. Navegue até o diretório onde deseja armazenar o projeto.
3. Use o seguinte comando para clonar o repositório:

```bash
git clone https://github.com/DiogoMelloDM7/Sempre_Seguro.git
```

### Configurando ambiente

Antes de executar a aplicação localmente, você precisa configurar o ambiente. Siga estas etapas:

1. Abra o terminal e navegue até o diretório raiz do projeto.
2. Execute o seguinte comando para instalar as dependências do projeto:

```bash
pip install -r requirements.txt
```

### Executando a aplicação localmente

Após a configuração do ambiente, você pode iniciar a aplicação localmente. Siga estas etapas:

1. No terminal, navegue até o diretório raiz do projeto.
2. Execute o seguinte comando para aplicar migrações do banco de dados, se necessário:

```bash
python manage.py migrate
```

1. Inicie o servidor de desenvolvimento com o seguinte comando:

```bash
python manage.py runserver
```












