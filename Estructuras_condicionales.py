# Ejemplo 1:
print("Contamos con los productos A y B: Ingrese el que necesite:")
producto= input("Ingrese un producto: ")
cantidad=int(input("Ingrese la cantiad:"))

if producto == "A":
    print("¡Estás comprando el producto A")
    if cantidad > 10:
        print("Podemos ofrecerle un 10% de descuento")
    else: print("No es prosible ofrecerle un descuento")

elif cantidad >= 2:
    print("¡Estás comprando el producto B")
    print("Podemos ofrecerle un 5% de descuento")
else: print("No es prosible ofrecerle un descuento")

#Ejemplo 1:
print("Contamos con los productos A y B: Ingrese el que necesite:")
producto= input("Ingrese un producto:")
cantidad=int(input("Ingrese la cantidad"))

if producto == "A":
    print("¡Estás comprando el producto A")
    if cantidad > 10:
        print("Podemos ofrecerle un 10% de descuento")
    else: print("No es posible ofrecerle un descuento")

elif cantidad >= 2:
    print("¡Estás comprando el producto B")
    print("Podemos ofrecerle un 5% de descuento")
else: print("No es posible ofrecerle un descuento")