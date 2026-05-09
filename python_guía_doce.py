#Ejercicio 12
#Pide dos números. Actualiza el primer número sumándole el segundo, y actualiza el segundo
#número restándole 3. Luego muestra cuál de los dos actualizados es mayor.

print("\n==============================================\n")

num_1 = float(input("Ingrese el primer número: "))
num_2 = float(input("Ingrese el segundo número: "))

num_1 = num_1 + num_2
num_2 = num_2 - 3

print(f"Primer número actualizado: {num_1:.2f}")
print(f"Segundo número actualizado: {num_2:.2f}\n")

if num_2 > num_1:
    print(f"{num_2:.2f} es mayor que {num_1:.2f}")

elif num_1 > num_2:
    print(f"{num_1:.2f} es mayor que {num_2:.2f}")

else:
    print("Ambos numeros son iguales.")

print("\n==============================================\n")