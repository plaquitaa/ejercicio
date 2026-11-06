
estudiantes = []
notas = []

while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1. Ingresar estudiantes")
    print("2. Mostrar todos los estudiantes")
    print("3. Estadisticas del salon")
    print("4. Salir")

    opcion = int(input("Seleccione una opcion: "))

    # OPCION 1: INGRESAR ESTUDIANTES
    if opcion == 1:
        nombre = input("Ingrese el nombre del estudiante: ")
        nota = float(input("Ingrese la nota del estudiante (1 a 5): "))

        while nota < 1 or nota > 5:
            print("Error: La nota debe estar entre 1 y 5.")
            nota = float(input("Ingrese nuevamente la nota: "))

        estudiantes.append(nombre)
        notas.append(nota)

        print("Estudiante registrado correctamente.")

    # OPCION 2: MOSTRAR ESTUDIANTES
    elif opcion == 2:

        if len(estudiantes) == 0:
            print("No hay estudiantes registrados.")

        else:
            print("\n===== ESTUDIANTES REGISTRADOS =====")

            for i in range(len(estudiantes)):
                print("\nEstudiante:", estudiantes[i])
                print("Nota:", notas[i])

                if notas[i] >= 3.0:
                    print("Estado: GANO")
                else:
                    print("Estado: PERDIO")

    # OPCION 3: ESTADISTICAS DEL SALON
    elif opcion == 3:

        if len(estudiantes) == 0:
            print("No hay notas para mostrar.")

        else:
            mejor_nota = max(notas)
            peor_nota = min(notas)
            promedio = sum(notas) / len(notas)

            print("\n===== ESTADISTICAS DEL SALON =====")
            print("Cantidad de estudiantes:", len(estudiantes))
            print("Mejor nota:", mejor_nota)
            print("Peor nota:", peor_nota)
            print("Promedio del salon:", round(promedio, 2))

            print("Estudiantes con la mejor nota:")

            for i in range(len(notas)):
                if notas[i] == mejor_nota:
                    print(estudiantes[i])

    # OPCION 4: SALIR
    elif opcion == 4:
        print("Saliendo del programa...")
        break

    # OPCION NO VALIDA
    else:
        print("Opcion no valida. Intente nuevamente (y este es el cambiooo).")
        
