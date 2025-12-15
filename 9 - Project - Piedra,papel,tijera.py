# Proyecto Basico de fundamentos de Programacion
# Piedra, Papel o Tijera
# Jonatan Osiris Gonzalez Ibarra

import time 
import os 
import random 

def limpiarpantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Hola usuario, mucho gusto de que estes aqui")
print("Estas listo para poder iniciar este programa?")
input("Presiona Enter para continuar...")
limpiarpantalla()

print("Este programa es un juego de Piedra, Papel o Tijera\n" \
"vas a jugar contra la computadora, asi que mucha suerte")
time.sleep(3)
limpiarpantalla()


Opciones = ["Piedra", "Papel", "Tijera"]
eleccion_computadora = random.choice(Opciones)
eleccion_usuario = input("Elige Piedra, Papel o Tijera: \n")
limpiarpantalla()
print(f"La computadora eligio: {eleccion_computadora}")
time.sleep(1)

if eleccion_usuario == eleccion_computadora:
    print("Es un empate!")
elif (eleccion_usuario == "Piedra" and eleccion_computadora == "Tijera") or \
     (eleccion_usuario == "Papel" and eleccion_computadora == "Piedra") or \
     (eleccion_usuario == "Tijera" and eleccion_computadora == "Papel"):
    print("Felicidades, ganaste!")
else:
    print("Lo siento, la computadora gano!")