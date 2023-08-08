#EJERCICIO2
def suma_enteros():
    while True:
        # Solicitar al usuario que ingrese un número entero positivo
        n = int(input("Ingrese un número entero positivo: "))

        # Validar que el número sea positivo
        if n <= 0:
            print("El número ingresado no es válido.")
            continue

        # Calcular la suma de los enteros desde 1 hasta n
        suma = 0
        for i in range(1, n + 1):
            suma += i

        # Imprimir la suma en pantalla
        print("La suma de los enteros desde 1 hasta ",n," es: ",suma)

        # Preguntar al usuario si desea continuar o salir del programa
        respuesta = input("¿Desea continuar? (s/n): ")
        if respuesta.lower() != "s":
            print("Hasta luego!")
            break

suma_enteros()
