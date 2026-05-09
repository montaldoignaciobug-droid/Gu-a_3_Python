#Ejercicio 6
#Pide tres calificaciones (enteros) al usuario. Calcula el promedio. Si el promedio es >= 70,
#muestra "Aprobado"; si está entre 50 y 69, "Recuperación"; si es menor, "Reprobado".
#Actualiza una variable estado con el resultado.

print("\n==============================================\n")
print("Promediador de notas\n")

cal_1 = int(input("Ingrese la primera nota: "))
cal_2 = int(input("Ingrese la segunda nota: "))
cal_3 = int(input("Ingrese la tercera nota: "))

promedio = (cal_1 + cal_2 + cal_3) / 3

if promedio >= 70:
    estado = "Aprobado"

elif promedio <= 69 and promedio >= 50:
    estado = "Recuperación"

else:
    estado = "Reprobado"

print(f"Promedio: {promedio:.2f}")
print(f"Estado: {estado}")

print("\n==============================================\n")