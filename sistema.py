# IMPORTAÇÕES PARA O SISTEMA FUNCIONAR
import sqlite3
from time import sleep
from funcoes_sistema import *
# CONECTAR AO BANCO DE DADOS
connection = sqlite3.connect('banco_de_dados.db')
cursor = connection.cursor()
# TABELA CLIENTES
def create_clients_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                        usuario varchar(20),
                        email varchar(20), 
                        senha varchar(20), 
                        id varchar(4))''')
# TABELA PRODUTOS
def create_registred_products_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                        nome varchar(20),
                        preço varchar(20), 
                        quantidade varchar(20), 
                        id varchar(4))''')
# CRIAR A TABELA CLIENTES E PRODUTOS
create_clients_table(), create_registred_products_table()
# MENU INICIAL COM ESCOLHA DO USUÁRIO ==============================================================================
def menu_inicial():
    logged = False
    while logged == False:
        sleep(0.5)
        botao_final = Menu_inicial()
        if botao_final == 1:
            sleep(1)
            logged = Register()
        elif botao_final == 2:
            sleep(1)
            logged = Login()
        elif botao_final == 3:
            connection.close()
            break
        else:
            sleep(1)
            print(f"\033[0;31mOpção inválida!\033[m")
    return logged
logged = menu_inicial()
# MENU FINAL COM ESCOLHA DO USUÁRIO ================================================================================
def menu_final():
    logged = True
    while logged == True:
        sleep(0.5)
        botao_final = Menu_final()
        if botao_final == 1:
            sleep(0.5)
            Registred_products()
        elif botao_final == 2:
            sleep(0.5)
            Register_products()
        elif botao_final == 3:
            logged = menu_inicial()
            if logged == True:
                continue
            else:
                break
        else:
            sleep(1)
            print(f"\033[0;31mOpção inválida!\033[m")
menu_final()
# FINALIZAÇÃO DO SISTEMA ===========================================================================================
sleep(0.5)
print("="*66)
sleep(0.5)
print("\033[0;32mObrigado por usar o nosso sistema! Volte sempre!\033[m")