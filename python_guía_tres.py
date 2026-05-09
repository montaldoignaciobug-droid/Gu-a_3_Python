#Ejercicio 3
#Pide una contraseña (string). Si la contraseña es "python123", muestra acceso concedido. Si
#no, muestra acceso denegado. Luego, actualiza una variable booleana llamada acceso que sea
#True si la contraseña es correcta.

print("\n==========================================\n")

validacion = "python123"
contraseña = input("Ingrese su contraseña: ")

if contraseña == validacion:
    acceso = True
    print("Contraseña correcta, acceso permitido.")

else:
    acceso = False
    print("Contraseña incorrecta.")

print(f"Variable acceso: {acceso}")

print("\n==========================================\n")