# Proyecto Basico de fundamentos de Programacion
# Tablas de Multiplicar
# Jonatan Osiris Gonzalez Ibarra

import time 
import os 

def limpiarpantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Hola usuario, mucho gusto de que estes aqui")
print("Estas listo para poder iniciar este programa?")
input("Presiona Enter para continuar...")
limpiarpantalla()
print("Este programa te ayudara a generar las tablas de multiplicar que tu quieras\n" \
"solo tienes que decirme la tabla que quieres y hasta que numero quieres que te la genere")
time.sleep(3)   
limpiarpantalla()

tabla = int(input("Ingrese la tabla de multiplicar que desea generar: \n"))
hasta = int(input("Ingrese hasta que numero desea que se genere la tabla: \n"))
limpiarpantalla()

for i in range(1, hasta + 1):
    resultado = [i * tabla ]
    print(f"{tabla} x {i} = {resultado}")
    time.sleep(0.5)
print("\nGracias por usar este programa, espero haberte ayudado")

