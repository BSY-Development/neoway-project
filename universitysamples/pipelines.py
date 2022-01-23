# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
from itemadapter import ItemAdapter
import mysql.connector
from dotenv import load_dotenv, find_dotenv

# Aqui é feito a chamada ao arquivo .env para utilizar valores de 
# conteúdo sensiveis.
load_dotenv(find_dotenv())

class UniversitysamplesPipeline:
    # Inicializa o banco
    def __init__(self):
        self.con = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
        )
        self.cur = self.con.cursor()
        # Cria o banco se não existir
        self.create_database()
        # Cria a tabela Users se não existir
        self.create_table()

    def create_database(self):
        self.cur.execute("CREATE SCHEMA IF NOT EXISTS University")

    # Cria a tabela Users para armazenar os usuarios, e a tabela Rejected para guardar as pessoas 
    # com o cpf inválido, caso seja necessário para entrar em contato com a pessoa para atualizar os dados.
    def create_table(self):
        self.cur.execute("USE University")
        self.cur.execute("CREATE TABLE IF NOT EXISTS Users (name VARCHAR(100), cpf VARCHAR(11), score FLOAT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS Rejected (name VARCHAR(100), cpf VARCHAR(11), score FLOAT)")

    def process_item(self, item, spider):
        # Caso o cpf seja valido insere em Users e invalido insere em Rejected
        if item['valid_cpf']:
            self.cur.execute("INSERT INTO Users VALUES (%s, %s, %s)", (item['name'], item['cpf'], item['score']))
        else:
            self.cur.execute("INSERT INTO Rejected VALUES (%s, %s, %s)", (item['name'], item['cpf'], item['score']))
        self.con.commit()
        return item
