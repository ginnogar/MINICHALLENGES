caracteres = input("Ingrese una palabra: ") # Solicita al usuario que escriba una palabra

def invertir_caracteres(cadena_de_caracteres): # Define la función invertir_caracteres que toma una cadena como 
    # argumento.
    if len(cadena_de_caracteres) == 0: # Verifica si la longitud de la cadena es 0.
        return "" # Si es así, retorna una cadena vacía. 
    else: # Si la cadena no está vacía
        return cadena_de_caracteres[-1] + invertir_caracteres(cadena_de_caracteres[:-1]) # Retorna el último 
    # carácter de la cadena más la llamada recursiva de la función con la cadena sin el último carácter.

# Llama a la funcion invertir_caracteres con la cadena ingresada por el usuario
resultado = invertir_caracteres(caracteres)

#Imprime el resultado
print(resultado)

