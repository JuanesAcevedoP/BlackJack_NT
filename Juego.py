while True:
    print("Bienvenido al Casino el Sombrero Vueltiao")
    print("Menú:")
    print("1. TragaPerras")
    print("2. BlackJack")
    print("3. Ruleta")
    print("4. Dados")
    print("5. Salir")

    # Pedir al usuario que elija una opción
    opcion = input("Elija que quiere jugar ps mijito (1-5): ")

    #### Funciones aquí #####



    ####  Fin Funciones #####

    # Verificar si la opción es válida
    if opcion.isdigit():
        opcion = int(opcion)
        if opcion == 1:
            print("Has seleccionado la TragaPerras")
            # Aquí puedes colocar el código correspondiente a la Opción 1
        elif opcion == 2:
            print("Has seleccionado el BlackJack")
            # Aquí puedes colocar el código correspondiente a la Opción 2
        elif opcion == 3:
            print("Has seleccionado la Ruleta")
            # Aquí puedes colocar el código correspondiente a la Opción 3
        elif opcion == 4:
            print("Has seleccionado los Dados")
            # Aquí puedes colocar el código correspondiente a la Opción 4
        elif opcion == 5:
            print("Hasta que vuelva ps mijito. ¡Que la virgen lo acompañe")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida (1-5).")
    else:
        print("Entrada no válida. Por favor, ingrese un número del menú (1-5).")
