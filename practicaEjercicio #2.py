def contar_letras():
    while True:
        # Solicitar al usuario que ingrese su nombre
        nombre = input("Ingrese su nombre: ")

        # Contar la cantidad de letras en el nombre
        cantidad_letras = len(nombre)

        # Mostrar el resultado en pantalla
        print("{} tiene {} letras.".format(nombre, cantidad_letras))

        # Preguntar al usuario si desea continuar o salir del programa
        respuesta = input("¿Desea continuar? (s/n): ")
        if respuesta.lower() != "s":
            print("Hasta luego!")
            break

contar_letras()
