# Desarrollo de un prototipo simple de un sistema de gestion de inventarios basado en consola

#Funiconalidades niminas requeridas
#ver la lista de productos en el inventario
#Registrar una venta y que se actualice el programa en cantidad de unidades de stock
#registrar ingreso de la nueva mercancia

#funcionalidades adicionales
#login de usuario y contrasena
#registro de ventas diarias
#registro de ventas por producto

#conceptos a utilizar
#variables para guardar datos
#Listas para estructurar el invenatrio
#Bucles para el menu principal 
#Ciclos para correr el inventario 
#Condicionales para validaciones
#Break par a salir del programa

# Vamos a crearlo todo con funciones para que despues sea mas facil de llamarlos


#Funcion de inicio de sesion:
#lista de usuarios para la aplicacion
user = "us"
contrasena = "pass"

#Registro de ventas
ventas = 0

#Este es el inventario de la tienda de Don carlos 
inventario = [
    ["Leche", 20, 3500],
    ["Pan", 50, 3500],
    ["Huevos", 30, 500]
]

#Funcion de inicio de ingreso de sesion 
def usuario():
    print("\n ---> INVENTARIO TIENDA DON CARLOS <--- ")
    intentos = 0
    
    while intentos < 3:
        intentoIngreso = input("\nIngrese su usuario: ")
        intentoUser = intentoIngreso.lower()
        if intentoUser != user:
            print("\nUsuario incorrecto, ingrese su usuario")
            intentos += 1
            print(f"\nLe quedan {3 - intentos} oportunidades para ingresar el usuario correctamente")
        else:
            intentoLogin = 0
            while intentoLogin < 3:
                intentoPass = input("Ingrese su contrasena: ")
                if intentoPass != contrasena:
                    intentoLogin += 1
                    print(f"Contrasena incorrecta tienes {3 - intentoLogin} oportunidades para ingresar correctamente tu contrasena")
                else:
                    return intentoUser
            return None
    print("Error en el sistema, intentelo mas tarde")


#funcion para mostrar el menu de la aplicacion
def mostrarMenu (intentoUser):
    print(f"\nBienvenido {user.title()}")
    print("\n ---> INVENTARIO TIENDA DON CARLOS <--- ")
   
    print("1. Ver la lista de productos")
    print("2. Registrar una venta")
    print("3. Registrar ingreso de mercancia")
    print("4. Registro de ventas diarias")
    print("5. Registro de ventas por producto")
    print("6. Salir del sistema")
    

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
                    
    
#funcion para registrar una venta, teniendo en cuenta que debe modificarse el inventario
def registroVentas():
    global ventas, inventario # Se toman desde afuera de la funcion
    print("\n ---> INVENTARIO TIENDA DON CARLOS <---")
    venta = input("Ingrese el nombre del producto: ")
    ventaProducto = venta.title()
    encontrado =  False
    for producto in inventario:
        if producto[0] == ventaProducto: # En este caso el nombre "Producto" esta remplanzando el nombre inventario y el numero [#] es la posicion de lo quye tenemos en la lista anidada
                cantidadVenida = int(input("Ingrese la cantidad que vendio: "))
                if cantidadVenida > producto[1]: # aca remplaza a la cantidad de unidades que tenemos en stock.
                    print("La cantidad registrada supera la cantidad de unidades de stock.")
                else:
                    producto[1] -= cantidadVenida
                    print(f"Venta registrada exitosamente! se registro la venta de {cantidadVenida} {ventaProducto}, te quedan {producto[1]}")
                    producto[2] *= cantidadVenida
                    print(f"\n Ventas de {producto[1]} es de ${producto[2]} Pesos")
                    
                    
                    
                    
