from time import sleep
from funcoes_sistema import *
import sqlite3

connection = sqlite3.connect('banco_de_dados.db')
cursor = connection.cursor()

def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                        usuario varchar(20),
                        email varchar(20), 
                        senha varchar(20), 
                        id varchar(4))''')
    #preço varchar(8), quantidade varchar(20), pago text

create_table()

inicio()
sleep(0.5)
print("\033[0;33mSeja bem vindo(a) ao maior sistema comercial da América Latina!\033[m")
key = True
valor_pago = 0
logged = False
while logged == False:
    sleep(0.5)
    opcao = menu()
    if opcao == 1:
        sleep(0.5)
        logged = Register()
    elif opcao == 2:
        sleep(1)
        remover_produto()
    elif opcao == 3:
        connection.close()
        break
    else:
        sleep(1)
        print(f"\033[0;31mOpção inválida!\033[m")
sleep(1)
print("="*57)
sleep(0.5)
print("\033[0;32mObrigado por usar o nosso sistema! Volte sempre!\033[m")