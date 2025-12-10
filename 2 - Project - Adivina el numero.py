# Adivina el numero 
# Jonathan Osiris Gonzalez Ibarra
# Proyectos Basicos

import time
import os
import random as rm 

def limpiarpantalla():
    os.system('cls' if os.name == 'nt' else 'clear')



print("Hola usuario, mucho gusto, este sera tu nueva travecia usando esta aplicacion..")
time.sleep(2)
print("Por ahora te diremos todo lo que tienes que hacer para que entiendas la aplicacion")
time.sleep(2)
limpiarpantalla()
print("Esta aplicacion es para adivina el numero, tendras un numero el cual tu tendras que adivinar\n"
"por ahora, sera un numero del 1 - 10 para que sea mas sencillo de adivinar...")
input("Presiona Enter para continuar...")
limpiarpantalla()


numero = rm.randint(1,10)
num1 = int(input("ingrese el numero que piensas que es: "))

if num1 == numero:
    print("Cargando...")
    time.sleep(2)
    print("Felicidades le atinaste")
    time.sleep(2)
    limpiarpantalla()
    
else:
    print("Cargando...")
    time.sleep(2)
    print(f"el numero era {numero}")
    print("Suerte para la proxima..")
    time.sleep(2)
    limpiarpantalla()










