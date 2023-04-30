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

create_table()

inicio()
sleep(0.5)
print("\033[0;32mSeja bem vindo(a) ao maior sistema comercial da América Latina!\033[m")
logged = False
while logged == False:
    sleep(0.5)
    opcao = menu()
    if opcao == 1:
        sleep(0.5)
        logged = Register()
    elif opcao == 2:
        sleep(0.5)
        logged = Login()
    elif opcao == 3:
        connection.close()
        break
    else:
        sleep(1)
        print(f"\033[0;31mOpção inválida!\033[m")
sleep(0.5)
print("="*66)
sleep(0.5)
print("\033[0;32mObrigado por usar o nosso sistema! Volte sempre!\033[m")