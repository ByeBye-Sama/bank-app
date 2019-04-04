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
        cursor.execute("INSERT INTO RESERVATION(idCustomer, idBarber, idService, reservationDate, observation) VALUES (" + str(
            idCustomer) + "," + str(idBarber) + "," + str(idService) + "," + "'" + reservationDate + "'," + "'" + observation + "')")
        db.commit()

        print('\x1b[6;30;42m' + "|{:^100}|".format("SUCCESS")+'\x1b[0m')
        print("+{:-<100}+".format(""))
        print("Your reservation code is: ", cursor.lastrowid)
        print("+{:-<100}+".format(""))

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
        print("+{:-<100}+".format(""))

        Reservation.__init__('', idCustomer, idBarber,
                             idService, reservationDate, observation)

    def reservationScore(self):

        print("+{:-<100}+".format(""))
        print("|{:^100}|".format("RESERVATION RECORDS"))
        print("+{:-<100}+".format(""))

        firstDate = input("Insert first date with format (DD/MM/YY): ")
        lastDate = input("Insert first date with format (DD/MM/YY): ")

        print("+{:-<100}+".format(""))
        print('\x1b[6;30;42m' + "|{:^100}|".format("SUCCESS")+'\x1b[0m')

        reservations = "SELECT c.nameCustomer Customer, b.nameBarber Barber, s.nameService Service, r.reservationDate , r.observation FROM RESERVATION r INNER JOIN CUSTOMER c on r.idCustomer=c.idCustomer INNER JOIN BARBER b on r.idBarber=b.idBarber INNER JOIN SERVICE s on r.idService=s.idService WHERE r.reservationDate BETWEEN ? and ?;"
        cursor.execute(reservations, [(firstDate), (lastDate)])
        allreservations = cursor.fetchall()

        print("+{:-<18}+{:-<18}+{:-<18}+{:-<18}+{:-<24}+".format("", "", "", "", ""))
        print("|{:^18}|{:^18}|{:^18}|{:^18}|{:^24}|".format(
            "Customer", "Barber", "Service", "Date", "Observation"))
        print("+{:-<18}+{:-<18}+{:-<18}+{:-<18}+{:-<24}+".format("", "", "", "", ""))

        for Customer, Barber, Service, reservationDate, observation in allreservations:
            print("|{:^18}|{:^18}|{:^18}|{:^18}|{:^24}|".format(
                Customer, Barber, Service, reservationDate, observation))
            print(
                "+{:-<18}+{:-<18}+{:-<18}+{:-<18}+{:-<24}+".format("", "", "", "", ""))
