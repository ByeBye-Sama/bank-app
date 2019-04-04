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


class Reservation:

    idCustomer = 0
    idBarber = 0
    idService = 0
    reservationDate = ""
    observation = ""

    def __init__(self, idCustomer, idBarber, idService, reservationDate, observation):
        try:
            cursor.execute("INSERT INTO RESERVATION(idCustomer, idBarber, idService, reservationDate, observation) VALUES (" + str(
                idCustomer) + "," + str(idBarber) + "," + str(idService) + "," + "'" + reservationDate + "'," + "'" + observation + "')")
            db.commit()
            print("Your reservation code is: ", cursor.lastrowid)
        except sqlite3.IntegrityError as e:
            print('sqlite error', e.args[0])

    def makeReservation(self):

        print("+{:-<100}+".format(""))
        print("|{:^100}|".format("MAKE A RESERVATION"))
        print("+{:-<100}+".format(""))

        idCustomer = int(input("Insert customer number: "))
        print("+{:-<100}+".format(""))
        idBarber = int(input("Insert barber number: "))
        print("+{:-<100}+".format(""))
        idService = int(input("Insert services number: "))
        print("+{:-<100}+".format(""))
        reservationDate = input("Insert reservation date: ")
        print("+{:-<100}+".format(""))
        observation = input("Insert observations: ")

        Reservation.__init__('', idCustomer, idBarber,
                             idService, reservationDate, observation)
