#Ejercicio 17
#Pide tres números enteros. Determina si al menos dos de ellos son positivos. Muestra un
#mensaje booleano (True/False) indicándolo.

print("\n==============================================\n")

num_1 = int(input("Ingresa un número: "))
num_2 = int(input("Ingresa otro número: "))
num_3 = int(input("Ingresa otro número: "))

estado = False
contador = 0

if num_1 > 0:
    contador += 1

if num_2 > 0:
    contador += 1

if num_3 > 0:
    contador += 1

if contador >= 2:
    estado = True
    print(f"Estado: {estado}")
    
else:
    print(f"Estado: {estado}")

print("\n==============================================\n")