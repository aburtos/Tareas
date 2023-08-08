def division_cubo():
    while True:
        # Solicitar al usuario que ingrese los dos números enteros
        num1 = int(input("Ingrese el primer número entero (distinto de cero): "))
        num2 = int(input("Ingrese el segundo número entero (distinto de cero): "))

        # Calcular división entera entre los dos números
        division_entera = num1 // num2

        # Calcular el cubo de los dos números usando la función de potencia
        cubo_num1 = num1 ** 3
        cubo_num2 = num2 ** 3

        # Imprimir los resultados en la consola
        print("La división entera de {} entre {} es: {}".format(num1, num2, division_entera))
        print("El cubo de {} es: {}".format(num1, cubo_num1))
        print("El cubo de {} es: {}".format(num2, cubo_num2))

        # Preguntar al usuario si desea continuar o salir del programa
        respuesta = input("¿Desea continuar? (s/n): ")
        if respuesta.lower() != "s":
            print("Hasta luego!")
            break

division_cubo()
