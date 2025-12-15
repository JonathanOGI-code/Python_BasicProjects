# Registro de usuarios
# Jonathan Osiris Gonzalez Ibarra
# Proyectos Basicos
import time
import os

def pausa_cargando(segundos=2, mensaje="Cargando..."):
    print(mensaje)
    time.sleep(segundos)
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa_y_limpieza(segundos=2):
    time.sleep(segundos)
    os.system('cls' if os.name == 'nt' else 'clear')
pausa_y_limpieza()
print("Hola usuario, ahorita mismo te explicaremos para que funcionara esta aplicacion")
pausa_cargando()
print("la aplicacion es sencilla en todos los aspectos, basicamente es un contador de vocales de palabras\n" \
"basicamente no tiene mucha ciencia, escribes la palabra y te contare las vocales...")
input("presiona enter para confirmar...")
pausa_y_limpieza()

vocales = "aeiouAEIOU"
palabra = input("Ingresa la oracion completa: ")
contador = 0

for i in palabra:
    if i in vocales:
        contador+=1
pausa_cargando(mensaje="Contando vocales...")
print(f"La cantidad de vocales en la oracion es: {contador}")
pausa_y_limpieza()
print("Gracias por usar la aplicacion, hasta luego!")

