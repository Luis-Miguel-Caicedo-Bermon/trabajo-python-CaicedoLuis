import json

def Abrir():
    datos=[]
    with open("productos.json", encoding="utf8") as openfile:
        datos=json.load(openfile)
        return datos
    
def guardar(midato):
    with open("productos.json", "w") as mifile:
        json.dump(midato,mifile)

archivo=Abrir()

def menu():
    print("------Menú------\n"
          "1. ventas\n"
          "2. compras\n"
          "3. generacion de informes\n")
    
bucle=True
while bucle==True:
    menu()
    opc=int(input("Selecciona una opción"))
    if opc==1:
        fecha=input("ingresa la fecha de la venta\n")
        print("informacion del cliente")
        nombre_cliente=input("ingresa el nombre\n")
        direccion_cliente=input("ingrese la direccion del cliente")
        nombre_empleado=input("Información del empleado que realizo la venta\n"
                              "Nombre del empleado\n")
