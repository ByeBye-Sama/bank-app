from random import randint
from colorama import Fore, Back, Style
import sqlite3
import datetime
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
now = datetime.datetime.now()


class Bank():

    def newAccount(self):

        print("+{:-<100}+".format(""))
        print('\x1b[6;30;47m' + "|{:^100}|".format("REGISTER ACOUNT FORM")+'\x1b[0m')
        print("+{:-<100}+".format(""))

        accNumber = input("Insert new account number: ")
        email = input("Insert new email: ")
        bankCode = input("Insert bank code: ")
        totalAmount = int(input("Insert first ammount: "))

        newAcc = '''INSERT INTO USER(accNumber,email,bankCode,totalAmount)
                    VALUES ('%s', '%s', '%s', '%s') ''' % (accNumber, email, bankCode, totalAmount)

        cursor.execute(newAcc)
        db.commit()
        db.close()

        print("+{:-<100}+".format(""))
        print("|{:^100}|".format("NEW USER"))
        print("+{:-<100}+".format(""))
        print('\x1b[6;30;42m' + "|{:^100}|".format("SUCCESS")+'\x1b[0m')

        print("+{:-<22}+{:-<31}+{:-<22}+{:-<22}+".format("", "", "", ""))
        print("|{:^22}|{:^31}|{:^22}|{:^22}|".format(
            "Account Number", "Email", "Bank Code", "Total Amount"))
        print("+{:-<22}+{:-<31}+{:-<22}+{:-<22}+".format("", "", "", ""))

        print("|{:^22}|{:^31}|{:^22}|{:^22}|".format(
            accNumber, email, bankCode, totalAmount))
        print("+{:-<22}+{:-<31}+{:-<22}+{:-<22}+".format("", "", "", ""))

    def deposit(self):

        print("+{:-<100}+".format(""))
        print('\x1b[6;30;47m' + "|{:^100}|".format("DEPOSIT FORM")+'\x1b[0m')
        print("+{:-<100}+".format(""))

        accNumber = input("Insert account number to login: ")
        findAcc = ("SELECT * FROM USER WHERE accNumber = ?")
        cursor.execute(findAcc, [(accNumber)])

        results = cursor.fetchall()

        if results:
            for i in results:
                print("+{:-<100}+".format(""))
                print("|{:^100}|".format('Welcome: ' + i[1]))
                print("+{:-<100}+".format(""))

                transactionType = "Deposit"
                transactionDate = now.strftime('%Y-%m-%d')
                print("Date: " + str(transactionDate))
                print("+{:-<100}+".format(""))
                transactionNum = randint(100000, 999999)
                print("Your transacion number is: " + str(transactionNum))
                print("+{:-<100}+".format(""))
                transactionAmount = int(input("Insert deposit amount: "))
                print("+{:-<100}+".format(""))

                newTran = '''INSERT INTO MONEY(accNumber, transactionNum, transactionType, transactionDate, transactionAmount)
                    VALUES ('%s', '%s', '%s', '%s', '%s') ''' % (accNumber, transactionNum, transactionType, transactionDate, transactionAmount)

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

                print('\x1b[6;30;42m' +
                      "|{:^100}|".format("SUCCESS")+'\x1b[0m')
                print("+{:-<100}+".format(""))
                print("|{:^100}|".format("You have now: " + str(newAmount)))
                print("+{:-<100}+".format(""))

        else:
            print("+{:-<100}+".format(""))
            print('\x1b[0;37;41m' +
                  "|{:^100}|".format("Account doesn't exist")+'\x1b[0m')
            print("+{:-<100}+".format(""))

            again = input("Do you want to try again? (Y/N): ").upper()

            if again != "N":
                Bank.deposit(self)
            else:
                print("+{:-<100}+".format(""))
                print("|{:^100}|".format("GOOD BYE"))
                print("+{:-<100}+".format(""))

    def withdraw(self):

        print("+{:-<100}+".format(""))
        print('\x1b[6;30;47m' + "|{:^100}|".format("WITHDRAW FORM")+'\x1b[0m')
        print("+{:-<100}+".format(""))

        accNumber = input("Insert account number to login: ")
        findAcc = ("SELECT * FROM USER WHERE accNumber = ?")
        cursor.execute(findAcc, [(accNumber)])

        results = cursor.fetchall()

        if results:
            for i in results:
                print("+{:-<100}+".format(""))
                print("|{:^100}|".format('Welcome: ' + i[1]))
                print("+{:-<100}+".format(""))

                transactionType = "Withdraw"
                transactionDate = now.strftime('%Y-%m-%d')
                print("Date: " + str(transactionDate))
                print("+{:-<100}+".format(""))
                transactionNum = randint(100000, 999999)
                print("Your transacion number is: " + str(transactionNum))
                print("+{:-<100}+".format(""))
                transactionAmount = int(input("Insert withdraw amount: "))
                print("+{:-<100}+".format(""))

                accountAmount = (
                    "SELECT totalAmount FROM USER WHERE accNumber = ?")
                cursor.execute(accountAmount, [(accNumber)])
                currentAmount = cursor.fetchone()
                oldAmount = currentAmount[0]

                if oldAmount > transactionAmount:
                    newAmount = oldAmount - transactionAmount

                    newTran = '''INSERT INTO MONEY(accNumber, transactionNum, transactionType ,transactionDate, transactionAmount)
                        VALUES ('%s', '%s', '%s', '%s', '%s') ''' % (accNumber, transactionNum, transactionType, transactionDate, transactionAmount)
                    cursor.execute(newTran)
                    db.commit()

                    updateAmount = (
                        "UPDATE USER SET totalAmount =? WHERE accNumber = ?")
                    cursor.execute(updateAmount, [(newAmount), (accNumber)])
                    db.commit()

                    print('\x1b[6;30;42m' +
                          "|{:^100}|".format("SUCCESS")+'\x1b[0m')
                    print("+{:-<100}+".format(""))
                    print("|{:^100}|".format(
                        "You have now: " + str(newAmount)))
                    print("+{:-<100}+".format(""))

                else:
                    print("+{:-<100}+".format(""))
                    print('\x1b[0;37;41m' +
                          "|{:^100}|".format("You don't have enough money to do that")+'\x1b[0m')
                    print("+{:-<100}+".format(""))

                    again = input("Do you want to try again? (Y/N): ").upper()

                    if again != "N":
                        Bank.withdraw(self)
                    else:
                        print("+{:-<100}+".format(""))
                        print("|{:^100}|".format("GOOD BYE"))
                        print("+{:-<100}+".format(""))

        else:
            print("+{:-<100}+".format(""))
            print('\x1b[0;37;41m' +
                  "|{:^100}|".format("Account doesn't exist")+'\x1b[0m')
            print("+{:-<100}+".format(""))

            again = input("Do you want to try again? (Y/N): ").upper()

            if again != "N":
                Bank.withdraw(self)
            else:
                print("+{:-<100}+".format(""))
                print("|{:^100}|".format("GOOD BYE"))
                print("+{:-<100}+".format(""))

    def checkMovements(self):

        print("+{:-<100}+".format(""))
        print('\x1b[6;30;47m' + "|{:^100}|".format("BANK MOVEMENTS")+'\x1b[0m')
        print("+{:-<100}+".format(""))

        accNumber = input("Insert account number to check: ")
        findAcc = ("SELECT * FROM USER WHERE accNumber = ?")
        cursor.execute(findAcc, [(accNumber)])
        results = cursor.fetchall()

        accountAmount = ("SELECT totalAmount FROM USER WHERE accNumber = ?")
        cursor.execute(accountAmount, [(accNumber)])
        currentAmount = cursor.fetchone()
        allAmount = currentAmount[0]


        if results:
            for i in results:
                print("+{:-<100}+".format(""))
                print("|{:^100}|".format('Welcome: ' + i[1]))
                print("+{:-<100}+".format(""))

               
                accountMovement = (
                    "SELECT transactionNum, transactionType, transactionDate, transactionAmount FROM MONEY WHERE accNumber = ? ORDER BY transactionDate DESC")
                cursor.execute(accountMovement, [(accNumber)])
                movements = cursor.fetchall()

                print('\x1b[6;30;42m' +
                      "|{:^100}|".format("SUCCESS")+'\x1b[0m')
                print("+{:-<100}+".format(""))
                print("|{:^100}|".format("LIFE SAVINGS: " + str(allAmount)))
                    

                print("+{:-<24}+{:-<24}+{:-<25}+{:-<24}+".format("", "", "", ""))
                print("|{:^24}|{:^24}|{:^25}|{:^24}|".format(
                    "Transaction Number", "Transaction Type", "Transaction Date", "Transaction Amount"))
                print("+{:-<24}+{:-<24}+{:-<25}+{:-<24}+".format("", "", "", ""))

                for transactionNum, transactionType, transactionDate, transactionAmount in movements:
                    print("|{:^24}|{:^24}|{:^25}|{:^24}|".format(
                        transactionNum, transactionType, transactionDate, transactionAmount))
                    print(
                        "+{:-<24}+{:-<24}+{:-<25}+{:-<24}+".format("", "", "", ""))

        else:
            print("+{:-<100}+".format(""))
            print('\x1b[0;37;41m' +
                  "|{:^100}|".format("Account doesn't exist")+'\x1b[0m')
            print("+{:-<100}+".format(""))

            again = input("Do you want to try again? (Y/N): ").upper()

            if again != "N":
                Bank.checkMovements(self)
            else:
                print("+{:-<100}+".format(""))
                print("|{:^100}|".format("GOOD BYE"))
                print("+{:-<100}+".format(""))
