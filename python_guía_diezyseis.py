#Ejercicio 16
#Pide el nombre de un producto y su precio. Si el precio es mayor a 1000, aplica un descuento
#del 15% y actualiza el precio. Si es menor o igual, aplica descuento del 5%. Muestra el precio
#final.

print("\n==============================================\n")

name = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))

if precio > 1000:
    print("Descuento del 15%")
    precio = precio - (precio * 0.15)
    print(name)
    print(f"Precio actualizado: {precio:.2f}")

else:
    print("Descuento del 5%")
    precio = precio - (precio * 0.05)
    print(name)
    print(f"Precio actualizado: {precio:.2f}")

print("\n==============================================\n")