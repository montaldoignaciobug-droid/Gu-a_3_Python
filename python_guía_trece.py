#Ejercicio 13
#Pide una cadena de texto. Si la longitud de la cadena es mayor a 10, muestra la cadena en
#mayúsculas. Si es menor o iguaal a 10, muestra la cadena en minúsculas. Actualiza la cadena
#con su versión transformada

print("\n==============================================\n")

txt = input("Ingrese una cadena: ")
longitud = len(txt)

if longitud > 10:
    txt = txt.upper()
    print(txt)

else:
    txt = txt.lower()
    print(txt)

print("\n==============================================\n")