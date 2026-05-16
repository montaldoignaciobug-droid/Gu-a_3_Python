#Ejercicio 19
#Pide un número. Calcula su valor absoluto sin usar abs() (usando condicional). Luego actualiza
#la variable con su valor absoluto y muestra cuántas veces cabe el número 3 en ese valor
#(división entera).

print("\n==============================================\n")

num = int(input("Ingresa un número: "))

if num < 0:
    num = -num

contador = num // 3

print(f"Valor absoluto: {num}")
print(f"El tres cabe {contador} veces en {num}")

print("\n==============================================\n")