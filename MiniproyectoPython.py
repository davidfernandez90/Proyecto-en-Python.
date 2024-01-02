import os
import pickle


# lee archivo binario
def abrir():
    datosTabla=[]
    if os.path.isfile("datos.bin"):
        fichero=open("datos.bin", "rb")
        datosTabla= pickle.load(fichero)
        fichero.close()
        return datosTabla
    else:
        return datosTabla

# guarda archivo binario
def guardar(datosTabla):
    fichero=open("datos.bin","wb")
    pickle.dump(datosTabla,fichero)
    fichero.close()


#2.- Presentar un menú que contenga la posibilidad de:
#a.- agregar un registro  #opcion 1
def agregar(datosTabla, porcentaje):
    agregado=[]
    clavePrimera=int(input("Ingrese la clave primera a añadir:"))
    campotexto1=input("Ingrese el primer campo de texto a añadir:")
    campotexto2=input("Ingrese el segundo campo de texto a añadir:")
    camponumerico1=float(input("Ingrese el primer campo numerico a añadir:"))
    # actualizo el campo calculado
    camponumerico2=camponumerico1 * (porcentaje / 100)
    agregado=[clavePrimera,campotexto1,campotexto2,camponumerico1,camponumerico2]
    datosTabla.append(agregado)
    guardar(datosTabla)
    return datosTabla
    
#b.- eliminar un registro# opcion 2
def eliminar(datosTabla):
    eliminado=int(input("Ingrese la clave primera del elemento a eliminar:"))
    for i in datosTabla:
        if(i[0] == eliminado):
            datosTabla.remove(i)
    guardar(datosTabla)
    return datosTabla

#c.- modificar un registro (en este caso debe presentar un submenú consultando qué campo se desea modificar) #opcion 3 
def modificar(datosTabla, porcentaje):

    modificar=int(input("Ingrese la clave primera del elemento a modificar:"))
    for i in datosTabla:
        if(i[0] == modificar):
            print("Eligio la opcion 3. Modificar un registro:")
            print("Opcion 0: si quiere modificar la clave primera:")
            print("Opcion 1: si quiere modificar el primer campo de texto:")
            print("Opcion 2: si quiere modificar el segundo campo de texto:")
            print("Opcion 3: si quiere modificar el primer campo numerico:")
            opcionModificar=int(input("Ingrese la opcion a modificar:"))
            if opcionModificar ==0:
                print("Elijio Opcion 0: Clave primaria: ")
                print("Valor anterior:", i[0])
                clavePrimera=int(input("Ingrese nuevo valor:"))
                i[0] = clavePrimera
                guardar(datosTabla)
            elif opcionModificar ==1:
                print("Elijio Opcion 1: primer campo de texto: ", i[1])
                print("Valor anterior:", i[1])
                campotexto1=input("Ingrese nuevo valor:")
                i[1] = campotexto1
                guardar(datosTabla)
            elif opcionModificar ==2:
                print("Elijio Opcion 2: segundo campo de texto: ", i[2])
                print("Valor anterior:", i[2])
                campotexto2=input("Ingrese nuevo valor:")
                i[2] = campotexto2
                guardar(datosTabla)
            elif opcionModificar ==3:
                print("Elijio Opcion 3: primer campo numerico: ", i[3])
                print("Valor anterior:", i[3])
                camponumerico1=float(input("Ingrese nuevo valor:"))
                i[3] = camponumerico1
                # actualizo el campo calculado
                i[4] = camponumerico1 * (porcentaje / 100)
            else:
                print("La opcion ingresada es incorrecta")
    guardar(datosTabla)
    return datosTabla
            
#d.- actualizar el campo calculado (en base a un índice, coeficiente, porcentaje, o valor fijo según corresponda)  # opcion 4
def actualizarPorcentaje(porcentaje, datosTabla):
    porcentaje=int(input("ingresa valor de porcentaje: "))
    fichero= open("porcentaje.bin", "wb")
    pickle.dump(porcentaje,fichero)
    fichero.close()    

    for i in datosTabla:
        elementoModificado= float(i[3]) * (porcentaje / 100)
        i[4] = elementoModificado
    guardar(datosTabla)
    return datosTabla
    

def obtenerPorcentaje():
    porcentaje = 0
    if os.path.isfile("porcentaje.bin"):
        fichero= open("porcentaje.bin","rb")
        porcentaje=pickle.load(fichero)
        fichero.close()
    else:
        porcentaje=int(input("ingresa valor de porcentaje: "))
        fichero= open("porcentaje.bin", "wb")
        pickle.dump(porcentaje,fichero)
        fichero.close()    
    return porcentaje



#e.- listar la tabla (debe presentar un submenú ofreciendo dos tipos de listado). Los listados deben mostrar al final la cantidad # opcion 5
#de registros y el total de al menos uno de los campos numéricos.
def listar(datosTabla):

    cantidadRegistros=0
    sumaNumerico1=0.0
    sumaNumerico2=0.0

    for i in datosTabla:
        print(i[0], i[1], i[2], i[3], i[4])
        cantidadRegistros = cantidadRegistros+1
        sumaNumerico1=sumaNumerico1+float(i[3])
        sumaNumerico2=sumaNumerico2+float(i[4])

    print("La cantidad de registros son:", cantidadRegistros)
    print("La suma total del campo numerico 1 es:", sumaNumerico1)
    print("La suma total del campo numerico 2 es:", sumaNumerico2)
    
    
#f.- exportar la tabla a un archivo “.csv” #opcion 6
def exportar(datosTabla):
    fichero=open("datos.csv","w")
    for dato in datosTabla:
        registro=(str(dato[0]) + ";" +dato[1] + ";" + dato[2]+ ";"+ str(dato[3]).replace(".",",")+ ";"+str(dato[4]).replace(".",",")+ "\n")
        fichero.write(registro)
    fichero.close()

#1.- Cargar y leer los datos de la tabla desde/hacia un archivo binario.
datosTabla = abrir()
porcentaje = obtenerPorcentaje();
    
# se repite siempre hasta que ingrese un 0 #opcion 7
while True:
    print("Bienvenidos al menu")
    print("Ingrese la opcion 1: para agregar un registro:")
    print("Ingrese la opcion 2: para eliminar un registro:")
    print("Ingrese la opcion 3: para modificar un registro:")
    print("Ingrese la opcion 4: para actualizar el campo calculado:")
    print("Ingrese la opcion 5: para listar la tabla:")
    print("Ingrese la opcion 6: para exportar la tabla:")
    print("Ingrese la opcion 0: Salir:")
    opcion=int(input("Ingrese la opcion deseada:"))


    if opcion ==1:
        print(agregar(datosTabla, porcentaje))
        
    elif opcion ==2:
        print(eliminar(datosTabla))
        
    elif opcion ==3:
        print(modificar(datosTabla, porcentaje))
        
    elif opcion ==4:
        print(actualizarPorcentaje(porcentaje,datosTabla))
        
    elif opcion ==5:
        listar(datosTabla)
        
    elif opcion ==0:
        break
    elif opcion == 6:
        exportar(datosTabla)
        print("Se Guardo con Éxito el Archivo")
        
    else:
        print("La opcion ingresada es incorrecta, intentelo nuevamente")
    

    
    
    
    
#import lib as datos
#import os
    


            