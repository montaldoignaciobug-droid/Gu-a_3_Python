#Ejercicio 2
#Pide dos números enteros al usuario. Realiza las operaciones aritméticas básicas (suma, resta,
#multiplicación, división entera, residuo) y muestra los resultados. Si el segundo número es 0,
#evita la división mostrando un mensaje de error.

print("\n==========================================\n")

print("Calculadora básica")

num_1 = float(input("Primer número: "))
num_2 = float(input("Segundo número: "))

print("\n +) Suma")
print(" -) Resta")
print(" *) Multiplicación")
print(" /) División")
print(" %) Residuo\n")

opt = input("Ingrese el signo de la operación deseada: ")

if opt == "+":
    print("Suma")
    print(f"La suma da: {num_1 + num_2}")

elif opt == "-":
    print("Resta")
    print(f"La resta da: {num_1 - num_2}")

elif opt == "*":
    print("Multiplicación")
    print(f"La multiplicación da: {num_1 * num_2}")

elif opt == "/":
    if num_2 == 0:
        print("Error. No se puede dividir entre 0")

    else:
        print("División")
        print(f"La división da: {num_1 / num_2}")

elif opt == "%":
    print("Residuo")
    print(f"El residuo da: {num_1 % num_2}")

else:
    print("Elección no valida.")

print("\n==========================================\n")