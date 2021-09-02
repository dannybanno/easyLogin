from colorama import Fore, Back, Style
import random
import pyautogui


print(Fore.RED + '''

.__                .__        
|  |   ____   ____ |__| ____  
|  |  /  _ \ / ___\|  |/    \ 
|  |_(  <_> ) /_/  >  |   |  |
|____/\____/\___  /|__|___|  /
           /_____/         \/

''')

loginUsername = input('Enter Username: ')

loginPassword = input('Enter Password: ')


def login():
           if loginUsername == 'danny':
               if loginPassword == 'danny2':
                   print('Welcome ' + loginUsername)
           else:
                      print('Wrong info Try Again!')
                      return login
