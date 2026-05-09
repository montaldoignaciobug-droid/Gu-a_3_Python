#Ejercicio 9
#Pide un número entero. Incrementa su valor en 10 (actualización). Luego verifica si el nuevo
#valor es múltiplo de 3 y de 5 al mismo tiempo.

print("\n==============================================\n")

num = int(input("Ingrese un número entero: "))
num = num * 10

multiplo_3 = num % 3
multiplo_5 = num % 5

if multiplo_3 == 0 and multiplo_5 == 0:
    print(f"El número {num} es múltiplo de 3 y 5")

else:
    print(f"El número {num} no es múltiplo de 3 y 5")

print("\n==============================================\n")