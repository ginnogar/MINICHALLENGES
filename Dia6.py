# Conversión de Temperatura: Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit.

#Paso 1: Pedir al usuario que ingrese un valor de temperatura en grado celsius
grado_celsius = float(input("Ingrese el valor de temperatura en grado celsius: ")) 

#Paso 2: Realizar la conversion a Farenheit 
farenheit = (grado_celsius * 9/5) + 32

#Paso 3: Mostrar el resultado
print(f'{grado_celsius} en grado Farenheit es {farenheit} F°')
