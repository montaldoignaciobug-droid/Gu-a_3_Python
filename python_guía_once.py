#Ejercicio 11
#Pide la base y altura de un rectángulo (enteros). Calcula el área. Si el área es mayor a 100,
#muestra "Rectángulo grande", de lo contrario "Rectángulo pequeño".

print("\n==============================================\n")

base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

area = (base * altura)

if area > 100:
    print(f"Rectángulo grande (área: {area})")

else:
    print(f"Rectángulo pequeño (área: {area})")

print("\n==============================================\n")