#Ejercicio 7
#Pide el nombre del usuario y su año de nacimiento. Calcula la edad actual (suponiendo año
#2025). Si la edad es >= 18, muestra "Bienvenido [nombre]". Si no, muestra "Acceso
#restringido".

print("\n==============================================\n")

nombre = input("Ingrese su nombre: ").title()
nombre = nombre.strip()

año = int(input("Ingrese su año de nacimiento: "))

edad = 2025 - año

if edad >= 18:
    print(f"Bienvenido, {nombre}")

else:
    print("Acceso restringido.")

print("\n==============================================\n")