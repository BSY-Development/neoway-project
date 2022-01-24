# Sample University Scrap
É um serviço de coleta de dados e persistência em um banco de dados. O site utilizado foi o [Sample University](https://sample-university-site.herokuapp.com/approvals/1). Para este projeto foi utilizado Python3 e mySQL.

## :rocket: Começando
Este projeto utiliza algumas bibliotecas externas que são necessárias realizar o download. Instalaremos através do [pip3](https://pip.pypa.io/en/stable/getting-started/).

### :clipboard: Pré-requisitos
#### É necessário instalar as dependências do projeto:
Utilize o comando abaixo para instalar automaticamente as dependências.
```sh
pip3 install -r requirements.txt
```
#### Caso prefira instalar manualmente cada uma das dependências, utilize os comandos abaixo.

#### [Scrapy](https://pypi.org/project/Scrapy/) - Para realizar a raspagem de dados no site.
```sh
pip3 install Scrapy
```
#### [Mysql.Connector](https://pypi.org/project/mysql-connector-python/) - Para conectar ao banco de dados mySQL.
```sh
pip3 install mysql-connector-python
```
#### [Dotenv](https://pypi.org/project/python-dotenv/) - Para acessar váriaveis de ambiente de conteúdo sensível.
```sh
pip3 install python-dotenv
```

### :wrench: Instalação
1. Clone o Repositório.
  - `git clone git@github.com:BSY-Development/neoway-project.git`.
  - Entre na pasta que você acabou de clonar `cd neoway-project/`.
2. Crie um arquivo com o nome `.env` na raiz do projeto.
  - Adicione nele as informações de acesso ao seu banco seguindo o modelo abaixo.
  ```sh
  MYSQL_USER=root
  MYSQL_HOST=localhost
  MYSQL_PASSWORD=yourpassword
  ```
### :gear: Rodando o código
Após instalar as dependências do projeto e criar o arquivo `.env`, você está pronto para rodar a aplicação. Por padrão, o código irá passar por todas as 4761 páginas, caso queira rodar um valor menor de páginas, vá até o arquivo `./universitysamples/spiders/university.py`. Altere o valor de `first_page` e `last_page` com o minimo de 1 e máximo de 4761. Para rodar, utilize o comando abaixo. Obs: Todas as páginas levam cerca de 20 minutos para finalizar.
```sh
scrapy crawl university
```

# Arquitetura



