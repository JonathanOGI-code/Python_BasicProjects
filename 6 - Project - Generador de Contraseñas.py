# Generador de Contraseñas
# Jonathan Osiris Gonzalez Ibarra
# Proyectos Basicos

import time 
import os 
import random 

def limpiarpantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa_cargando(segundos=2, mensaje="Cargando..."):
    print(mensaje)
    time.sleep(segundos)
    limpiarpantalla()

limpiarpantalla()
print("--------------------------------------------------------------------")
print("Hola usuario, bienvenido al generador de contraseñas...            |" \
"\nEn esta aplicacion u me diras la cantidad de caracteres que deseas |" \
"\npara generar una contraseña aleatoria y lo mas segura posible      |") 
print("--------------------------------------------------------------------\n\n\n")

pausa_cargando()
tamaño = int(input("Ingresa la cantidad de caracteres que quieres para poder generar la contraseña:\n"))
pausa_cargando(mensaje="Generando contraseña...")
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
contraseña = "".join(random.sample(caracteres, tamaño))
print(f"\n\nTu contraseña generada es: {contraseña}\n\n")