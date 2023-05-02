# IMPORTAÇÕES PARA O SISTEMA FUNCIONAR
import sqlite3
import os
from time import sleep
# CONECTAR AO BANCO DE DADOS
connection = sqlite3.connect('banco_de_dados.db')
cursor = connection.cursor()
# INÍCIO
def inicio():
    print("\n" * os.get_terminal_size().lines)
    sleep(1)
    print("="*66)
    print(f"\033[0;34m{'S I S T E M A':^66}\033[m")
    print(f"\033[0;34m{'C O M E R C I A L':^66}\033[m")
    print("="*66)
# MENU INICIAL
def Menu_inicial():
    inicio()
    sleep(0.5)
    print("\033[0;32mSeja bem vindo(a) ao maior sistema comercial da América Latina!\033[m")
    sleep(0.5)
    print("="*66)
    sleep(0.2)
    print("\033[0;33m1\033[m - Registrar uma conta")
    sleep(0.2)
    print("\033[0;33m2\033[m - Logar em uma conta")
    sleep(0.2)
    print("\033[0;33m3\033[m - Sair do menu")
    sleep(0.2)
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
    sleep(0.5)
    print("\033[0;36mDigite 0 à qualquer momento para sair do cadastro!\033[m")
    while username_confirmation == False:
        username = str(input("\033[0;33mDigite seu nome de usuário: \033[m"))
        # VERIFICA SE O USUÁRIO QUER SAIR
        if username == "0":
            sleep(0.7)
            print("\033[0;32mRetornando ao menu!\033[m")
            sleep(0.7)
            username_confirmation = True
            logged = False
            break
        cursor.execute(f"SELECT * FROM clientes WHERE usuario = '{username}'")
        resultado = cursor.fetchall()
        if resultado != []:
            sleep(1.2)
            print("\033[0;31mEsse usuário já existe!\033[m")
            username_confirmation = False
        else:
            # CONFIRMAÇÃO DO EMAIL
            email_confirmation = False
            while email_confirmation == False:
                sleep(1)
                email = str(input("\033[0;33mDigite seu email: \033[m"))
                # VERIFICA SE O USUÁRIO QUER SAIR
                if email == "0":
                    sleep(0.7)
                    print("\033[0;32mRetornando ao menu!\033[m")
                    sleep(0.7)
                    username_confirmation = True
                    logged = False
                    break
                cursor.execute(f"SELECT * FROM clientes WHERE email = '{email}'")
                resultado = cursor.fetchall()
                if resultado != []:
                    sleep(1.2)
                    print("\033[0;31mEsse email já foi cadastrado!\033[m")
                    email_confirmation = False
                else:
                    # CONFIRMAÇÃO DA SENHA
                    password_confirmation = False
                    while password_confirmation == False:
                        sleep(1)
                        password = str(input("\033[0;33mDigite sua senha: \033[m"))
                        # VERIFICA SE O USUÁRIO QUER SAIR
                        if password == "0":
                            sleep(0.7)
                            print("\033[0;32mRetornando ao menu!\033[m")
                            sleep(0.7)
                            email_confirmation = True
                            username_confirmation = True
                            logged = False
                            break
                        sleep(1)
                        password_confirm = str(input("\033[0;33mConfirme a sua senha: \033[m"))
                        # VERIFICA SE O USUÁRIO QUER SAIR
                        if password_confirm == "0":
                            sleep(0.7)
                            print("\033[0;32mRetornando ao menu!\033[m")
                            sleep(0.7)
                            email_confirmation = True
                            username_confirmation = True
                            logged = False
                            break
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
                            email_confirmation = True
                            username_confirmation = True
                            logged = True
                            sleep(1)
    return logged
# LOGAR NA CONTA ===================================================================================================
def Login():
    inicio()
    # VERIFICAR SE EXISTE O NOME DE USUÁRIO OU EMAIL
    sleep(1)
    print("\033[0;36mDigite 0 à qualquer momento para sair do login!\033[m")
    username_or_email_exists = False
    while username_or_email_exists == False:
        username_or_email = str(input("\033[0;33mDigite seu nome de usuário ou email: \033[m"))
        # VERIFICA SE O USUÁRIO QUER SAIR
        if username_or_email == "0":
            sleep(0.7)
            print("\033[0;32mRetornando ao menu!\033[m")
            sleep(0.7)
            username_or_email_exists = True
            logged = False
            break
        user = cursor.execute(f"SELECT * FROM clientes WHERE usuario = '{username_or_email}' OR email = '{username_or_email}'")
        user = user.fetchall()
        # USUÁRIO OU EMAIL NÃO EXISTE
        if user == []:
            sleep(1)
            print("\033[0;31mEste usuário ou email não existe!\033[m")
            username_or_email_exists = False
        else:
            # CONFIRMAÇÃO DA SENHA
            password_confirmation = False
            while password_confirmation == False:
                sleep(1)
                password = str(input("\033[0;33mDigite sua senha: \033[m"))
                # VERIFICA SE O USUÁRIO QUER SAIR
                if password == "0":
                    sleep(0.7)
                    print("\033[0;32mRetornando ao menu!\033[m")
                    sleep(0.7)
                    username_or_email_exists = True
                    password_confirmation = True
                    logged = False
                    break
                user_password = user[0][2]
                # AS SENHAS ESTÃO INCORRETAS
                if password != user_password:
                    sleep(1)
                    print("\033[0;31mA senha está incorreta!\033[m")
                    password_confirmation = False
                else:
                    # USUÁRIO ESTÁ LOGADO
                    sleep(1.5)
                    print(f"\033[0;32mSeja bem-vindo, {user[0][0]}!\033[m")
                    password_confirmation = True
                    username_or_email_exists = True
                    logged = True
                    sleep(1)
    return logged
# MENU FINAL =======================================================================================================
def Menu_final():
    inicio()
    sleep(0.7)
    print("\033[0;33m1\033[m - Ver produtos cadastrados")
    sleep(0.4)
    print("\033[0;33m2\033[m - Cadastrar produtos")
    sleep(0.4)
    print("\033[0;33m3\033[m - Sair da conta")
    sleep(0.4)
    while True:
        try:
            opcao = int(input("\033[0;33mEscolha uma das opções acima para continuar: \033[m"))
            break
        except ValueError:
            sleep(1)
            print(f"\033[0;31mDigite um número!\033[m")
    return opcao
# PRODUTOS CADASTRADOS =============================================================================================
def Registred_products():
    inicio()
    sleep(0.5)
    # LISTA DOS PRODUTOS CADASTRADOS NO BANCO DE DADOS
    print("\033[0;32mAqui está a lista dos produtos cadastrados:\033[m")
    sleep(0.5)
    print(f"\033[0;33m{'Nome':<14}{'Preço':<12}{'Quantidade':<15}{'ID'}\033[m")
    # SELECIONAR OS PRODUTOS NO BANCO DE DADOS
    product = cursor.execute(f"SELECT * FROM produtos")
    product = product.fetchall()
    # MOSTRAR AS INFORMAÇÕES DE TODOS OS PRODUTOS REGISTRADOS
    for products in product:
        sleep(0.3)
        print(f"{products[0]:<12}R${float(products[1]):<15.2f}{products[2]:<12}{products[3]}")
    # ESPERANDO RESPOSTA DO USUÁRIO PARA VOLTAR AO MENU
    answer = False
    while answer == False:
        sleep(0.5)
        answer = str(input("\033[0;33mDigite \033[0;36mvoltar\033[m \033[0;33mpara retornar ao menu: \033[m"))
        # RESPOSTA INVÁLIDA
        if answer != "voltar":
            sleep(1)
            print("\033[0;31mResposta inválida!\033[m")
            answer = False
        # RETORNANDO PARA O MENU
        else:
            sleep(1)
            print("\033[0;32mRetornando para o menu!\033[m")
            answer = True
            sleep(0.5)
# CADASTRAR PRODUTOS ===============================================================================================
def Register_products():
    inicio()
    sleep(1)
    print("\033[0;36mDigite 0 à qualquer momento para sair do registro dos produtos!\033[m")
    # VERIFICAR O NOME DO PRODUTO
    product_confirmation = False
    while product_confirmation == False:
        product_name = str(input("\033[0;33mDigite o nome do seu produto: \033[m"))
        # VERIFICA SE O USUÁRIO QUER SAIR
        if product_name == "0":
            sleep(0.7)
            print("\033[0;32mRetornando ao menu!\033[m")
            sleep(0.7)
            product_confirmation = True
            break
        product = cursor.execute(f"SELECT * FROM produtos WHERE nome = '{product_name}'")
        product = product.fetchall()
        # REGISTRAR O PREÇO DO PRODUTO
        sleep(1)
        if product == []:
            product_price = str(input("\033[0;33mDigite o preço do seu produto: \033[m"))
            # VERIFICA SE O USUÁRIO QUER SAIR
            if product_price == "0":
                sleep(0.7)
                print("\033[0;32mRetornando ao menu!\033[m")
                sleep(0.7)
                product_confirmation = True
                id_confirmation = True
                break
            sleep(1)
            # VERIFICAR O ID DO PRODUTO
            id_confirmation = False
            while id_confirmation == False:
                product_id = str(input("\033[0;33mDigite o id do seu produto (de 1 à 999): \033[m"))
                # VERIFICA SE O USUÁRIO QUER SAIR
                if product_id == "0":
                    sleep(0.7)
                    print("\033[0;32mRetornando ao menu!\033[m")
                    sleep(0.7)
                    product_confirmation = True
                    id_confirmation = True
                    break
                product = cursor.execute(f"SELECT * FROM produtos WHERE id = '{product_id}'")
                product = product.fetchall()
                # REGISTRAR A QUANTIDADE DO PRODUTO EM ESTOQUE
                sleep(1)
                if product == []:
                    product_quantify = str(input("\033[0;33mDigite a quantidade do seu produto que tem em estoque: \033[m"))
                    # VERIFICA SE O USUÁRIO QUER SAIR
                    if product_quantify == "0":
                        sleep(0.7)
                        print("\033[0;32mRetornando ao menu!\033[m")
                        sleep(0.7)
                        product_confirmation = True
                        id_confirmation = True
                        break
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