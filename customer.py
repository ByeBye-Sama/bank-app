from colorama import Fore, Back, Style
import sqlite3
import os
import os.path
import time
from colorama import init
init()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "barber-store.db")
db = sqlite3.connect(db_path)
cursor = db.cursor()
asw = ""


class Customer:

    nameBarber = ''
    mailBarber = ''

    def __init__(self, nameCustomer, cellCustomer, mailCustomer):

        self.nameCustomer = nameCustomer
        self.cellCustomer = cellCustomer
        self.mailCustomer = mailCustomer

    def customerList(self):

        customers = "SELECT nameCustomer, cellCustomer, mailCustomer FROM CUSTOMER;"
        cursor.execute(customers)
        allCustomers = cursor.fetchall()

        print("+{:-<100}+".format(""))
        print("|{:^100}|".format("CUSTOMERS LIST"))
        print("+{:-<100}+".format(""))
        print('\x1b[6;30;42m' + "|{:^100}|".format("SUCCESS")+'\x1b[0m')
      

        print("+{:-<33}+{:-<32}+{:-<33}+".format("", "", ""))
        print("|{:^33}|{:^32}|{:^33}|".format("Name", "Cellphone", "Email"))
        print("+{:-<33}+{:-<32}+{:-<33}+".format("", "", ""))

        for nameCustomer, cellCustomer, mailCustomer in allCustomers:
            print("|{:^33}|{:^32}|{:^33}|".format(
                nameCustomer, cellCustomer, mailCustomer))
            print("+{:-<33}+{:-<32}+{:-<33}+".format("", "", ""))
