// Escribir un programa que pida al usuario dos números y los sume. ¡Pero esta vez hazlo en C++! :)

#include <iostream>
using namespace std;
int main () {
    // Declarar dos variables para almacenar los números ingresados por el usuario
    int num1, num2;
 
    // Pedir al usuario que ingrese el primer número
    cout << "Ingrese un numero: ";
    cin >> num1; // Lee el primer numero y lo almacena en num1 

    // Pedir al usuario que ingrese el segundo número
    cout << "Ingrese el siguiente numero: ";
    cin >> num2; // Lee el segundo numero y lo almacena en num2

    // Sumar los dos numeros
    int suma = num1 + num2;

    //  // Mostrar el resultado de la suma
    cout << "La suma de " << num1 << " y " << num2 << " es: " << suma << endl;
    return 0;
}