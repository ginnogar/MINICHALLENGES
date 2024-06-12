# Tabla de Multiplicar: Escribe un programa que muestre la tabla de multiplicar de un número dado por el usuario.

# Solicitar al usuario que escriba un numero 
num_usuario = int(input("Ingrese un numero para crear su tabla de multiplicar: "))

# Generar la tabla de multiplicar
for i in range (1,11): # Iniciar un bucle que va desde 1 hasta 10 (incluyendo el 10)
    resultado = num_usuario * i # Multiplicar el número del usuario por el valor actual de 'i' en una variable resultado
    # Mostrar el resultado de la multiplicación en el formato: número x i = resultado
    print(f'{num_usuario} x {i} = {resultado}')
    