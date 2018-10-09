import datetime   

def verificacionDatos(age,sex,weeksC):
    if(sex.lower() == "m" and int(age) >= 60 and int(weeksC)>=750):
        print("SI")
    elif(sex.lower() == "f" and int(age) >= 55 and int(weeksC)>=750):
        print("SI")
    else:
        print("NO")

def calculoEdad(fecha):
    # Fecha debe ser del tipo XX/XX/XXXX donde x es un entero, verifiquemoslo:
    fecha = fecha.split('/')
    if(len(fecha)== 3):
        if(fecha[0].isdigit() and fecha[1].isdigit() and fecha[2].isdigit()):
            now = datetime.datetime.now()
            edad = int(now.year) - int(fecha[2])
        else:
            print("Error, la fecha debe seguir el formato indicado.")
            exit()
    else:
        print("Error, la fecha debe seguir el formato indicado.")
        exit()

    return edad

def main():
    opcion = input("Ingrese la opcion 1 para ingresar datos por consola, ingrese dos para cargar un archivo de texto: ")
    if(opcion == "1"):
        edad = calculoEdad(input("Imgrese fecha de nacimiento (XX/XX/XXXX): "))
        sexo = input("Ingrese su sexo: ")
        semCoti = input("Ingrese el numero de semanas cotizadas: ")
        descontEdad = input("Ha trabajado usted en medios insalubres o capaces de producir vejez prematura?")
        if(descontEdad.lower() == "si"):
            numAnos = input("Indique el numero de anos que trabajo: ")
            if(numAnos > 4):
                menosAnos = numAnos // 4
                edad = edad - menosAnos
                print("Se le ha descontado " + menosAnos + "de la edad considerada")
        verificacionDatos(edad,sexo,weeksC)
    elif(opcion == "2"):
        nombre = input("Ingrese nombre del archivo: ")
        file = open(nombre, "r")
        for line in file:
            datos = line.split()
            verificacionDatos(datos[0],datos[1],datos[2])
    else:
        print("Error, debe ingresar 1 o 2")
       
if __name__ == '__main__':
    main()  