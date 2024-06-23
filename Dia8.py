# Generador de Contraseñas Seguras: Escribe un programa que genere una contraseña segura de longitud variable 
# (entre 8 y 16 caracteres) que incluya letras mayúsculas, minúsculas, números y símbolos.

import random
import string

def generar_contraseña():
    # Longitud aleatoria entre 8 y 16
    longitud = random.randint(8, 16)

    # Conjuntos de caracteres
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation

    # Asegurarse de incluir al menos un carácter de cada tipo
    contraseña = [
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    # Llenar el resto de la contraseña con caracteres aleatorios
    todos_caracteres = mayusculas + minusculas + numeros + simbolos
    contraseña += random.choices(todos_caracteres, k=longitud - 4)

    # Mezclar la contraseña para que los caracteres iniciales no estén siempre en el mismo orden
    random.shuffle(contraseña)

    # Unir la lista de caracteres en una sola cadena
    return ''.join(contraseña)

# Mensaje inicial
input("Dale Enter para generar tu contraseña :)")

# Generar y mostrar la contraseña
contraseña = generar_contraseña()
print("¡Tu contraseña segura es 😎!: ", contraseña)
