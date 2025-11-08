
from Tienda_casa import *
val=True
carrito=[]
while val:
    print("1. Añadir carrito al producto")
    print("2. ver mi carrito")
    print("3. ver productosi esta activo")
    print("4.salir")
    opcion=int(input("Opcion:\n"))
    try:
        if opcion==1:
            name=input("name:\n")
            price=float(input("price:\n"))
            producto=Tienda(name,price)
            carrito.append(producto)
        elif opcion==2:
            if len(carrito)==0:
                print("el carrito esta vacio")
            else:
                for producto in carrito:
                    print(producto)
        elif opcion==3:
            if len(carrito)==0:
                print("el carrito esta vacio")
            else:
                for producto in carrito:
                    print(producto.isActive)
        elif opcion==4:
            val=False
        else:
            print("opcion no valida")
    except ValueError as e:
        print("[error]", e , sep="=>")
    except:
        print("[error desconocido]")


