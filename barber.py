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


class Barber:

    nameBarber = ''
    mailBarber = ''

    def __init__(self, nameBarber, mailBarber):

        self.nameBarber = nameBarber
        self.mailBarber = mailBarber

    def barberList(self):

        barbers = "SELECT nameBarber,mailBarber FROM BARBER;"
        cursor.execute(barbers)
        allBarbers = cursor.fetchall()

        print("+{:-<100}+".format(""))
        print("|{:^100}|".format("BARBERS LIST"))
        print("+{:-<100}+".format(""))
        print('\x1b[6;30;42m' + "|{:^100}|".format("SUCCESS")+'\x1b[0m')
       

        print("+{:-<50}+{:-<49}+".format("", ""))
        print("|{:^50}|{:^49}|".format("Name", "Email"))
        print("+{:-<50}+{:-<49}+".format("", ""))

        for nameBarber, mailBarber in allBarbers:
            print("|{:^50}|{:^49}|".format(nameBarber, mailBarber))
            print("+{:-<50}+{:-<49}+".format("", ""))



