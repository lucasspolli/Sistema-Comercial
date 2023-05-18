from time import sleep
import sys

sys.path.insert(1, '../')

from Database.tables import createClientsTable, createRegistredProductsTable, connection

from Screens.HomeScreen import HomeScreen
from Screens.LoggedScreen import LoggedScreen

sys.path.insert(1, './Class')

from Class.user import User

user = User()

homeScreen = HomeScreen(user)
loggedScreen = LoggedScreen(user)

createClientsTable(), createRegistredProductsTable()

homeScreen.showScreen()

if user.isLogged:
    loggedScreen.showScreen()
    
sleep(0.5)
print("="*66)
sleep(0.5)
print("\033[0;32mObrigado por usar o nosso sistema, volte sempre!\033[m\n")
sleep(0.5)