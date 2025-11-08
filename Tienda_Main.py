from Tienda_casa import *
def menu():
    print("\n1. Añadir producto")
    print("2. Ver productos")
    print("3. Filtrar por categoría")
    print("4. Ver total de ventas simuladas")
    print("5. Salir")
def main():
    productos=[]
    continuar=True
    while continuar:
        menu()
        try:
            opcion=int(input("Ingresa una opcion:\n"))
            if opcion==1:
                nombre=input("introduce el nombre del producto:\n").strip()
                print("categoria disponibles: [electronica|ropa|hogar]")
                categoria=input("ingresa la categoria:\n").lower().strip()
                producto=Producto(nombre=nombre,categoria=categoria)
                productos.append(producto)
            elif opcion==2:
                if len(productos)>0:
                    for p in productos:
                        print("los productos:" ,p)
                else:
                    print("No hay productos que mostrar...")
            elif opcion==3:
                if len(productos)>0:
                    categoria = input("Filtrar categoría [electronica | ropa | hogar]:\n").lower().strip()
                    for p in productos:
                        if p.get_categoria()==categoria:
                            print(p)
                        else:
                            print("No hay productos que filtar")
            elif opcion==4:
                if len(productos)>0:
                    total=0
                    for p in productos:
                        total+=p.get_precio_final()
                    print(f"El total de ventas es: {round(total,2)}€")
                else:
                    print("No hay productos registrados")
            elif opcion==5:
                print("Saliendo del programa")
                continuar=False
            else:
                print("Opcion ingresada invalida")
        except ValueError as e:
            print("[Error] =>", e)
main()



