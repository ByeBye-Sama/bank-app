from colorama import Fore, Back, Style
import sqlite3
import os
import os.path
import time
from colorama import init
init()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "bank.db")
db = sqlite3.connect(db_path)
cursor = db.cursor()
asw = ""
totalAmount = 0
transactionAmount = 0
transactionNum = 0
newAmount = 0


def newAccount():

    print("+{:-<143}+".format(""))
    print("|{:^143}|".format("REGISTER ACOUNT FORM"))
    print("+{:-<143}+".format(""))

    accNumber = raw_input("Insert new account number: ")
    email = raw_input("Insert new email: ")
    bankCode = raw_input("Insert bank code: ")
    totalAmount = int(raw_input("Insert first ammount: "))

    newAcc = '''INSERT INTO USER(accNumber,email,bankCode,totalAmount)
                VALUES ('%s', '%s', '%s', '%s') ''' % (accNumber, email, bankCode, totalAmount)

    cursor.execute(newAcc)
    db.commit()
    db.close()

    print("+{:-<143}+".format(""))
    print("|{:^143}|".format("NEW USER"))
    print("+{:-<143}+".format(""))
    print('\x1b[6;30;42m' + "|{:^143}|".format("SUCCESS")+'\x1b[0m')

    print("+{:-<30}+{:-<50}+{:-<30}+{:-<30}+".format("", "", "", ""))
    print("|{:^30}|{:^50}|{:^30}|{:^30}|".format(
        "Account Number", "Email", "Bank Code", "Total Amount"))
    print("+{:-<30}+{:-<50}+{:-<30}+{:-<30}+".format("", "", "", ""))

    print("|{:^30}|{:^50}|{:^30}|{:^30}|".format(
        accNumber, email, bankCode, totalAmount))
    print("+{:-<30}+{:-<50}+{:-<30}+{:-<30}+".format("", "", "", ""))


def deposit():

    print("+{:-<100}+".format(""))
    print("|{:^100}|".format("DEPOSIT FORM"))
    print("+{:-<100}+".format(""))

    accNumber = raw_input("Insert account number to login: ")
    findAcc = ("SELECT * FROM USER WHERE accNumber = ?")
    cursor.execute(findAcc, [(accNumber)])

    results = cursor.fetchall()

    if results:
        for i in results:
            print("+{:-<100}+".format(""))
            print("|{:^100}|".format('Welcome: ' + i[1]))
            print("+{:-<100}+".format(""))

            transactionDate = raw_input("Insert date with format (DD/MM/YY): ")
            print("+{:-<100}+".format(""))
            transactionNum = int(raw_input("Insert transaction number: "))
            print("+{:-<100}+".format(""))
            transactionAmount = int(raw_input("Insert deposit amount: "))
            print("+{:-<100}+".format(""))

            newTran = '''INSERT INTO MONEY(accNumber,transactionNum,transactionDate,transactionAmount)
                VALUES ('%s', '%s', '%s', '%s') ''' % (accNumber, transactionNum, transactionDate, transactionAmount)

            cursor.execute(newTran)
            db.commit()

            accountAmount = (
                "SELECT totalAmount FROM USER WHERE accNumber = ?")
            cursor.execute(accountAmount, [(accNumber)])
            currentAmount = cursor.fetchone()
            oldAmount = currentAmount[0]

            newAmount = oldAmount + transactionAmount

            updateAmount = (
                "UPDATE USER SET totalAmount =? WHERE accNumber = ?")
            cursor.execute(updateAmount, [(newAmount), (accNumber)])
            db.commit()

            print('\x1b[6;30;42m' + "|{:^100}|".format("SUCCESS")+'\x1b[0m')
            print("+{:-<100}+".format(""))
            print("|{:^100}|".format("You have now: " + str(newAmount)))
            print("+{:-<100}+".format(""))

    else:
        print("+{:-<100}+".format(""))
        print('\x1b[0;37;41m' +
              "|{:^100}|".format("Account doesn't exist")+'\x1b[0m')
        print("+{:-<100}+".format(""))

        again = raw_input("Do you want to try again? (Y/N): ").upper()

        if again != "N":
            deposit()
        else:
            print("+{:-<100}+".format(""))
            print("|{:^100}|".format("GOOD BYE"))
            print("+{:-<100}+".format(""))


def withdraw():

    print("+{:-<100}+".format(""))
    print("|{:^100}|".format("WITHDRAW FORM"))
    print("+{:-<100}+".format(""))

    accNumber = raw_input("Insert account number to login: ")
    findAcc = ("SELECT * FROM USER WHERE accNumber = ?")
    cursor.execute(findAcc, [(accNumber)])

    results = cursor.fetchall()

    if results:
        for i in results:
            print("+{:-<100}+".format(""))
            print("|{:^100}|".format('Welcome: ' + i[1]))
            print("+{:-<100}+".format(""))

            transactionDate = raw_input("Insert date with format (DD/MM/YY): ")
            print("+{:-<100}+".format(""))
            transactionNum = int(raw_input("Insert transaction number: "))
            print("+{:-<100}+".format(""))
            transactionAmount = int(raw_input("Insert withdraw amount: "))
            print("+{:-<100}+".format(""))

            accountAmount = (
                "SELECT totalAmount FROM USER WHERE accNumber = ?")
            cursor.execute(accountAmount, [(accNumber)])
            currentAmount = cursor.fetchone()
            oldAmount = currentAmount[0]

            if oldAmount > transactionAmount:
                newAmount = oldAmount - transactionAmount

                newTran = '''INSERT INTO MONEY(accNumber, transactionNum,transactionDate,transactionAmount)
                    VALUES ('%s', '%s', '%s', '%s') ''' % (accNumber, transactionNum, transactionDate, transactionAmount)
                cursor.execute(newTran)
                db.commit()

                updateAmount = (
                    "UPDATE USER SET totalAmount =? WHERE accNumber = ?")
                cursor.execute(updateAmount, [(newAmount), (accNumber)])
                db.commit()

                print('\x1b[6;30;42m' +
                      "|{:^100}|".format("SUCCESS")+'\x1b[0m')
                print("+{:-<100}+".format(""))
                print("|{:^100}|".format("You have now: " + str(newAmount)))
                print("+{:-<100}+".format(""))

            else:
                print("+{:-<100}+".format(""))
                print('\x1b[0;37;41m' +
                      "|{:^100}|".format("You don't have enough money to do that")+'\x1b[0m')
                print("+{:-<100}+".format(""))

                again = raw_input("Do you want to try again? (Y/N): ").upper()

                if again != "N":
                    withdraw()
                else:
                    print("+{:-<100}+".format(""))
                    print("|{:^100}|".format("GOOD BYE"))
                    print("+{:-<100}+".format(""))

    else:
        print("+{:-<100}+".format(""))
        print('\x1b[0;37;41m' +
              "|{:^100}|".format("Account doesn't exist")+'\x1b[0m')
        print("+{:-<100}+".format(""))

        again = raw_input("Do you want to try again? (Y/N): ").upper()

        if again != "N":
            withdraw()
        else:
            print("+{:-<100}+".format(""))
            print("|{:^100}|".format("GOOD BYE"))
            print("+{:-<100}+".format(""))


def checkMovements():

    print("+{:-<100}+".format(""))
    print("|{:^100}|".format("BANK MOVEMENTS"))
    print("+{:-<100}+".format(""))

    accNumber = raw_input("Insert account number to check: ")
    findAcc = ("SELECT * FROM USER WHERE accNumber = ?")
    cursor.execute(findAcc, [(accNumber)])

    results = cursor.fetchall()

    if results:
        for i in results:
            print("+{:-<100}+".format(""))
            print("|{:^100}|".format('Welcome: ' + i[1]))
            print("+{:-<100}+".format(""))

            accountMovement = (
                "SELECT * FROM MONEY WHERE accNumber = ?")
            cursor.execute(accountMovement, [(accNumber)])
            movements = cursor.fetchall()
            print(movements)

            """print('\x1b[6;30;42m' + "|{:^100}|".format("SUCCESS")+'\x1b[0m')
            print("+{:-<33}+{:-<32}+{:-<33}+".format("", "", ""))
            print("|{:^33}|{:^32}|{:^33}|".format(
                "Transaction Number", "Transaction Date", "Transaction Amount"))
            print("+{:-<33}+{:-<32}+{:-<33}+".format("", "", ""))
            print("|{:^33}|{:^32}|{:^33}|".format(
                transactionNum, transactionNum, transactionAmount))
            print("+{:-<33}+{:-<32}+{:-<33}+".format("", "", ""))"""

    else:
        print("+{:-<100}+".format(""))
        print('\x1b[0;37;41m' +
              "|{:^100}|".format("Account doesn't exist")+'\x1b[0m')
        print("+{:-<100}+".format(""))

        again = raw_input("Do you want to try again? (Y/N): ").upper()

        if again != "N":
            checkMovements()
        else:
            print("+{:-<100}+".format(""))
            print("|{:^100}|".format("GOOD BYE"))
            print("+{:-<100}+".format(""))


newAccount()
