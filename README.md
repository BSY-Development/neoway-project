# Sample University Scrap
É um serviço de coleta de dados e persistência em um banco de dados. O site utilizado foi o [Sample University](https://sample-university-site.herokuapp.com/approvals/1). A página mostra dados fictícios de pessoas onde cada pessoa possui cpf, nome e pontuação (score), cada página possui cerca de 10 pessoas, tendo um total de 4671 páginas. Para este projeto foi utilizado Python3 e MySQL.

## :rocket: Começando
Este projeto utiliza algumas bibliotecas externas que são necessárias para que o projeto funcione corretamente. Instalaremos através do [pip3](https://pip.pypa.io/en/stable/getting-started/).

## :clipboard: Pré-requisitos
#### O projeto depende da instalação de alguns pacotes para funcionar corretamente. Caso não os possua instalado, estarei disponibilizando o comando para a instalação de cada um em [Instalação](#wrench-instala%C3%A7%C3%A3o). Abaixo estão os pacotes utilizados no projeto.


- [Scrapy](https://pypi.org/project/Scrapy/) - Para realizar a raspagem de dados no site.
- [Mysql.Connector](https://pypi.org/project/mysql-connector-python/) - Para conectar ao banco de dados mySQL.
- [Dotenv](https://pypi.org/project/python-dotenv/) - Para acessar variáveis de ambiente de conteúdo sensível.


## :wrench: Instalação
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
3. Instale as dependências (se houver).
- `Scrapy`
```sh
pip3 install Scrapy
```
- `Mysql-connector-python`
```sh
pip3 install mysql-connector-python
```
- `python-dotenv`
```sh
pip3 install python-dotenv
```
## :gear: Rodando o código
Após instalar as dependências do projeto e criar o arquivo `.env`, você está pronto para rodar a aplicação. Por padrão, o código irá passar por todas as 4761 páginas, caso queira rodar um valor menor de páginas, vá até o arquivo localizado em `./universitysamples/spiders/university.py`. Altere o valor de `first_page` (mínimo de 1) e `last_page` (máximo de 4761). Ao rodar será criado e armazenado os dados obtidos em um banco de dados mySQL, dentro de 2 tabelas, onde a tabela Users ficam os usuários que possuem dados válidos, e na tabela Rejected ficam os usuários que não possuem um CPF válido. Para rodar o código, utilize o comando abaixo. 
```sh
scrapy crawl university
```
_`OBS: Quanto maior o número páginas, maior será o tempo para finalizar, todas as páginas levam cerca de 20 minutos para finalizar.`_

## :gear: Fluxo de funcionamento
Ao utilizar o comando `scrapy crawl university`, o sistema irá acessar uma list predefinida (utilizando generator) de todos os links a serem acessados durante a execução, e ao entrar na página o software irá buscar pelos elementos que combinem com o seletor indicado durante a configuração. E trazer seu nome, cpf e pontuação (score), com os dados obtidos, o software submete-os a uma higienização de dados, mantendo apenas as informações necessárias e padronizadas para todas as pessoas, sendo então armazenadas no banco, em sua respectiva tabela, e caso não possua um cpf válido, os dados da pessoa serão armazenados em uma diferente tabela para manter uma organização caso a informação se torne pertinente em algum momento para com o usuário. O sistema repete o fluxo até que seja finalizado o processo.

#### Por [Bruno Yamamoto](https://www.brunoy.dev/)
