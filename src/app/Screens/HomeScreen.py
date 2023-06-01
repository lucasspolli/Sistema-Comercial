from time import sleep
from Repositories.UsersRepository import UsersRepository
from Repositories.CartsRepository import CartsRepository

import sys

sys.path.insert(1, '../app/Screens')

from DefaultScreen import DefaultScreen

usersRepository = UsersRepository()
cartsRepository = CartsRepository()

class HomeScreen(DefaultScreen):
    def __init__(self, user):
        self.user = user

    def showScreen(self):
        options = [
            { "key": 1, "text": "Registrar uma conta", "handle": self.Register },
            { "key": 2, "text": "Logar em uma conta", "handle": self.Login },
            { "key": 3, "text": "Sair do menu", "handle": self.Exit }
        ]

        while not self.user.isLogged:
            self.banner(True)
            self.showOptions(options)

            selectedOption = self.selectOption()

            self.executeOption(options, selectedOption)

            if selectedOption == 3:
                break

    def Register(self):
        self.banner()
        
        sleep(0.5)
        print("\033[0;36mDigite 0 à qualquer momento para sair do cadastro!\033[m")
        
        while True:
            username = str(input("\033[0;33mDigite seu nome de usuário: \033[m"))

            if username == "0":
                self.printReturningToMenu()
                return

            userAlreadyExists = usersRepository.findByUsername(username)

            if userAlreadyExists:
                sleep(1)
                print("\033[0;31mEsse usuário já foi cadastrado!\033[m")
            else:
                break

        while True:
            sleep(1)
            email = str(input("\033[0;33mDigite seu email: \033[m"))
            
            if email == "0":
                self.printReturningToMenu()
                return
            
            emailAlreadyExists = usersRepository.findByEmail(email)
            
            if emailAlreadyExists:
                sleep(1)
                print("\033[0;31mEsse email já foi cadastrado!\033[m")
            else:
                break
                
        while True:
            sleep(1)
            password = str(input("\033[0;33mDigite sua senha: \033[m"))

            if password == "0":
                self.printReturningToMenu()
                return

            sleep(1)
            passwordConfirm = str(input("\033[0;33mConfirme a sua senha: \033[m"))

            if passwordConfirm == "0":
                self.printReturningToMenu()
                return
            
            if password != passwordConfirm:
                sleep(1)
                print("\033[0;31mAs senhas não se coincidem!\033[m")
            else:
                userId = usersRepository.create(username, email, password)

                cartsRepository.create(userId)

                sleep(1.5)
                print(f"\n\033[0;32mSeja bem-vindo, {username}!\033[m")
                sleep(1)

                self.user.isLogged = True
                self.user.id = userId
                
                break

    def Login(self):
        self.banner()
        
        sleep(1)
        print("\033[0;36mDigite 0 à qualquer momento para sair do login!\033[m")

        while True:
            usernameOrEmail = str(input("\033[0;33mDigite seu nome de usuário ou email: \033[m"))

            if usernameOrEmail == "0":
                self.printReturningToMenu()
                return
            
            userExists = usersRepository.findByUsername(usernameOrEmail)

            if userExists:
                break

            userExists = usersRepository.findByEmail(usernameOrEmail)

            if userExists:
                break
            
            sleep(1)
            print("\033[0;31mEste usuário ou email não existe!\033[m")

        while True:
            sleep(1)
            typedPassword = str(input("\033[0;33mDigite sua senha: \033[m"))

            if typedPassword == "0":
                self.printReturningToMenu()
                return
            
            if typedPassword == userExists.password:
                cartsRepository.create(userExists.id)

                sleep(1.5)
                print(f"\n\033[0;32mSeja bem-vindo, {userExists.username}!\033[m")

                self.user.isLogged = True
                self.user.id = userExists.id

                sleep(1)
                break
           
            sleep(1)
            print("\033[0;31mA senha está incorreta!\033[m")

    def Exit(self):
        self.user.isLogged = False
        pass