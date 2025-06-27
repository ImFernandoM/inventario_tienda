user = "us"
contrasena = "pass"

#Funcion de inicio de ingreso de sesion 
def login():
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