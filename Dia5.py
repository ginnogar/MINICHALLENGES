# Crear un Diccionario: Escribe un programa que cree un diccionario a partir de dos listas dadas: 
# una de claves y otra de valores.

#Pedirle al usuario las claves y los valores
clave_usuario = input("Ingrese las claves separas por espacios: ")
valor_usuario = input("Ingrese los valores separados por espacios: ")

# Convertir las cadenas de entrada en listas
claves = clave_usuario.split()
valores = valor_usuario.split()

# Crear el diccionario 
diccionario = {}
for i in range(len(claves)):
    diccionario[claves[i]] = valores [i]

# Mostrar el diccionario
print("Diccionario creado: ", diccionario)
