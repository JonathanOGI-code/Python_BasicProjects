# Registro de usuarios
# Jonathan Osiris Gonzalez Ibarra
# Proyectos Basicos
import time 
import os 

def limpiarpantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

usuarios = []
cantidad = int(input("¿cuantos usuarios deseas ingresar?\n"))
time.sleep(2)
limpiarpantalla()
for i in  range(cantidad):
    print(f"\n--usuario{i+1}--")
    nombre = input("Ingrese el nombre: ")
    edad   = input("Ingrese la edad: ")
    correo = input("ingresa tu correo electronico: ")
    limpiarpantalla()

    usuario = {
        
        "nombre":nombre,
        "edad":edad,
        "correo":correo
    }

    usuarios.append(usuario)

print("La cantidad de usuarios ya fue terminada\n\n")

for u in usuarios:
    print(f"Nombre: {u['nombre']} | Edad: {u['edad']} | Correo: {u['correo']}")
