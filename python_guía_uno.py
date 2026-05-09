#Ejercicio 1
#Crea un programa que pida al usuario su edad (entero) y determine si es mayor de edad (18 o
#más). Muestra un mensaje indicándolo. Además, actualiza la variable edad sumándole 5 años y
#muestra la edad futura.

print("\n==========================================\n")
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Usted es mayor de edad.")

else:
    print("Usted es menor de edad.")

print(f"Mas 5 años su edad sería: {edad + 5} años")

print("\n==========================================")