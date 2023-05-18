from time import sleep
import os

class DefaultScreen:
    def __init__(self):
        pass

    def printReturningToMenu(self):
        sleep(1)
        print("\n\033[0;32mRetornando ao menu!\033[m")
        sleep(1)

    def banner(self, showBannerSubtitle = False):
        print("\n" * os.get_terminal_size().lines)
        sleep(1)
        print("="*66)
        print(f"\033[0;34m{'S I S T E M A':^66}\033[m")
        print(f"\033[0;34m{'C O M E R C I A L':^66}\033[m")
        print("="*66)

        if showBannerSubtitle:
            sleep(0.5)
            print("\033[0;32mSeja bem vindo(a) ao maior sistema comercial da América Latina!\033[m")
            
    def showOptions(self, options):
        sleep(0.7)
        print("")

        for option in options:
            optionKey = (options.index(option) + 1)

            print(f"\033[0;33m{optionKey}\033[m", " - ", option["text"])
            sleep(0.4)

            if len(options) == optionKey:
                print("")

    def selectOption(self):
        while True:
            try:
                selectedOptionKey = int(input("\033[0;33mEscolha uma das opções acima para continuar: \033[m"))
                return selectedOptionKey
            except ValueError:
                sleep(1)
                print(f"\033[0;31mDigite um número!\033[m")
                
    def executeOption(self, options, selectedOption):
        findedOption = False

        for option in options:
            if option["key"] == selectedOption:
                findedOption = option

        if findedOption:
            sleep(1)
            findedOption["handle"]()
        else:
            sleep(1)
            print(f"\033[0;31mOpção inválida!\033[m")
            sleep(1)
            