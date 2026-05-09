#Ejercicio 4
#Pide un número entero. Si es positivo, calcula su cuadrado (potencia 2). Si es negativo,
#muestra un mensaje. Si es cero, muestra otro mensaje. Usa operador aritmético.

print("\n==========================================\n")

num = int(input("Ingrese un número entero: "))

if num > 0:
    print(f"Calculo de su cuadrado: {num ** 2}")

elif num < 0:
    print(f"Su numero es negativo.")

else:
    print("Su número es 0.")

print("\n==========================================\n")