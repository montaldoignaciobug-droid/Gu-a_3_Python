#Ejercicio 8
#Pide un número. Si es par y mayor que 10, muestra "Número par y mayor que 10". Si es par
#pero no mayor que 10, muestra "Número par menor o igual a 10". Si es impar, muestra
#"Impar". Usa operador módulo (%).

print("\n==============================================\n")

num = float(input("Ingrese un número: "))
residuo = num % 2

if num > 10 and residuo == 0.0:
    print("Número par y mayor que 10")

elif num <= 10 and residuo == 0.0:
    print("Número par menor o igual a 10")

else:
    print("Impar")

print("\n==============================================\n")