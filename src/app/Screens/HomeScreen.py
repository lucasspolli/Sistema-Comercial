from time import sleep
from Database.tables import connection, cursor
import sys

sys.path.insert(1, '../app/Screens')

from DefaultScreen import DefaultScreen

class HomeScreen(DefaultScreen):
    def __init__(self, user):
        self.user = user

    def showScreen(self):
        options = [
            { "key": 1, "text": "Registrar uma conta", "handle": self.Register },
            { "key": 2, "text": "Logar em uma conta", "handle": self.Login },
            { "key": 3, "text": "Sair do menu", "handle": self.Exit }
        ]

        while self.user.isLogged == False:
            self.banner(True)
            self.showOptions(options)

            selectedOption = self.selectOption()

            self.executeOption(options, selectedOption)

            if selectedOption == 3:
                break

    def Register(self):
        self.banner()
        # CONFIRMAÇÃO DO NOME DO USUÁRIO
        sleep(0.5)
        print("\033[0;36mDigite 0 à qualquer momento para sair do cadastro!\033[m")
        usernameConfirmation = False
        while usernameConfirmation == False:
            username = str(input("\033[0;33mDigite seu nome de usuário: \033[m"))
            # VERIFICA SE O USUÁRIO QUER SAIR
            if username == "0":
                self.printReturningToMenu()
                usernameConfirmation = True
                return
            cursor.execute(f"SELECT * FROM clientes WHERE usuario = '{username}'")
            result = cursor.fetchall()
            # USUÁRIO JÁ EXISTE
            if result != []:
                sleep(1)
                print("\033[0;31mEsse usuário já foi cadastrado!\033[m")
            else:
                break
        # CONFIRMAÇÃO DO EMAIL
        emailConfirmation = False
        while emailConfirmation == False:
            sleep(1)
            email = str(input("\033[0;33mDigite seu email: \033[m"))
            # VERIFICA SE O USUÁRIO QUER SAIR
            if email == "0":
                self.printReturningToMenu()
                return
            cursor.execute(f"SELECT * FROM clientes WHERE email = '{email}'")
            result = cursor.fetchall()
            # EMAIL JÁ FOI CADASTRADO
            if result != []:
                sleep(1)
                print("\033[0;31mEsse email já foi cadastrado!\033[m")
            else:
                break
        # CONFIRMAÇÃO DA SENHA
        passwordConfirmation = False
        while passwordConfirmation == False:
            sleep(1)
            password = str(input("\033[0;33mDigite sua senha: \033[m"))
            # VERIFICA SE O USUÁRIO QUER SAIR
            if password == "0":
                self.printReturningToMenu()
                return
            sleep(1)
            passwordConfirm = str(input("\033[0;33mConfirme a sua senha: \033[m"))
            # VERIFICA SE O USUÁRIO QUER SAIR
            if passwordConfirm == "0":
                self.printReturningToMenu()
                return
            cursor.execute("SELECT * from clientes")
            result = cursor.fetchall()
            # DEFINIR O ID DO USUÁRIO
            if result == []:
                pass
            else:
                for users in result:
                    self.user.id += 1
            # AS SENHAS ESTÃO INCORRETAS
            if password != passwordConfirm:
                sleep(1)
                print("\033[0;31mAs senhas não se coincidem!\033[m")
            # ADICIONAR O USUÁRIO AO BANCO DE DADOS
            else:
                cursor.execute(f"INSERT INTO clientes (usuario, email, senha, id) VALUES('{username}', '{email}', '{password}', '{self.user.id}')")
                cursor.execute(f'''CREATE TABLE IF NOT EXISTS '{self.user.id}' (
                                    nome varchar(1),
                                    preço varchar(1),
                                    quantidade varchar(1),
                                    id varchar(1))''')
                connection.commit()
                # TESTAR
                # userInformations = cursor.execute(f"SELECT * FROM clientes WHERE usuario = '{username}' OR email = '{email}'")
                # userInformations = userInformations.fetchall()
                sleep(1.5)
                print(f"\n\033[0;32mSeja bem-vindo, {username}!\033[m")
                self.user.isLogged = True
                sleep(1)
                break

    def Login(self):
        self.banner()
        # VERIFICAR SE EXISTE O NOME DE USUÁRIO OU EMAIL
        sleep(1)
        print("\033[0;36mDigite 0 à qualquer momento para sair do login!\033[m")
        usernameOrEmailExists = False
        while usernameOrEmailExists == False:
            usernameOrEmail = str(input("\033[0;33mDigite seu nome de usuário ou email: \033[m"))
            # VERIFICA SE O USUÁRIO QUER SAIR
            if usernameOrEmail == "0":
                self.printReturningToMenu()
                return
            cursor.execute(f"SELECT * FROM clientes WHERE usuario = '{usernameOrEmail}' OR email = '{usernameOrEmail}'")
            userInformations = cursor.fetchall()
            # USUÁRIO OU EMAIL NÃO EXISTE
            if userInformations == []:
                sleep(1)
                print("\033[0;31mEste usuário ou email não existe!\033[m")
            else:
                break
        # CONFIRMAÇÃO DA SENHA
        passwordConfirmation = False
        while passwordConfirmation == False:
            sleep(1)
            password = str(input("\033[0;33mDigite sua senha: \033[m"))
            # VERIFICA SE O USUÁRIO QUER SAIR
            if password == "0":
                self.printReturningToMenu()
                return
            user_password = userInformations[0][2]
            # AS SENHAS ESTÃO INCORRETAS
            if password != user_password:
                sleep(1)
                print("\033[0;31mA senha está incorreta!\033[m")
            else:
                # USUÁRIO ESTÁ LOGADO
                sleep(1.5)
                print(f"\n\033[0;32mSeja bem-vindo, {userInformations[0][0]}!\033[m")
                self.user.isLogged = True
                sleep(1)
                break
    
    def Exit(self):
        connection.close()
        return