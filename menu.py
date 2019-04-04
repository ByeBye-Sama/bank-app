from reservation import Reservation
from services import Services
from customer import Customer
from barber import Barber
from colorama import Fore, Back, Style
import os
import os.path
import time
from colorama import init
init()


asw = ""


def barberMenu():
    option = "0"
    print("+{:-<50}+".format(""))
    print('\x1b[6;30;47m' + "|{:^50}|".format("Barbershop System")+'\x1b[0m')
    print("+{:-<50}+".format(""))
    print('\x1b[1;32;40m' + "|{:50}|".format("1. Barbers' list")+'\x1b[0m')
    print("+{:-<50}+".format(""))
    print('\x1b[1;33;40m' + "|{:50}|".format("2. Customers' list")+'\x1b[0m')
    print("+{:-<50}+".format(""))
    print('\x1b[1;34;40m' + "|{:50}|".format("3. Services' list")+'\x1b[0m')
    print("+{:-<50}+".format(""))
    print('\x1b[1;35;40m' +
          "|{:50}|".format("4. Make reservation")+'\x1b[0m')
    print("+{:-<50}+".format(""))
    print('\x1b[1;36;40m' +
          "|{:50}|".format("5. Reservations record")+'\x1b[0m')
    print("+{:-<50}+".format(""))
    time.sleep(2)
    option = input("Choose one option: ")
    print("+{:-<50}+".format(""))
    time.sleep(2)
    if option == "1":
        Barber.barberList("")
    elif option == "2":
        Customer.customerList("")
    elif option == "3":
        Services.serviceList("")
    elif option == "4":
        Reservation.makeReservation("")
    elif option == "5":
        Reservation.reservationScore("")
    else:
        print("+{:-<50}+".format(""))
        print('\x1b[0;37;41m' +
              "|{:^50}|".format("Option doesn't exist")+'\x1b[0m')
        print("+{:-<50}+".format(""))
        exit


def initAll():
    barberMenu()
    asw = input("Do you want to continue? (Y/N): ").upper()

    while asw == 'Y':
        os.system('cls')
        initAll()

    if asw == 'N':
        print("+{:-<50}+".format(""))
        print('\x1b[6;30;43m' +
              "|{:^50}|".format("Thanks for use this program")+'\x1b[0m')
        print("+{:-<50}+".format(""))
        time.sleep(2)
        exit

    else:
        print("+{:-<50}+".format(""))
        print('\x1b[0;37;41m' +
              "|{:^50}|".format("Option doesn't exist")+'\x1b[0m')
        print("+{:-<50}+".format(""))
        time.sleep(2)
        initAll()


initAll()
