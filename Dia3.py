# Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.

# Paso 1: Pedir al usuario que ingrese una palabra para ver cuantas vocales tiene
palabra_usuario = input("Ingrese una palabra para ver cuantas vocales tiene: ")
# Paso 2: Crear una variable para almacenar las vocales
vocales = "aeiouAEIOU"
#Paso 3: Crear una funcion para contar las vocales
def contar_vocales(palabra):
    contador_vocales = 0
    for letra in palabra:
        if letra in vocales:
            contador_vocales += 1
    return contador_vocales
# Paso 4: Llamar a la función y mostrar el resultado
numero_de_vocales = contar_vocales(palabra_usuario)
print(f'El numero de vocales que tiene la palabra es: {numero_de_vocales}')
