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


class Services:

    nameService = ''
    priceService = ''

    def __init__(self, nameService, priceService):

        self.nameService = nameService
        self.priceService = priceService

    def serviceList(self):

        services = "SELECT nameService,priceService FROM SERVICE;"
        cursor.execute(services)
        allServices = cursor.fetchall()

        print("+{:-<100}+".format(""))
        print("|{:^100}|".format("SERVICE LIST"))
        print("+{:-<100}+".format(""))
        print('\x1b[6;30;42m' + "|{:^100}|".format("SUCCESS")+'\x1b[0m')
       

        print("+{:-<50}+{:-<49}+".format("", ""))
        print("|{:^50}|{:^49}|".format("Name", "Price"))
        print("+{:-<50}+{:-<49}+".format("", ""))

        for nameService, priceService in allServices:
            print("|{:^50}|{:^49}|".format(nameService, priceService))
            print("+{:-<50}+{:-<49}+".format("", ""))
