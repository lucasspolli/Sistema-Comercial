from time import sleep
import sqlite3

connection = sqlite3.connect('ecommerce.db')
cursor = connection.cursor()

cart = []
# PRODUTOS
products = [{"id": 55, "name": 'Teclado Logitech', "price": 359.99, "amount": 1},
            {"id": 256, "name": 'Fone sem fio', "price": 150.00, "amount": 1},
            {"id": 541, "name": 'Iphone 16', "price": 20000.00, "amount": 1},
            {"id": 13, "name": 'Nokia', "price": 135.50, "amount": 1},
            {"id": 45, "name": 'Monitor 19"', "price": 700.00, "amount": 1},
            {"id": 698, "name": 'TV Samsung 4k 75"', "price": 5700.00, "amount": 1},
            {"id": 1243, "name": 'PC Gamer Gtx 1050Ti', "price": 5000.00, "amount": 1},
            {"id": 908, "name": 'Mouse Razzer', "price": 99.99, "amount": 1},
            {"id": 258, "name": 'Tablet CCE', "price": 450.00, "amount": 1},
            {"id": 157, "name": 'Copo stanley', "price": 300.00, "amount": 1}]
# INÍCIO
ecommerce = "E - C O M M E R C E"
do = "D O"
lukako = "L U K A K O"

def inicio():
    print("="*57)
    print(f"{ecommerce:^57}")
    print(f"{do:^57}")
    print(f"{lukako:^57}")
    print("="*57)
# MENU
def menu():
    sleep(0.2)
    print("="*57)
    sleep(0.2)
    print("1 - Adicionar um produto ao carrinho")
    sleep(0.2)
    print("2 - Remover um produto do carrinho")
    sleep(0.2)
    print("3 - Consultar valor do carrinho")
    sleep(0.2)
    print("4 - Sair do menu")
    sleep(0.2)
    while True:
        try:
            opcao = int(input("\033[0;33mEscolha uma das opções acima para continuar: \033[m"))
            break
        except ValueError:
            sleep(1)
            print(f"\033[0;31mDigite um número!\033[m")
    return opcao
# ADICIONAR UM PRODUTO
def adicionar_produto():
    print("="*57)
    sleep(1)
    print("\033[0;32mSegue abaixo uma lista dos nosso produtos disponíveis no estoque:\033[m")
    sleep(1)
    print("\033[0;33mNome                    Preço          Id\033[m")
    for produto in products:
        name = produto.get("name")
        price = produto.get("price")
        id = produto.get("id")
        sleep(0.2)
        print(f"{name:<23}", f"{price:<12.2f}", "(", f"{id}", ")")
    sleep(0.2)
    print("="*57)
    return_to_the_question = True
    while return_to_the_question == True:
        while True:
            try:
                sleep(1)
                product = int(input("\033[0;33mDigite o ID do produto que você deseja adicionar ao carrinho: \033[m"))
                break
            except ValueError:
                sleep(1)
                print(f"\033[0;31mDigite um número!\033[m")
        sleep(0.5)
        added = False
        for produto in products:
            name = produto.get("name")
            ids = produto.get("id")
            price = produto.get("price")
            amount = produto.get("amount")
            if product == ids:
                sleep(1)
                cursor.execute(f"SELECT * FROM dados WHERE id = {product}")
                resultado = cursor.fetchall()
                if resultado == []:
                    pago = 'nao'
                    comando = f"INSERT INTO dados (nome, id, preço, quantidade, pago) VALUES('{name}', '{product}', '{price}', '{amount}', '{pago}')"
                    cursor.execute(comando)
                    print(f"\033[0;32m{name} adicionado ao carrinho!\033[m")
                    added = True
                    connection.commit()
                    break
                else:
                    cursor.execute(f"SELECT quantidade FROM dados WHERE id = {product}")
                    quantidade = cursor.fetchall()
                    quantidade2 = int(quantidade[0][0])
                    quantidade2 += 1
                    comando2 = (f'UPDATE dados SET quantidade = {quantidade2} WHERE ID = {product}') ######
                    cursor.execute(comando2)
                    connection.commit()
                    print(f"\033[0;32mMais um(a) {name} adicionado ao carrinho!\033[m")
                    added = True
                    break
            elif added == False and ids == 157:
                sleep(1)
                print(f"\033[0;31mProduto não encontrado!\033[m")
        sleep(0.5)
        while True:
            escolha = str(input("\033[0;33mDeseja adicionar mais itens ao carrinho? (sim/nao) \033[m"))
            if escolha in "nao":
                return_to_the_question = False
                break
            elif escolha in "sim":
                break
            else:
                sleep(1)
                print(f"\033[0;31mDigite apenas: sim/nao\033[m")
# REMOVER UM PRODUTO
def remover_produto():
    print("="*57)
    sleep(0.2)
    print("\033[0;32mSegue abaixo os itens contidos no seu carrinho:\033[m")
    sleep(0.5)
    name2 = "Nome"
    id2 = "ID"
    price2 = "Preço"
    quantify2 = "Quantidade"
    #print(f"\033[0;33mNome                       ID          Preço       Quantidade\033[m")
    print(f"\033[0;33m{name2:<23} {price2:<14} {id2:<11} {quantify2}\033[m")
    #print(f"{name:<23}", f"{price:<12.2f}", f"{id}")
    #=============================================================================================================
    cursor.execute(f"SELECT * FROM dados")
    resultado = cursor.fetchall()
    print('Produtos:')
    
    for item in resultado:
        name = item[0]
        price = item[2]
        id = item[1]
        price = float(price)
        sleep(0.5)
        #print(item[0], f"{item[1]:>12}", f"{item[2]:>15}", f"{item[3]:>10}")
        print(f"{name:<23}", f"{price:<14.2f}", f"{id}")
    sleep(0.5)
    # TIRAR VARIÁVEL
    var = True
    cursor.execute("SELECT * FROM dados")
    resultado = cursor.fetchall()
    if resultado == []:
        sleep(1)
        print(f"\033[0;31mVocê não tem produtos em seu carrinho!\033[m")
    else:
        while var == True:
            try:
                sleep(1)
                id = int(input("\033[0;33mDigite o ID do item que você deseja remover do carrinho? \033[m"))
                sleep(1)
                cursor.execute(f"SELECT * FROM dados WHERE id = {id}")
                resultado = cursor.fetchall()
                if resultado == []:
                    sleep(1)
                    print(f"\033[0;31mProduto não encontrado!\033[m")
                else:
                    cursor.execute(f"SELECT * FROM dados WHERE id = {id}")
                    resultado = cursor.fetchall()
                    quantidade = int(resultado[0][3])
                    if quantidade > 1:
                        sleep(1)
                        quantidade -= 1
                        cursor.execute(f"SELECT * FROM dados WHERE id = {id}")
                        resultado = cursor.fetchall()
                        ##############
                        cursor.execute(f"UPDATE dados SET quantidade = {quantidade} WHERE id = {id}")
                        ##############
                        connection.commit()
                        print(f"\033[0;32mUm(a) dos(as) {resultado[0][0]} foi removido do carrinho!\033[m")
                        break
                    else:
                        cursor.execute(f"DELETE FROM dados WHERE id = {id}")
                        connection.commit()
                        print(f"\033[0;32m{resultado[0][0]} removido do carrinho!\033[m")
                        break
            except ValueError:
                sleep(1)
                print(f"\033[0;31mDigite um número!\033[m")
    
# CONSULTAR VALOR DO CARRINHO
def consultar_carrinho(valor_pago):
    soma = 0
    print("="*57)
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