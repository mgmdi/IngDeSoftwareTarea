
        
def verificacionDatos(age,sex,weeksC):
    if(sex.lower() == "m" and int(age) >= 60 and int(weeksC)>=750):
        print("SI")
    elif(sex.lower() == "f" and int(age) >= 55 and int(weeksC)>=750):
        print("SI")
    else:
        print("NO")




def main():
    opcion = input("Ingrese la opcion 1 para ingresar datos por consola, ingrese dos para cargar un archivo de texto: ")
    if(opcion == "1"):
        edad = input("Imgrese fecha de nacimiento (XX/XX/XXXX): ")
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

if __name__ == '__main__':
    main()  