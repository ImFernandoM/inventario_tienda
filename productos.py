#funcion para revisar el inventario, tiene que ingresar un argumento que en este caso es el inventario
def productos(listaProductos):
    regreso = "si"
    regresoLower = regreso.lower
    while regreso == "si":
        print("\n ---> INVENTARIO TIENDA DON CARLOS <--- ")
        print("\nProductos disponibles: ")
        disponible = []
        for producto in listaProductos:
            disponible.append(producto[0])
        print(disponible)
        consulta = input("\nIngrese el nombre del producto a consultar: ")
        consultaLower = consulta.title()
        encontrado = False # Bandera, no se ha encontrado el producto
        for product in listaProductos:
            if consultaLower == product[0]:
                print(product)
                encontrado = True
                break
        else:
            print("Producto no encontrado")
            regreso = input("Desea regresar al menu del inventario ? Si / No ")
            regresoLower = regreso.lower 
            if regresoLower == "no" or regresoLower == "salir":
                break
    print("Gracias por usar nuestro servicio")