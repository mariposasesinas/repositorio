print("This is python")

# Función para sumar dos números
def sumar(a, b):
    return a + b

# Función para restar dos números
def restar(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Función para dividir dos números
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero"

# Función principal
def main():
    opcion = ""
    while opcion != "5":
        print("\nCALCULADORA")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        try:
            opcion = int(opcion)
            if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))

                if opcion == 1:
                    resultado = sumar(num1, num2)
                    print("El resultado de la suma es:", resultado)
                elif opcion == 2:
                    resultado = restar(num1, num2)
                    print("El resultado de la resta es:", resultado)
                elif opcion == 3:
                    resultado = multiplicar(num1, num2)
                    print("El resultado de la multiplicación es:", resultado)
                elif opcion == 4:
                    resultado = dividir(num1, num2)
                    print("El resultado de la división es:", resultado)
            elif opcion == 5:
                print("¡Hasta luego!")
            else:
                print("Opción inválida. Por favor, elige una opción válida.")
        except ValueError:
            print("Opción inválida. Por favor, elige una opción válida.")

# Ejecutar la función principal
main()