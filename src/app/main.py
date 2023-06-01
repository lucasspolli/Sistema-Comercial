from time import sleep
import sys

sys.path.insert(1, '../')

from Database.main import createTables

from Screens.HomeScreen import HomeScreen
from Screens.LoggedScreen import LoggedScreen

sys.path.insert(1, './Class')

from Class.user import User

user = User()

homeScreen = HomeScreen(user)
loggedScreen = LoggedScreen(user)

createTables()

while True:
  homeScreen.showScreen()

  if user.isLogged:
    loggedScreen.showScreen()
  else:
    break

sleep(0.5)
print("="*66)
sleep(0.5)
print("\033[0;32mObrigado por usar o nosso sistema, volte sempre!\033[m\n")
sleep(0.5)