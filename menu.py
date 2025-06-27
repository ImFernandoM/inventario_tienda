user = "us"
contrasena = "pass"

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