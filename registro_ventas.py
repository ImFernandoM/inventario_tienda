#Registrar ventas  
def registroIngreso(listaProductos):
    global inventario
    print("\n ---> INVENTARIO TIENDA DON CARLOS <--- ")
    print("Ingrese la el producto a registrar")
    nombre = input("Nombre del producto: ")
    nombreRegistro = nombre.title()
    cantidad = 0
    while cantidad <= 0:
        cantidad = int(input("cantidad de unidades a registrar: "))
    precio = 0
    while precio <= 0:
        precio = float(input("Ingrese precio: "))

    inventario.append([nombre, cantidad, precio])
    
    print("Registro exitoso")
    print(f"Se ingresaron {cantidad} unidades de {nombreRegistro} con un valor de {precio} por unidad.")