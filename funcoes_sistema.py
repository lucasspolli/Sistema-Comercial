# IMPORTAÇÕES PARA O SISTEMA FUNCIONAR
import sqlite3
import os
from time import sleep
# CONECTAR AO BANCO DE DADOS
connection = sqlite3.connect('banco_de_dados.db')
cursor = connection.cursor()
# INÍCIO
sistema = "S I S T E M A"
comercial = "C O M E R C I A L"

def inicio():
    print("\n" * os.get_terminal_size().lines)
    sleep(1)
    print("="*66)
    print(f"\033[0;34m{sistema:^66}\033[m")
    print(f"\033[0;34m{comercial:^66}\033[m")
    print("="*66)
# MENU INICIAL
def Menu_inicial():
    print("="*66)
    sleep(0.7)
    print("\033[0;33m1\033[m - Registrar uma conta")
    sleep(0.4)
    print("\033[0;33m2\033[m - Logar em uma conta")
    sleep(0.4)
    print("\033[0;33m3\033[m - Sair do menu")
    sleep(0.4)
    while True:
        try:
            opcao = int(input("\033[0;33mEscolha uma das opções acima para continuar: \033[m"))
            break
        except ValueError:
            sleep(1)
            print(f"\033[0;31mDigite um número!\033[m")
    return opcao
# REGISTRAR CONTA ==================================================================================================
def Register():
    inicio()
    # CONFIRMAÇÃO DO NOME DO USUÁRIO
    username_confirmation = False
    while username_confirmation == False:
        sleep(1)
        username = str(input("\033[0;33mDigite seu nome de usuário: \033[m"))
        cursor.execute(f"SELECT * FROM clientes WHERE usuario = '{username}'")
        resultado = cursor.fetchall()
        if resultado != []:
            sleep(1.2)
            print("\033[0;31mEsse usuário já existe!\033[m")
            username_confirmation = False
        else:
            username_confirmation = True
    # CONFIRMAÇÃO DO EMAIL
    email_confirmation = False
    while email_confirmation == False:
        sleep(1)
        email = str(input("\033[0;33mDigite seu email: \033[m"))
        cursor.execute(f"SELECT * FROM clientes WHERE email = '{email}'")
        resultado = cursor.fetchall()
        if resultado != []:
            sleep(1.2)
            print("\033[0;31mEsse email já foi cadastrado!\033[m")
            email_confirmation = False
        else:
            email_confirmation = True
    # CONFIRMAÇÃO DA SENHA
    password_confirmation = False
    while password_confirmation == False:
        sleep(1)
        password = str(input("\033[0;33mDigite sua senha: \033[m"))
        sleep(1)
        password_confirm = str(input("\033[0;33mConfirme a sua senha: \033[m"))
        cursor.execute("SELECT * from clientes")
        resultado = cursor.fetchall()
        # DEFINIR O ID DO USUÁRIO
        if resultado == []:
            id = 0
        else:
            id = 0
            for users in resultado:
                id = id + 1
        # AS SENHAS ESTÃO INCORRETAS
        if password != password_confirm:
            sleep(1.2)
            print("\033[0;31mAs senhas não se coincidem!\033[m")
            password_confirmation = False
        # ADICIONAR O USUÁRIO AO BANCO DE DADOS
        else:
            comand = f"INSERT INTO clientes (usuario, email, senha, id) VALUES('{username}', '{email}', '{password}', '{id}')"
            cursor.execute(comand)
            connection.commit()
            user = cursor.execute(f"SELECT * FROM clientes WHERE usuario = '{username}' OR email = '{email}'")
            user = user.fetchall()
            sleep(1.5)
            print(f"\033[0;32mSeja bem-vindo, {user[0][0]}!\033[m")
            password_confirmation = True
            sleep(2)
            logged = True
    return logged
# LOGAR NA CONTA ===================================================================================================
def Login():
    inicio()
    # VERIFICAR SE EXISTE O NOME DE USUÁRIO OU EMAIL
    username_or_email_exists = False
    while username_or_email_exists == False:
        sleep(1)
        username_or_email = str(input("\033[0;33mDigite seu nome de usuário ou email: \033[m"))
        user = cursor.execute(f"SELECT * FROM clientes WHERE usuario = '{username_or_email}' OR email = '{username_or_email}'")
        user = user.fetchall()
        # USUÁRIO OU EMAIL NÃO EXISTE
        if user == []:
            sleep(1)
            print("\033[0;31mEste usuário ou email não existe!\033[m")
            username_or_email_exists = False
        # CONFIRMAÇÃO DA SENHA
        else:
            password_confirmation = False
            while password_confirmation == False:
                sleep(1)
                password = str(input("\033[0;33mDigite sua senha: \033[m"))
                user_password = user[0][2]
                # AS SENHAS ESTÃO INCORRETAR
                if password != user_password:
                    sleep(1)
                    print("\033[0;31mA senha está incorreta!\033[m")
                    password_confirmation = False
                # USUÁRIO ESTÁ LOGADO
                else:
                    sleep(1.5)
                    print(f"\033[0;32mSeja bem-vindo, {user[0][0]}!\033[m")
                    sleep(2)
                    password_confirmation = True
                    username_or_email_exists = True
                    logged = True
                    break
    return logged
# MENU FINAL =======================================================================================================
def Menu_final():
    inicio()
    sleep(0.7)
    print("1 - Ver produtos cadastrados")
    sleep(0.4)
    print("2 - Cadastrar produtos")
    sleep(0.4)
    print("3 - Sair do menu")
    sleep(0.4)
    while True:
        try:
            opcao = int(input("\033[0;33mEscolha uma das opções acima para continuar: \033[m"))
            break
        except ValueError:
            sleep(1)
            print(f"\033[0;31mDigite um número!\033[m")
    return opcao
# CADASTRAR PRODUTOS ===============================================================================================
def Register_products():
    inicio()
    print("\033[0;33mVamos cadastrar seu produto!\033[m")
    sleep(1)
    # VERIFICAR O NOME DO PRODUTO
    product_confirmation = False
    while product_confirmation == False:
        product_name = str(input("\033[0;33mDigite o nome do seu produto: \033[m"))
        product = cursor.execute(f"SELECT * FROM produtos WHERE nome = '{product_name}'")
        product = product.fetchall()
        # REGISTRAR O PREÇO DO PRODUTO
        if product == []:
            product_price = str(input("\033[0;33mDigite o preço do seu produto: \033[m"))
            sleep(1)
            # VERIFICAR O ID DO PRODUTO
            id_confirmation = False
            while id_confirmation == False:
                product_id = str(input("\033[0;33mDigite o id do seu produto (de 0 à 999): \033[m"))
                product = cursor.execute(f"SELECT * FROM produtos WHERE id = '{product_id}'")
                product = product.fetchall()
                # REGISTRAR A QUANTIDADE DO PRODUTO EM ESTOQUE
                if product == []:
                    product_quantify = str(input("\033[0;33mDigite a quantidade do seu produto que tem em estoque: \033[m"))
                    # ADICIONAR O PRODUTO À TABELA PRODUTOS NO BANCO DE DADOS
                    comand = f"INSERT INTO produtos (nome, preço, quantidade, id) VALUES('{product_name}', '{product_price}', '{product_quantify}', '{product_id}')"
                    cursor.execute(comand)
                    connection.commit()
                    sleep(1)
                    # FINALIZAÇÃO DA FUNÇÃO
                    print("\033[0;32mSeu produto foi adicionado ao sistema!\033[m")
                    id_confirmation = True
                    product_confirmation = True
                    sleep(1)
                    break
                # JÁ EXISTE UM PRODUTO COM O ID DIGITADO
                elif product_id == product[0][3]:
                    sleep(1)
                    print("\033[0;31mEste id já existe!\033[m")
                    id_confirmation = False
        # JÁ EXISTE UM PRODUTO COM O NOME DIGITADO
        elif product_name == product[0][0]:
            sleep(1)
            print("\033[0;31mEste nome de produto já existe!\033[m")
            product_confirmation = False
# PRODUTOS CADASTRADOS =============================================================================================
def Registred_products():
    inicio()
    sleep(0.5)
    # LISTA DOS PRODUTOS CADASTRADOS NO BANCO DE DADOS
    print("\033[0;32mAqui está a lista dos produtos cadastrados:\033[m")
    nome = "Nome"
    preço = "Preço"
    quantidade = "Quantidade"
    id = "Id"
    sleep(1)
    print(f"\033[0;33m{nome:<14}{preço:<10}{quantidade:<15}{id}\033[m")
    # SELECIONAR OS PRODUTOS NO BANCO DE DADOS
    product = cursor.execute(f"SELECT * FROM produtos")
    product = product.fetchall()
    # MOSTRAR AS INFORMAÇÕES DE TODOS OS PRODUTOS REGISTRADOS
    for products in product:
        name = products[0]
        price = float(products[1])
        quantify = products[2]
        id = products[3]
        sleep(1)
        print(f"{name:<12}R${price:<13.2f}{quantify:<12}{id}")
    answer = False
    while answer == False:
        sleep(1)
        answer = str(input("\033[0;33mVocê deseja voltar ao menu (s/n)? \033[m"))
        if answer not in "sn":
            sleep(1)
            print("\033[0;31mDigite somente s/n!\033[m")
            answer = False
        elif answer == "n":
            sleep(1)
            print("\033[0;32mTudo bem!\033[m")
            answer = False
        else:
            sleep(1)
            print("\033[0;32mTe redirecionando para o menu!\033[m")
            answer = True
            sleep(1)