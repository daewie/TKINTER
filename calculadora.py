import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("Error: No se puede dividir por cero.")
        return None
    else:
        return a / b

def potenciacion(a, b):
    return a ** b

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def raiz_cuadrada(n):
    if n < 0:
        print("Error: La raíz cuadrada solo está definida para números no negativos.")
        return None
    else:
        return math.sqrt(n)

def cambiar_numeros():
    a = float(input("Ingrese el nuevo valor para el primer número: "))
    b = float(input("Ingrese el nuevo valor para el segundo número: "))
    return a, b

def menu():
    print("Calculadora:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potenciación")
    print("6. Factorial")
    print("7. Raíz Cuadrada")
    print("8. Cambiar Números")
    print("9. Salir")

# Inicializar números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

while True:
    menu()
    opcion = input("Seleccione una opción (1-9): ")

    if opcion == "1":
        print("Resultado:", suma(num1, num2))
    elif opcion == "2":
        print("Resultado:", resta(num1, num2))
    elif opcion == "3":
        print("Resultado:", multiplicacion(num1, num2))
    elif opcion == "4":
        resultado_division = division(num1, num2)
        if resultado_division is not None:
            print("Resultado:", resultado_division)
    elif opcion == "5":
        print("Resultado:", potenciacion(num1, num2))
    elif opcion == "6":
        num_factorial = int(input("Ingrese el número para calcular el factorial: "))
        print("Resultado:", factorial(num_factorial))
    elif opcion == "7":
        num_raiz = int(input("Ingrese un número entero positivo para calcular la raíz cuadrada: "))
        resultado_raiz = raiz_cuadrada(num_raiz)
        if resultado_raiz is not None:
            print("Resultado:", resultado_raiz)
    elif opcion == "8":
        num1, num2 = cambiar_numeros()
    elif opcion == "9":
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")