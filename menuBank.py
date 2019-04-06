from bank import Bank

from colorama import Fore, Back, Style
import os
import os.path
import time
from colorama import init
init()

asw = ""


def bankMenu():
    option = "0"
    print("+{:-<50}+".format(""))
    print('\x1b[6;30;47m' + "|{:^50}|".format("Bank System")+'\x1b[0m')
    print("+{:-<50}+".format(""))
    print('\x1b[1;32;40m' +
          "|{:50}|".format("1. Create a new account")+'\x1b[0m')
    print("+{:-<50}+".format(""))
    print('\x1b[1;33;40m' + "|{:50}|".format("2. Deposit")+'\x1b[0m')
    print("+{:-<50}+".format(""))
    print('\x1b[1;34;40m' + "|{:50}|".format("3. Withdraw")+'\x1b[0m')
    print("+{:-<50}+".format(""))
    print('\x1b[1;35;40m' +
          "|{:50}|".format("4. Check your bank movements")+'\x1b[0m')
    print("+{:-<50}+".format(""))

    time.sleep(1)
    option = input("Choose one option: ")
    print("+{:-<50}+".format(""))
    print("")
    time.sleep(2)
    if option == "1":
        Bank.newAccount("")
    elif option == "2":
        Bank.deposit("")
    elif option == "3":
        Bank.withdraw("")
    elif option == "4":
        Bank.checkMovements("")

    else:
        print("+{:-<50}+".format(""))
        print('\x1b[0;37;41m' +
              "|{:^50}|".format("Option doesn't exist")+'\x1b[0m')
        print("+{:-<50}+".format(""))
        exit


def initAll():
    bankMenu()
    asw = input("Do you want to continue? (Y/N): ").upper()

    while asw == 'Y':
        os.system('cls')
        initAll()

    if asw == 'N':
        print("+{:-<50}+".format(""))
        print('\x1b[6;30;43m' +
              "|{:^50}|".format("Thanks for use this program")+'\x1b[0m')
        print("+{:-<50}+".format(""))
        exit

    else:
        print("+{:-<50}+".format(""))
        print('\x1b[0;37;41m' +
              "|{:^50}|".format("Option doesn't exist")+'\x1b[0m')
        print("+{:-<50}+".format(""))
        time.sleep(2)
        initAll()


initAll()
