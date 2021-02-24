####################
# github.com/acexe #
####################


import sys
import socket
import platform
import webbrowser
import os
import time
from colorama import *

sistema = platform.system()

if sistema == 'Windows':
    os.system("cls")
else:
    os.system("clear")

while True:
    init()
    print(Fore.GREEN+'''
┏━━━┳━━━┳━━━┳━┓┏━┳━━━┓
┃┏━┓┃┏━┓┃┏━━┻┓┗┛┏┫┏━━┛
┃┃╋┃┃┃╋┗┫┗━━┓┗┓┏┛┃┗━━┓
┃┗━┛┃┃╋┏┫┏━━┛┏┛┗┓┃┏━━┛
┃┏━┓┃┗━┛┃┗━━┳┛┏┓┗┫┗━━┓
┗┛╋┗┻━━━┻━━━┻━┛┗━┻━━━┛''')
    print("   code by acexe"+Fore.RESET)
    print("\n")

    print("[1] Mandar SMS anonimos")
    print("[2] Escanear puertos")
    print("[3] Salir")
    print("\n")

    opcion = int(input("Ingresa opcion: "))

    if opcion == 1:
        if sistema == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
            
        print(Fore.RED+"------------------------------------------------------------------------------")
        print("- En la siguiente pagina que se abrira puedes mandar SMS totalmente anonimos -")
        print("------------------------------------------------------------------------------"+Fore.RESET)
        
        time.sleep(1)
        webbrowser.open_new("https://www.afreesms.com/freesms/")
        print("\n")

        print("[1] Repetir proceso")
        print("[2] salir")

        op_1 = int(input("Ingresa respuesta: "))
        
        if op_1 == 1:
            print("Rpitiendo")
            if sistema == 'Windows':
                os.system("cls")
            else:
                os.system("clear")
        else:
            if sistema == 'Windows':
                os.system("cls")
            else:
                os.system("clear")
            print(Fore.RED+"------------")
            print("- SALIENDO -")
            print("------------"+Fore.RESET)
            time.sleep(1)
            break

    elif opcion == 2:
        if sistema == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
        print(Fore.GREEN+"-----------------------")
        print("- ESCANER DE PUERTOS  -")
        print("-----------------------"+Fore.RESET)
        print("\n")

        objetivo = socket.gethostbyname(input("Introduce IP: "))
        print("Escanenado objetivo: " + objetivo)
        try:
            for port in range(1,150):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                resultado = s.connect_ex((objetivo, port))
                if resultado == 0:
                    print("El puerto {} esta abierto".format(port))
                s.close()
        except:
            print("\n Saliendo...")
            sys.exit(0)

        print("[1] repetir procesos")
        print("[2] salir")
        op_2 = int(input("Ingresa opcion: "))
        if op_2 == 1:
            print("Repitiendo")
            if sistema == 'Windows':
                os.system("cls")
            else:
                os.system("clear")
        else:
            print("Saliendo")
            time.sleep(2)
            break

    elif opcion == 3:
        if sistema == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
        print(Fore.RED+"------------")
        print("- SALIENDO -")
        print("------------"+Fore.RESET)
        time.sleep(2)
        break

    else:
        if sistema == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
        print(Fore.RED+"------------------------")
        print("- OPCION NO DISPONIBLE -")
        print("------------------------"+Fore.RESET)
        time.sleep(1)
        if sistema == 'Windows':
            os.system("cls")
        else:
            os.system("clear")
