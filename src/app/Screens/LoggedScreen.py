from time import sleep
from Database.tables import connection, cursor
from DefaultScreen import DefaultScreen

class LoggedScreen(DefaultScreen):
    def __init__(self, user):
        self.user = user
      
    def showScreen(self):
        options = [
            { "key": 1, "text": "Ver produtos cadastrados", "handle": self.RegistredProducts },
            { "key": 2, "text": "Cadastrar produtos", "handle": self.RegisterProducts },
            { "key": 3, "text": "Comprar um produto", "handle": self.BuyProduct },
            { "key": 4, "text": "Pagar carrinho", "handle": self.PayTheCart },
            { "key": 5, "text": "Sair da conta", "handle": self.Exit },
        ]

        while self.user.isLogged == True:
            self.banner()
            self.showOptions(options)

            selectedOption = self.selectOption()
            
            self.executeOption(options, selectedOption)

            if selectedOption == 5:
                break
        
    # PRODUTOS CADASTRADOS ==============================================================================================
    def RegistredProducts(self):
        self.banner()
        sleep(0.5)
        # LISTA DOS PRODUTOS CADASTRADOS NO BANCO DE DADOS
        print("\033[0;32mAqui está a lista dos produtos cadastrados:\033[m")
        sleep(0.5)
        print(f"\033[0;33m{'Nome':<24}{'Preço':<12}{'Quantidade':<15}{'ID'}\033[m")
        # SELECIONAR OS PRODUTOS NO BANCO DE DADOS
        product = cursor.execute(f"SELECT * FROM produtos")
        product = product.fetchall()
        if product == []:
            sleep(1)
            print("\033[0;31mNo momento ainda não temos produtos em estoque!\033[m")
            sleep(2)
        else:
            # MOSTRAR AS INFORMAÇÕES DE TODOS OS PRODUTOS REGISTRADOS
            for products in product:
                sleep(0.3)
                print(f"{products[0]:<22}R${float(products[1]):<15.2f}{products[2]:<12}{products[3]}")
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
                    self.printReturningToMenu()
                    sleep(0.5)
                    break
    # CADASTRAR PRODUTOS ================================================================================================
    def RegisterProducts(self):
        self.banner()
        cont = 0
        adminConfirmation = False
        while adminConfirmation == False:
            sleep(1)
            adminPassword = str(input("\033[0;33mDigite a senha de admin: \033[m"))
            if adminPassword != "9078":
                cont = cont + 1
                sleep(1)
                if cont == 3:
                    print("\033[0;31m3 tentativas erradas!\033[m")
                    adminConfirmation = True
                    break
                else:
                    print("\033[0;31mSenha de admin errada!\033[m")
                    adminConfirmation = False
            else:
                adminConfirmation = True
                sleep(1)
                print("\033[0;36mDigite 0 à qualquer momento para sair do registro dos produtos!\033[m")
                # VERIFICAR O NOME DO PRODUTO
                productConfirmation = False
                while productConfirmation == False:
                    productName = str(input("\033[0;33mDigite o nome do seu produto: \033[m"))
                    # VERIFICA SE O USUÁRIO QUER SAIR
                    if productName == "0":
                        self.printReturningToMenu()
                        productConfirmation = True
                        adminConfirmation = True
                        break
                    product = cursor.execute(f"SELECT * FROM produtos WHERE nome = '{productName}'")
                    product = product.fetchall()
                    # REGISTRAR O PREÇO DO PRODUTO
                    if product == []:
                        productConfirmation = True
                        priceConfirmation = False
                        while priceConfirmation == False:
                            sleep(1)
                            try:
                                productPrice = float(input("\033[0;33mDigite o preço do seu produto: \033[m"))
                                break
                            except ValueError:
                                sleep(1)
                                print("\033[0;31mDigite somente os números do preço ou digite com '.' os centavos!\033[m")
                                priceConfirmation = False
                        # VERIFICA SE O USUÁRIO QUER SAIR
                        if productPrice == "0":
                            self.printReturningToMenu()
                            priceConfirmation = True
                            break
                        quantifyConfirmation = False
                        while quantifyConfirmation == False:
                            sleep(1)
                            try:
                                productQuantify = int(input("\033[0;33mDigite a quantidade do seu produto que tem em estoque: \033[m"))
                                break
                            except ValueError:
                                sleep(1)
                                print("\033[0;31mDigite somente valores inteiros!\033[m")
                                quantifyConfirmation = False
                        # VERIFICA SE O USUÁRIO QUER SAIR
                        if productQuantify == "0":
                            self.printReturningToMenu()
                            priceConfirmation = True
                            break
                        # SELECIONAR OS PRODUTOS NO BANCO DE DADOS
                        product = cursor.execute(f"SELECT * FROM produtos")
                        product = product.fetchall()
                        # DEFINIR O ID DO PRODUTO
                        productsId = 0
                        if product == []:
                            pass
                        else:
                            for productsId in product:
                                productsId += 1
                        # ADICIONAR O PRODUTO À TABELA PRODUTOS NO BANCO DE DADOS
                        cursor.execute(f"INSERT INTO produtos (nome, preço, quantidade, id) VALUES('{productName}', '{productPrice}', '{productQuantify}', '{productsId}')")
                        connection.commit()
                        sleep(1)
                        # FINALIZAÇÃO DA FUNÇÃO
                        print("\033[0;32mSeu produto foi adicionado ao sistema!\033[m")
                        priceConfirmation = True
                        sleep(1)
                        break
                    # JÁ EXISTE UM PRODUTO COM O NOME DIGITADO
                    elif productName == product[0][0]:
                        sleep(1)
                        print("\033[0;31mEste nome de produto já existe!\033[m")
                        productConfirmation = False
    # COMPRAR PRODUTOS ==================================================================================================
    def BuyProduct(self):
        self.banner()
        # LISTA DOS PRODUTOS CADASTRADOS NO BANCO DE DADOS
        sleep(0.5)
        print("\033[0;32mAqui está a lista dos produtos cadastrados:\033[m")
        sleep(0.5)
        print(f"\033[0;33m{'Nome':<24}{'Preço':<12}{'Quantidade':<15}{'ID'}\033[m")
        # SELECIONAR OS PRODUTOS NO BANCO DE DADOS
        product = cursor.execute(f"SELECT * FROM produtos")
        product = product.fetchall()
        # MOSTRAR AS INFORMAÇÕES DE TODOS OS PRODUTOS REGISTRADOS
        for products in product:
            sleep(0.3)
            print(f"{products[0]:<22}R${float(products[1]):<15.2f}{products[2]:<12}{products[3]}")
        # RECEBER INFORMAÇÕES DOS PRODUTOS QUE DESEJAM COMPRAR
        confirmation = False
        while confirmation == False:
            sleep(0.5)
            productId = str(input("\033[0;33mDigite o ID do produto que deseja comprar: \033[m"))
            product = cursor.execute(f"SELECT * FROM produtos WHERE id = '{productId}'")
            product = product.fetchall()
            productInCart = cursor.execute(f"SELECT * FROM '{self.user.id}' WHERE id = '{productId}'")
            productInCart = productInCart.fetchall()
            # ID DIGITADO NÃO EXISTE
            if product == []:
                sleep(1)
                print("\033[0;31mEste ID de produto não existe!\033[m")
                confirmation = False
            else:
                confirmation = True
                # ID EXISTE NO BANCO DE DADOS
                if productId == product[0][3]:
                    sleep(1)
                    self.banner()
                    sleep(0.5)
                    print("\033[0;33mO produto escolhido foi:\033[m")
                    sleep(0.5)
                    print(f"\033[0;36m{product[0][0]} que custa R${float(product[0][1]):.2f} com {product[0][2]} quantidades em estoque e seu ID é {product[0][3]}.\033[m")
                    # CONFIRMAR A QUANTIDADE QUE O USUÁRIO QUE COMPRAR
                    productQuantifyConfirmation = False
                    while productQuantifyConfirmation == False:
                        sleep(1)
                        productQuantify = str(input("\033[0;33mDigite a quantidade que deseja comprar: \033[m"))
                        productQuantify = int(productQuantify)
                        if productInCart == []:
                            productQuantifyAvaiable = int(product[0][2])
                            # QUANTIDADE ESTÁ DENTRO DAS REGRAS
                            if (productQuantify <= productQuantifyAvaiable) and (productQuantify > 0):
                                # ADICIONAR O PRODUTO AO CARRINHO DO USUÁRIO
                                cursor.execute(f"INSERT INTO '{self.user.id}' (nome, preço, quantidade, id) VALUES('{product[0][0]}', '{product[0][1]}', '{productQuantify}', '{product[0][3]}')")
                                connection.commit()
                                sleep(1.5)
                                print("\033[0;32mSeu produto foi adicionado ao carrinho!\033[m")
                                sleep(1)
                                productQuantifyConfirmation = True
                            # QUANTIDADE DIGITADA INVÁLIDA
                            else:
                                sleep(1)
                                print("\033[0;31mQuantidade de produto inválida!\033[m")
                                productQuantifyConfirmation = False
                        # SE JÁ EXISTIR O PRODUTO NO CARRINHO
                        else:
                            # ADICIONAR MAIS UM PRODUTO AO CARRINHO DO USUÁRIO
                            productQuantifyToAdd = (int(productInCart[0][2]) + productQuantify)
                            cursor.execute(f"UPDATE '{self.user.id}' SET quantidade = '{productQuantifyToAdd}' WHERE id = '{product[0][3]}'")
                            connection.commit()
                            sleep(2)
                            print(f"\033[0;32mMais {productQuantify} {productInCart[0][0]} foi adicionado ao carrinho!\033[m")
                            sleep(2)
                            break
    # MENU PAGAMENTO ====================================================================================================
    def paymentMenu(self):
        print("="*66)
        sleep(0.2)
        print("\033[0;33m1\033[m - Pagar no débito")
        sleep(0.2)
        print("\033[0;33m2\033[m - Pagar no crédito")
        sleep(0.2)
        print("\033[0;33m3\033[m - Sair do menu")
        sleep(0.2)
        while True:
            try:
                option = int(input("\033[0;33mComo você deseja pagar a sua conta? \033[m"))
                break
            except ValueError:
                sleep(1)
                print(f"\033[0;31mDigite um número!\033[m")
        return option
    # ATUALIZAR DADOS DOS PRODUTOS NO BANCO DE DADOS ====================================================================
    def updateData(self, product):
        cursor.execute(f"DELETE FROM '{self.user.id}'")
        for products in product:
            productInDatabase = cursor.execute(f"SELECT * FROM produtos WHERE id = '{products[3]}'")
            productInDatabase = productInDatabase.fetchall()
            productQuantify = int(productInDatabase[0][2]) - int(products[2])
            
            cursor.execute(f"UPDATE produtos SET quantidade = '{productQuantify}' WHERE id = '{products[3]}'")
            connection.commit()

        sleep(1.5)
    # PAGAR CARRINHO ====================================================================================================
    def PayTheCart(self):
        self.banner()
        answerConfirmation = False
        while answerConfirmation == False:
            sleep(1)
            # LISTA DOS PRODUTOS NO CARRINHO
            print("\033[0;32mAqui está a lista dos produtos do seu carrinho:\033[m")
            sleep(0.5)
            print(f"\033[0;33m{'Nome':<24}{'Preço':<12}{'Quantidade':<15}{'ID'}\033[m")
            # SELECIONAR OS PRODUTOS NO BANCO DE DADOS
            product = cursor.execute(f"SELECT * FROM '{self.user.id}'")
            product = product.fetchall()
            if product == []:
                sleep(1)
                print(f"\033[0;32mVocê não tem produtos no carrinho!\033[m")
                sleep(2)
                answerConfirmation = True
                break
            # MOSTRAR AS INFORMAÇÕES DE TODOS OS PRODUTOS REGISTRADOS
            total = 0
            for products in product:
                sleep(0.3)
                print(f"{products[0]:<22}R${float(products[1]):<15.2f}{products[2]:<12}{products[3]}")
                if products[2] == 1:
                    total = total + float(products[1])
                else:
                    total = total + (float(products[1]) * int(products[2]))
            # VALOR TOTAL DO CARRINHO
            sleep(1)
            print(f"\033[0;32mO valor total do seu carrinho é R${total:.2f}\033[m")
            sleep(1)
            # PAGAMENTO
            optionConfirmation = False
            while optionConfirmation == False:
                option = self.paymentMenu()
                # PAGOU COM DÉBITO
                if option == 1:
                    self.updateData(product, self.user.id)
                    print(f"\033[0;32mVocê pagou R${total:.2f} no débito!\033[m")
                    sleep(2)
                    break
                # PAGOU COM CRÉDTIO
                elif option == 2:
                    installmentsConfirmation = False
                    while installmentsConfirmation == False:
                        sleep(1)
                        installments = int(input(f"\033[0;33mEm quantas parcelas deseja pagar? \033[m"))
                        if installments > 12:
                            sleep(1)
                            print("\033[0;31mQuantidade de parcelas maior que 12!\033[m")
                            installmentsConfirmation = False
                        else:
                            self.updateData(product, self.user.id)
                            value = total / installments
                            print(f"\033[0;32mVocê irá pagar R${value:.2f} em {installments}x!\033[m")
                            sleep(2)
                            break
                # RETORNANDO PARA O MENU
                elif option == 3:
                    self.printReturningToMenu()
                    break
                # OPÇÃO INVÁLIDA
                else:
                    sleep(1)
                    print("\033[0;31mOpção inválida!\033[m")
                    sleep(1)
                    optionConfirmation = False
            answerConfirmation = True

    def Exit():
        connection.close()
        return