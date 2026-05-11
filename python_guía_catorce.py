#Ejercicio 14
#Pide un número del 1 al 7. Muestra el día de la semana correspondiente (1=Lunes, ...,
#7=Domingo). Si el número está fuera de rango, muestra error. Usa múltiples condiciones.

print("\n==============================================\n")
print("Días de la semana")
num = int(input("Ingresa un número del 1 al 7: "))

if num > 0 and num < 8:
    if num == 1:
        print("1 = Lunes")
    elif num == 2:
        print("2 = Martes")
    
    elif num == 3:
        print("3 = Miercoles")
    
    elif num == 4:
        print("4 = Jueves")
    
    elif num == 5:
        print("5 = Viernes")
    
    elif num == 6:
        print("6 = Sabado")

    else:
        print("7 = Domingo")

else:
    print("Error. Número fuera de rango.")

print("\n==============================================\n")