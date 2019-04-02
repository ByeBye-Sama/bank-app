import sqlite3
import os
import os.path
import time

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
    accNumber = raw_input("Insert new account number: ")
    email = raw_input("Insert new email: ")
    bankCode = raw_input("Insert bank code: ")
    totalAmount = int(raw_input("Insert first ammount: "))

    newAcc = '''INSERT INTO USER(accNumber,email,bankCode,totalAmount)
                VALUES ('%s', '%s', '%s', '%s') ''' % (accNumber, email, bankCode, totalAmount)

    cursor.execute(newAcc)
    db.commit()
    db.close()

    print("+{:-<30}+{:-<50}+{:-<30}+{:-<30}+".format("", "", "", ""))
    print("|{:^143}|".format("NEW USER"))

    print("+{:-<30}+{:-<50}+{:-<30}+{:-<30}+".format("", "", "", ""))
    print("|{:^30}|{:^50}|{:^30}|{:^30}|".format(
        "Account Number", "Email", "Bank Code", "Total Amount"))
    print("+{:-<30}+{:-<50}+{:-<30}+{:-<30}+".format("", "", "", ""))

    print("|{:^30}|{:^50}|{:^30}|{:^30}|".format(
        accNumber, email, bankCode, totalAmount))
    print("+{:-<30}+{:-<50}+{:-<30}+{:-<30}+".format("", "", "", ""))


def deposit():
    accNumber = raw_input("Insert account number to login: ")
    findAcc = ("SELECT * FROM USER WHERE accNumber = ?")
    cursor.execute(findAcc, [(accNumber)])

    results = cursor.fetchall()

    if results:
        for i in results:
            print('Welcome: ' + i[1])
            transactionDate = raw_input("Insert date: ")
            transactionNum = int(raw_input("Insert transaction number: "))
            transactionAmount = int(raw_input("Insert deposit amount: "))

            newTran = '''INSERT INTO MONEY(transactionNum,transactionDate,transactionAmount)
                VALUES ('%s', '%s', '%s') ''' % (transactionNum, transactionDate, transactionAmount)

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

            print("")
            print("You have now: " + str(newAmount))

    else:
        print("Account doesn't exist")
        again = raw_input("Do you want to try again? (Y/N): ").upper()
        if again != "N":
            deposit()


def test():
    newAmount = 600
    updateAmount = (
        "UPDATE USER SET totalAmount =? where accNumber = 678")
    cursor.execute(updateAmount, [(newAmount)])
    db.commit()


deposit()
