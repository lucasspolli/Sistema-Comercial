import sqlite3
import sys

connection = sqlite3.connect("../Database/database.db")
cursor = connection.cursor()

def createClientsTable():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            usuario varchar(1),
            email varchar(1), 
            senha varchar(1), 
            id varchar(1)
        )''')

def createRegistredProductsTable():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            nome varchar(1),
            preço varchar(1), 
            quantidade varchar(1), 
            id varchar(1)
        )''')