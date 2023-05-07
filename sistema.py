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
                        usuario varchar(1),
                        email varchar(1), 
                        senha varchar(1), 
                        id varchar(1))''')
# TABELA PRODUTOS
def create_registred_products_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                        nome varchar(1),
                        preço varchar(1), 
                        quantidade varchar(1), 
                        id varchar(1))''')
# CRIAR A TABELA CLIENTES E PRODUTOS
create_clients_table(), create_registred_products_table()
# MENU INICIAL COM ESCOLHA DO USUÁRIO ==============================================================================
def menu_inicial():
    logged = False
    id = 0
    while logged == False:
        sleep(0.5)
        botaoFinal = Menu_inicial()
        if botaoFinal == 1:
            sleep(1)
            logged, id = Register()
        elif botaoFinal == 2:
            sleep(1)
            logged = Login()
        elif botaoFinal == 3:
            connection.close()
            break
        else:
            sleep(1)
            print(f"\033[0;31mOpção inválida!\033[m")
            sleep(1)
    return logged, id
logged, id = menu_inicial()
# MENU FINAL COM ESCOLHA DO USUÁRIO =================================================================================
def menu_final(id):
    logged = True
    while logged == True:
        sleep(0.5)
        botaoFinal = Menu_final()
        if botaoFinal == 1:
            sleep(0.5)
            Registred_products()
        elif botaoFinal == 2:
            sleep(0.5)
            Register_products()
        elif botaoFinal == 3:
            sleep(0.5)
            Buy_product(id)
        elif botaoFinal == 4:
            sleep(0.5)
            Pay_cart(id)
        elif botaoFinal == 5:
            logged = menu_inicial()
            if logged == True:
                continue
            else:
                break
        else:
            sleep(1)
            print(f"\033[0;31mOpção inválida!\033[m")
            sleep(1)
menu_final(id)
# FINALIZAÇÃO DO SISTEMA ===========================================================================================
sleep(0.5)
print("="*66)
sleep(0.5)
print("\033[0;32mObrigado por usar o nosso sistema! Volte sempre!\033[m")