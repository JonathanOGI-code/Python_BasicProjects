# Conversor de Unidades
# Jonathan Osiris Gonzalez Ibarra
# Proyectos Basicos

import time
import os



def limpiarpantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Hola usuario, ahorita mismo te explicare como usaras esta aplicacion..")
print("Cargando...")
time.sleep(2)
limpiarpantalla()

print("Esta aplicacion sirve para que puedas hacer conversion de unidades, dependiendo el tipo de unidad que quieras cambiar sera este programa: \n" \
"1. Metros a Kilometros" \
"\n2. Grados Celsius a Fahrenheit" \
"\n3. Pesos a Dolares")

numero = float(input("\n\nIngresa el numero a cambiar: "))
Seleccion = int(input("Ingresa la conversion que quieres hacer: "))
time.sleep(2)
limpiarpantalla()
if Seleccion == 1:
    print(f"La converion seria {numero/1000} Kilometros")
    time.sleep(2)
    limpiarpantalla()
elif Seleccion == 2:
    print(f"La conversion seria {(numero * 9 /5) + 32} grados fahrenheit")
    time.sleep(2)
    limpiarpantalla()
elif Seleccion == 3:
    print(f"La conversion seria {float(input('Pesos: ')) / 17} dolares")
    time.sleep(2)
    limpiarpantalla()
else:
    print("Opción no válida")
    time.sleep(2)
    limpiarpantalla()

print("Eso seria todo, gracias por su tiempo...")
time.sleep(2)
limpiarpantalla()
print("Hasta pronto..")
time.sleep(2)
limpiarpantalla()