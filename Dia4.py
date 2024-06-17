# Ordenar Lista: Escribe un programa que ordene una lista de números dada por el usuario en orden ascendente.

# Paso 1: Recibir la lista del usuario
datos_usuario = input("Ingrese una lista de numeros separados CON ESPACIOS para ordenarlos: ")

# Paso 2: Hacer que los datos ingresados por el usuario se separen uno del otro
numero_usuario = datos_usuario.split()

# Paso 3: Convertir la cadena de entrada en una lista de números enteros
numero_usuario = [int(num) for num in numero_usuario]

# Paso 4: Ordenar la lista
numero_usuario.sort()

# Paso 5: Mostrar la lista ya ordenada
print("Lista Ordenada: ", numero_usuario)