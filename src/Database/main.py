import sqlite3

connection = sqlite3.connect("../Database/database.db")
cursor = connection.cursor()

def createTables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id          INTEGER PRIMARY KEY,
            username    VARCHAR(30) NOT NULL UNIQUE,
            email       VARCHAR(50) NOT NULL UNIQUE,
            password    VARCHAR(30)
        )''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id          INTEGER PRIMARY KEY,
            name        VARCHAR(50) NOT NULL UNIQUE,
            price       REAL NOT NULL,
            quantify    INTEGER NOT NULL
        )''')
