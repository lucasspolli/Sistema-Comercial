from time import sleep
import sqlite3

connection = sqlite3.connect('banco_de_dados.db')
cursor = connection.cursor()

# INÍCIO
sistema = "S I S T E M A"
comercial = "C O M E R C I A L"

def inicio():
    print("="*66)
    print(f"{sistema:^66}")
    print(f"{comercial:^66}")
    print("="*66)
# MENU
def menu():
    print("="*66)
    sleep(0.7)
    print("1 - Registrar")
    sleep(0.4)
    print("2 - Logar")
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
# REGISTRAR CONTA ==================================================================================================
def Register():
    print("="*66)
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
            sleep(1)
            print("\033[0;32mSeu usuário foi adicionado ao sistema!\033[m")
            password_confirmation = True
            sleep(0.5)
            logged = True
    return logged
# LOGAR NA CONTA ===================================================================================================
def Login():
    print("="*66)
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
                password = str(input("\033[0;33mDigite sua senha: \033[m"))
                user_password = user[0][2]
                # AS SENHAS ESTÃO INCORRETAR
                if password != user_password:
                    sleep(1)
                    print("\033[0;31mA senha está incorreta!\033[m")
                    password_confirmation = False
                # USUÁRIO ESTÁ LOGADO
                else:
                    sleep(1)
                    print(f"\033[0;32mSeja bem-vindo, {user[0][0]}!\033[m")
                    password_confirmation = True
                    username_or_email_exists = True
                    break
                logged = True
    return logged
# CONSULTAR VALOR DO CARRINHO
def consultar_carrinho(valor_pago):
    soma = 0
    print("="*66)
    sleep(0.2)
    print("\033[0;33mSegue abaixo o valor total do seu carrinho:\033[m")
    sleep(1)
    cursor.execute("SELECT * FROM dados")
    resultado = cursor.fetchall()
    if resultado != []:
        for produto in resultado:
            if produto[4] == 'nao':
                quantidade = int(produto[3])
                preço = float(produto[2])
                if quantidade > 1:
                    soma += preço * quantidade
                else:
                    soma += preço
    else:
        sleep(1)
        print(f"\033[0;32mA soma do seu carrinho deu R$0.00!\033[m")
        sleep(0.5)
        print(f"\033[0;32mNão tem nada à ser pago aqui!\033[m")
        sleep(1)
        return valor_pago
    print(f"\033[0;32mA soma do seu carrinho deu R${soma:.2f}!\033[m")
    cursor.execute("SELECT * FROM dados")
    resultado = cursor.fetchall()
    sim = 'sim'
    for produto in resultado:
        if produto[4] == 'nao':
            print(soma, valor_pago)
            if soma != valor_pago:
                sleep(1)
                print("\033[0;33mVocê tem produtos que não foram pagos! \033[m")
                sleep(1)
                print(f"\033[0;33mA diferença é de R${soma:.2f}! \033[m")
                while True:
                    sleep(1)
                    escolha = str(input("\033[0;33mVocê deseja pagar a sua conta? (sim/nao) \033[m"))
                    if escolha in "nao":
                        break
                    elif escolha in "sim":
                        sleep(0.2)
                        print("="*57)
                        sleep(0.2)
                        print("1 - Pagar no dinheiro")
                        sleep(0.2)
                        print("2 - Pagar no débito")
                        sleep(0.2)
                        print("3 - Pagar no crédito")
                        sleep(0.2)
                        opcao = int(input("\033[0;33mComo você deseja pagar a sua conta? \033[m"))
                        sleep(1)
                        if opcao == 1:
                            print(f"\033[0;32mVocê pagou R${soma:.2f} no dinheiro à vista!\033[m")
                            cursor.execute("UPDATE dados SET pago = '"+sim+"'")
                            connection.commit()
                            valor_pago += soma
                            return valor_pago
                        elif opcao == 2:
                            print(f"\033[0;32mVocê pagou R${soma:.2f} no débito!\033[m")
                            cursor.execute("UPDATE dados SET pago = '"+sim+"'")
                            connection.commit()
                            valor_pago += soma
                            return valor_pago
                        elif opcao == 3:
                            parcelas = int(input("\033[0;33mEm quantas parcelas você deseja pagar a sua conta? \033[m"))
                            sleep(1)
                            parcelado = soma / parcelas
                            print(f"\033[0;32mVocê irá pagar {parcelas}x de R${parcelado:.2f} no crédito!\033[m")
                            cursor.execute("UPDATE dados SET pago = '"+sim+"'")
                            connection.commit()
                            valor_pago += soma
                            return valor_pago
                        else:
                            print(f"\033[0;31mDigite uma opção válida!\033[m")
                    else:
                        print(f"\033[0;31mDigite apenas: sim/nao\033[m")
            else:
                sleep(1)
                print(f"\033[0;32mA sua conta de R${soma:.2f} já foi paga!\033[m")
                return valor_pago