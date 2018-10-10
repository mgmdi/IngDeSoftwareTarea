import datetime   

def verificacionDatos(age,sex,weeksC,indicador):
    if(not(indicador)):
        if(sex.lower() == "m" and int(age) >= 60 and int(weeksC)>=750):
            return("SI")
        elif(sex.lower() == "f" and int(age) >= 55 and int(weeksC)>=750):
            return("SI")
        else:
            return("NO")
    else:
        if(sex.lower() == "m" and int(age) >= 55 and int(weeksC)>=750):
            return("SI")
        elif(sex.lower() == "f" and int(age) >= 50 and int(weeksC)>=750):
            return("SI")
        else:
            return("NO")
        

def calculoEdad(fecha):
    # Fecha debe ser del tipo XX/XX/XXXX donde x es un entero, verifiquemoslo:
    fecha = fecha.split('/')
    if(len(fecha)== 3):
        if(fecha[0].isdigit() and fecha[1].isdigit() and fecha[2].isdigit()):
            now = datetime.datetime.now()
            if(int(fecha[1])<= now.month):
                edad = int(now.year) - int(fecha[2])
            else:
                edad = int(now.year) - int(fecha[2]) - 1
            
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
        if sexo.lower() not in ["m","f","femenino","masculino"]:
            print("Error, debe indicar su sexo de la forma F o M. Femenino o Masculino")
            exit()
        semCoti = input("Ingrese el numero de semanas cotizadas: ")
        if not(semCoti.isdigit()):
            print("Error, las semanas cotiza deben estar en formato numerico.")
            exit()
        descontEdad = input("Ha trabajado usted en medios insalubres o capaces de producir vejez prematura?")
        if descontEdad.lower() not in ["si","no"]:
            print("Error, la respuesta debe ser si o no")
            exit()
        if(descontEdad.lower() == "si"):
            numAnos = input("Indique el numero de anos que trabajo: ")
            if(numAnos > 4):
                edad = edad - (int(numAnos) // 4)
                print("Se le ha descontado " + menosAnos + "de la edad considerada")
        verificacionDatos(edad,sexo,weeksC,descontEdad)
    elif(opcion == "2"):
        nombre = input("Ingrese nombre del archivo: ")
        file = open(nombre, "r")
        for line in file:
            datos = line.split()
            edad = calculoEdad(datos[0])
            if datos[1].lower() not in ["m","f","femenino","masculino"]:
                print("Error en los datos del archivo")
                exit()
            elif not(datos[2].isdigit()):
                print("Error en los datos del archivo")
                exit()
            if(len(datos) == 5 and datos[3].lower() == "si"):
                edad = edad - (int(datos[4])//4)
                verificacionDatos(edad,datos[1],datos[2], True)
                return
            verificacionDatos(edad,datos[1],datos[2], False)
    else:
        print("Error, debe ingresar 1 o 2")
       
if __name__ == '__main__':
    main()  