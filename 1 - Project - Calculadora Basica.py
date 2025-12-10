# Calculadora basica
# Jonathan Osiris Gonzalez Ibarra
# Proyectos Basicos

import time 
print("Mucho gusto usuario, a continuacion te daremos una explicacion determinada sobre como funciona la aplicacion...")
print("Cargando...")
time.sleep(3)  # Espera 3 segundos
nombre = input("Ahora si usuario, dime ¿Cual es tu nombre?\n")
print("Cargando...")
time.sleep(3)
print(f"Bueno {nombre}, la aplicacion es una calculadora basica, solamenente se te daran las numeros para que tu puedas\ncual de las decisiones quieres que tome la app...")
print("Acciones de la calculadora basica" \
"\n1. Suma" \
"\n2. Resta" \
"\n3. Multipicacion" \
"\n4. Division")
print("Cargando...")
time.sleep(2)

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

num3 = int(input("Ahora ingrese la accion que quiera realizar con esos dos numeros: "))

if num3 == 1:
    print(num1 + num2)
elif num3 == 2:
    print(num1-num2)
elif num3 == 3:
    print(num1*num2)
elif num3 == 4:
    print(num1/num2)
else:
    print("El numero que ingresaste es incorrecto...")