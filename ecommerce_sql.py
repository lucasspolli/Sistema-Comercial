from time import sleep
from funcoes_ecommerce_sql import *
import sqlite3

connection = sqlite3.connect('ecommerce.db')
cursor = connection.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS dados (nome varchar(20), id varchar(4), preço varchar(8), quantidade varchar(20), pago text)')

create_table()

inicio()
sleep(1)
print("\033[0;33mSeja bem vindo(a) ao maior e-commerce da América Latina!\033[m")
sleep(1.5)
key = True
valor_pago = 0
while key == True:
    sleep(0.5)
    opcao = menu()
    if opcao == 1:
        sleep(1)
        adicionar_produto()
    elif opcao == 2:
        sleep(1)
        remover_produto()
    elif opcao == 3:
        sleep(1)
        valor_pago = consultar_carrinho(valor_pago)
    elif opcao == 4:
        sleep(1)
        connection.close()
        break
    else:
        sleep(1)
        print(f"\033[0;31mOpção inválida!\033[m")
sleep(1)
print("="*57)
sleep(0.5)
print("\033[0;33mObrigado por usar o nosso e-commerce! Volte sempre!\033[m")