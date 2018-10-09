opcion = input("Ingrese la opcion 1 para ingresar datos por consola, ingrese dos para cargar un archivo de texto")



    if(opcion == "1"):
        edad = input("Imgrese fecha de nacimiento (XX/XX/XXXX): ")
        sexo = input("Ingrese su sexo: ")
        semCoti = input("Ingrese el numero de semanas cotizadas: ")
        descontEdad = input("Ha trabajado usted en medios insalubres o capaces de producir vejez prematura?")
        if(descontEdad = "Si" or descontEdad = "si"):
            numAnos = input("Indique el numero de anos que trabajo: ")
            if(numAnos > 4):
                menosAnos = numAnos // 4
                edad = edad - menosAnos
                print("Se le ha descontado " + menosAnos + "de la edad considerada")
    else if(opcion == "2"):
        nombre = input("Ingrese nombre del archivo: ")
        print(nombre)
