# Proyecto Basico de fundamentos de Programacion
#  Lista de Tareas
# Jonatan Osiris Gonzalez Ibarra


import time 
import os 

def limpiarpantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Hola usuario, mucho gusto de que estes aqui")
print("Estas listo para poder iniciar este programa?")
input("Presiona Enter para continuar...")
limpiarpantalla()
print("Este programa es una lista de tareas, basicamente es simple, me diras la cantidad de cosas que tienes\n" \
"que hacer y yo mismo te la dare ordenada")
time.sleep(3)
limpiarpantalla()

tareas = []

cantidad = int(input("Ingrese la cantidad de tareas que quiere guardar aqui:\n"))

for i in range(cantidad):
    print(f"-- Tarea {i+1}--")
    tarea = input("Tarea: ")
    materia = input("Materia: ")
    fecha = input("Fecha de entrega: ")

    tarea = {

        "Tarea":tarea,
        "Materia":materia,
        "Fecha":fecha

    }

    tareas.append(tarea)

print("Tus tareas son las siguientes:\n")
for tarea in tareas:    
    print(f"Tarea: {tarea['Tarea']} | Materia: {tarea['Materia']} | Fecha de entrega: {tarea['Fecha']}")

print("\nGracias por usar este programa, espero haberte ayudado")
