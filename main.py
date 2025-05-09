#Módulos
from programas.sumas import sumar2
from programas.restas import resta2
from vistas.menu import menu
from vistas.lineas import cargar_lineas
from datetime import datetime

#Módulos de Python
import os
import time

while True:
    os.system("clear")  # En Windows usa "cls"
    print("Hora actual:", datetime.now().strftime("%H:%M:%S"))
    time.sleep(1)

programa = True 


while(programa):    
    cargar_lineas(50)
    menu()
    
    res = int(input("[?] "))
    
    if res == 1:
         print("[Sumar dos números]")
         sumar2()
    elif res == 2:
        print("[Restar dos números]")
        resta2()
    elif res == 0:
        print("Salir de programa")
        programa = False
        
    os.system("clear")
