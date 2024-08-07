import json

def Abrir():
    datos=[]
    with open("productos.json", encoding="utf8") as openfile:
        datos=json.load(openfile)
        return datos
    
def guardar(midato):
    with open("productos.json", "w") as mifile:
        json.dump(midato,mifile)
def AbrirVentas():
    datos=[]
    with open("ventas.json", encoding="utf8") as openfile:
        datos=json.load(openfile)
        return datos
    
def guardarVentas(midato):
    with open("ventas.json", "w") as mifile:
        json.dump(midato,mifile)

archivo=Abrir()
archivoVentas=AbrirVentas()
def menu():
    print("------Menú------\n"
          "1. ventas\n"
          "2. compras\n"
          "3. generacion de informes\n")
def tipos_productos():
    print("tipos de producto\n"
          "\n"
          "1. panaderia\n"
          "2. pasteleria\n"
          "3. bebidas\n"
          "4. apartado de promociones.\n"
          "")
def informes():
    print("GENERACIÓN DE INFORMES\n"
          "1. Informes de ventas\n"
          "2. Informes de stock"
          "")

bucle=True
while bucle==True:
    menu()
    opc=int(input("Selecciona una opción: "))
    if opc==1:
        archivo=Abrir()
        archivoVentas=AbrirVentas()
        print("ingresa la fecha de la venta")
        dia_venta=int(input("Dia: "))
        mes_venta=int(input("Mes (numero): "))
        año_venta=int(input("Año: "))
        print("informacion del cliente")
        nombre_cliente=input("ingresa el nombre\n")
        direccion_cliente=input("ingrese la direccion del cliente\n")
        nombre_empleado=input("Información del empleado que realizo la venta\n"
                              "Nombre del empleado\n")
        cargo=input("cargo del empleado\n")
        tipos_productos()
        opc_tipo=input("escoje un opción: ")
        if opc_tipo=="1":
            for i in archivo["Panaderia"]:
                print("------------------------------")
                print("ID: ",i["id"])
                print("Nombre: ",i["nombre"])
                print("Precio: ",i["precio"])
            escojer=int(input("Escoje el producto por su id\n"
                              "id del producto: "))
            for x in archivo["Panaderia"]:
                if x["id"]==escojer:
                    cantidad=int(input("Que cantidad quieres de este producto: "))
                    x["stock"]=x["stock"]-cantidad
                    nombre_producto=x["nombre"]
                    precio=x["precio"]
                    precio_total=cantidad*precio
        if opc_tipo=="2":
            for i in archivo["Pasteleria"]:
                print("------------------------------")
                print("ID: ",i["id"])
                print("Nombre: ",i["nombre"])
                print("Precio: ",i["precio"])
            escojer=int(input("Escoje el producto por su id\n"
                              "id del producto: "))
            for x in archivo["Pasteleria"]:
                if x["id"]==escojer:
                    cantidad=int(input("Que cantidad quieres de este producto: "))
                    x["stock"]=x["stock"]-cantidad
                    nombre_producto=x["nombre"]
                    precio=x["precio"]
                    precio_total=cantidad*precio
        if opc_tipo=="3":
            for i in archivo["Bebidas"]:
                print("------------------------------")
                print("ID: ",i["id"])
                print("Nombre: ",i["nombre"])
                print("Precio: ",i["precio"])
            escojer=int(input("Escoje el producto por su id\n"
                              "id del producto: "))
            for x in archivo["Bebidas"]:
                if x["id"]==escojer:
                    cantidad=int(input("Que cantidad quieres de este producto: "))
                    x["stock"]=x["stock"]-cantidad
                    nombre_producto=x["nombre"]
                    precio=x["precio"]
                    precio_total=cantidad*precio
        if opc_tipo=="4":
            for i in archivo["Apartado de promociones"]:
                print("------------------------------")
                print("ID: ",i["id"])
                print("Nombre: ",i["nombre"])
                print("Precio: ",i["precio"])
            escojer=int(input("Escoje el producto por su id\n"
                              "id del producto: "))
            for x in archivo["Apartado de promociones"]:
                if x["id"]==escojer:
                    cantidad=int(input("Que cantidad quieres de este producto: "))
                    x["stock"]=x["stock"]-cantidad
                    nombre_producto=x["nombre"]
                    precio=x["precio"]
                    precio_total=cantidad*precio
        idventas=len(archivoVentas["ventas"])+1
        archivoVentas["ventas"].append({"id":idventas, "fecha de venta":{"dia":dia_venta, "mes":mes_venta, "año":año_venta}, "cliente":{"nombre":nombre_cliente, "direccion":direccion_cliente}, "empleado":{"nombre":nombre_empleado, "cargo":cargo,},
                                        "producto":{"nombre":nombre_producto, "cantidad":cantidad,"precio":precio, "precio_total":precio_total},})
        guardarVentas(archivoVentas)
        guardar(archivo)

    if opc==2:
        archivo=Abrir()
        archivoVentas=AbrirVentas()
        print("ingresa la fecha de la compra")
        dia_compra=int(input("Dia: "))
        mes_compra=int(input("Mes (numero): "))
        año_compra=int(input("Año: "))
        nombre_proveedor=input("Información del proveedor\n"
                               "Nombre: ")
        contacto=input("Contacto: ")
        producto_comprado=input("Información del producto comprado\n"
                                "Nombre: ")
        cantidad_comprada=int(input("Cantidad: "))
        contador=0
        for a in archivo["Panaderia"]:
            if a["nombre"]==producto_comprado:
                contador+=1
                a["stock"]+=cantidad_comprada
        for a in archivo["Pasteleria"]:
            if a["nombre"]==producto_comprado:
                contador+=1
                a["stock"]+=cantidad_comprada
        for a in archivo["Bebidas"]:
            if a["nombre"]==producto_comprado:
                contador+=1
                a["stock"]+=cantidad_comprada
        for a in archivo["Apartado de promociones"]:
            if a["nombre"]==producto_comprado:
                contador+=1
                a["stock"]+=cantidad_comprada
        
        precio_compra=int(input("Precio de la compra: "))
        precio_unidad=precio_compra/cantidad_comprada
        if contador==0:
            print("Este es un nuevo producto, a que apartado lo deseas agregar")
            tipos_productos()
            opc_tipo=input("escoje un opción: ")
            if opc_tipo=="1":
                id_producto=len(archivo["Panaderia"])+1
                archivo["Panaderia"].append({"id":id_producto, "nombre":producto_comprado, "precio":precio_unidad, "stock":cantidad_comprada})
            if opc_tipo=="2":
                id_producto=len(archivo["Pasteleria"])+1
                archivo["Pasteleria"].append({"id":id_producto, "nombre":producto_comprado, "precio":precio_unidad, "stock":cantidad_comprada})
            if opc_tipo=="3":
                id_producto=len(archivo["Bebidas"])+1
                archivo["Bebidas"].append({"id":id_producto, "nombre":producto_comprado, "precio":precio_unidad, "stock":cantidad_comprada})
            if opc_tipo=="4":
                id_producto=len(archivo["Apartado de promociones"])+1
                archivo["Apartado de promociones"].append({"id":id_producto, "nombre":producto_comprado, "precio":precio_unidad, "stock":cantidad_comprada})
            
        id_compras=len(archivoVentas["compras"])+1
        archivoVentas["compras"].append({"id":id_compras, "fecha de compra":{"dia":dia_compra, "mes":mes_compra, "año":año_compra}, 
                                         "proveedor":{"nombre":nombre_proveedor, "contacto":contacto},"producto":{"nombre":producto_comprado, "cantidad":cantidad_comprada, "precio":precio_compra}})
        guardarVentas(archivoVentas)
        guardar(archivo)

    if opc==3:
        archivo=Abrir()
        archivoVentas=AbrirVentas()
        informes()
        opc_informes=input("Escoje una opción: ")
        if opc_informes=="1":
            print("De que fecha quieres ver las ventas realizadas")
            mes_inicio=int(input("Mes (número): "))
            año_inicio=int(input("Año: "))
            total_mes=0
            for z in archivoVentas["ventas"]:
                if z["fecha de venta"]["mes"]==mes_inicio and z["fecha de venta"]["año"]==año_inicio:
                    print("-------------------------")
                    print("ID: ",z["id"])
                    print("fecha: ",z["fecha de venta"]["dia"],"-",z["fecha de venta"]["mes"],"-",z["fecha de venta"]["año"])
                    print("Cliente: ",z["cliente"])
                    print("Empleado: ",z["empleado"])
                    print("producto")
                    print("nombre: ",z["producto"]["nombre"])
                    print("cantidad: ",z["producto"]["cantidad"])
                    print("precio: ",z["producto"]["precio"])
                    print("precio total: ",z["producto"]["precio_total"])
                    total_mes=total_mes+z["producto"]["precio_total"]
            print("Las ganancias de este mes son de: ",total_mes)
        
        if opc_informes=="2":
            archivo=Abrir()
            print("informes de stock")
            print("que productos quieres ver")
            tipos_productos()
            opc_tipo=input("escoje un opción: ")
            if opc_tipo=="1":
                for i in archivo["Panaderia"]:
                    print("------------------------------")
                    print("ID: ",i["id"])
                    print("Nombre: ",i["nombre"])
                    print("Precio: ",i["precio"])
                    print("Stock: ",i["stock"])
            if opc_tipo=="2":
                for i in archivo["Pasteleria"]:
                    print("------------------------------")
                    print("ID: ",i["id"])
                    print("Nombre: ",i["nombre"])
                    print("Precio: ",i["precio"])
                    print("Stock: ",i["stock"])
            if opc_tipo=="3":
                for i in archivo["Bebidas"]:
                    print("------------------------------")
                    print("ID: ",i["id"])
                    print("Nombre: ",i["nombre"])
                    print("Precio: ",i["precio"])
                    print("Stock: ",i["stock"])
            if opc_tipo=="4":
                for i in archivo["Apartado de promociones"]:
                    print("------------------------------")
                    print("ID: ",i["id"])
                    print("Nombre: ",i["nombre"])
                    print("Precio: ",i["precio"])
                    print("Stock: ",i["stock"])