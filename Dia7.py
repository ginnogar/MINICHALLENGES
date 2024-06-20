# Juego de Piedra, Papel o Tijeras: Escribe un programa que permita al usuario jugar piedra, papel o tijeras contra la computadora.
import random 

# Paso 1: Recibir la elección del usuario
jugada_usuario = input("Ingrese su jugada (piedra, papel o tijera): ").lower()

# Paso 2: Generar la eleccion de la computadora
opciones = ["piedra", "papel", "tijera"]
computadora =  random.choice(opciones)

# Paso 3: Determinar quien gana
if jugada_usuario == computadora:
    resultado = "Es un empate"

elif (jugada_usuario == "piedra" and computadora == "tiijera") or \
     (jugada_usuario == "papel" and computadora == "piedra") or \
     (jugada_usuario == "tijera" and computadora == "papel"):
    resultado = "¡Ganaste!"
else:
    resultado = "La computadora gana"

# Paso 4: Mostrar quien gano
print(f'Tu elegiste: {jugada_usuario}')
print(f'Computadora eligio: {computadora}')
print(resultado)