#Ejercicio 10
#Pide un carácter (string de un solo carácter). Determina si es vocal (mayúscula o minúscula),
#consonante o no es letra. Usa condicionales y operadores lógicos.

print("\n==============================================\n")

string = input("Ingresa un unico caracter: ")
largo = len(string)

if largo != 1:
    print("Debe ser de un solo caracter")

else:
    if string in "aeiou":
        print("Es una vocal en minúscula.")
    
    elif string in "AEIOU":
        print("Es una vocal en mayúscula.")

    elif string in "bcdfghjklmnñpqrstvwxyz":
        print("Es una consonante en minúscula.")
    
    elif string in "BCDFGHJKLMNÑPQRSTVWXYZ":
        print("Es una consonante en mayúscula")
    
    else:
        print("No es letra.")

print("\n==============================================\n")