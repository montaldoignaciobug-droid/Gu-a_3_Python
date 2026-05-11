#Ejercicio 18
#Pide un año. Determina si es bisiesto (divisible entre 4, pero no entre 100 a menos que
#también sea divisible entre 400). Muestra un mensaje.

print("\n==============================================\n")

año = int(input("Ingresa un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"{año} es bisiesto")

else:
    print(f"{año} no es bisiesto")

print("\n==============================================\n")
