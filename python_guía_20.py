#Ejercicio 20 (Completo)
#Crea un programa que pida nombre, edad y ciudad del usuario; pida horas trabajadas y valor
#por hora; calcule el salario bruto; si el salario bruto supera 1000 aplique impuesto del 20%; y si
#la edad es menor a 18 o mayor a 65 aplique un descuento especial adicional del 5%.
#Finalmente debe mostrar nombre, ciudad, edad y salario neto final.

print("\n==============================================\n")

name = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
ciudad = input("Ingrese su ciudad: ")

horas_trabajadas = int(input("Ingrese sus horas trabajadas: "))
valor_hora = int(input("Ingrese el valor de su hora: "))

sueldo = valor_hora * horas_trabajadas 
impuesto = 0

if sueldo > 1000:
    if edad < 18 or edad > 65:
        impuesto = sueldo * 0.15
        sueldo = sueldo - impuesto

    else:
        impuesto = sueldo * 0.20
        sueldo = sueldo - impuesto

print("\n---Datos generales---")
print(f"Nombre: {name}")
print(f"Ciudad: {ciudad}")
print(f"edad: {edad}")
print(f"salario final: {sueldo}")

print("\n==============================================\n")