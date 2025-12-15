# Proyecto Basico de fundamentos de Programacion
# Sistema de Calificaciones
# Jonatan Osiris Gonzalez Ibarra

import time 
import os 


def limpiarpantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Hola usuario, mucho gusto de que estes aqui")
print("Estas listo para poder iniciar este programa?")
input("Presiona Enter para continuar...")
limpiarpantalla()

print("Este programa es un sistema de calificaciones, basicamente tu me diras las calificaciones\n" \
"y yo te dire cual es tu promedio y si aprobaste o no la materia")
time.sleep(3)
limpiarpantalla()

cantidad= int(input("Ingrese la cantidad de calificaciones que desea promediar:\n"))
calificaciones = 0

for i in range(cantidad):
    print(f"\n-- Calificacion{i+1}--\n")
    calificacion = float(input("Calificacion: "))
    calificaciones += calificacion

promedio = calificaciones / cantidad
limpiarpantalla()
print(f"Tu promedio es: {promedio:.2f}")