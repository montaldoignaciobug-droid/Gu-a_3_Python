#Ejercicio 15
#Pide dos números. Calcula la suma, resta y multiplicación. Luego pregunta al usuario qué
#operación quiere ver (1=suma, 2=resta, 3=multiplicación). Muestra el resultado
#correspondiente usando condicionales.

print("\n==============================================\n")

num_1 = float(input("Ingrese el primer número: "))
num_2 = float(input("Ingrese el segundo número: "))

suma = num_1 + num_2
resta = num_1 - num_2
mult = num_1 * num_2

print("\nOperación matematicas")
print("1) Suma")
print("2) Resta")
print("3) Multiplicación\n")

opt = int(input("Escoje una opción (1/2/3): "))

if opt == 1:
    print(f"Suma de ambos números: {suma:.2f}")

elif opt == 2:
    print(f"Resta de ambos números: {resta:.2f}")

elif opt == 3:
    print(f"Multiplicación de ambos números: {mult:.2f}")

else:
    print("Elección no valida.")

print("\n==============================================\n")