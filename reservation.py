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

def makeReservation():

    print("+{:-<100}+".format(""))
    print("|{:^100}|".format("MAKE A RESERVATION"))
    print("+{:-<100}+".format(""))

    idCustomer = int(input("Insert customer number: "))
    print("+{:-<100}+".format(""))
    idBarber = int(input("Insert barber number: "))
    print("+{:-<100}+".format(""))
    idServices = int(input("Insert services number: "))
    print("+{:-<100}+".format(""))
    reservationDate = input("Insert date: ")
    print("+{:-<100}+".format(""))
    observation = input("Insert observations: ")

    newRev = '''INSERT INTO USER(idCustomer,idBarber,idService,reservationDate,observation)
                VALUES ('%s', '%s', '%s', '%s', '%s') ''' % (idCustomer, idBarber, idServices, reservationDate, observation)

    cursor.execute(newRev)
    db.commit()
    db.close()