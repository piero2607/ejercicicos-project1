def menu():
    print("1.Ingresar un nuevo diccionario")
    print("2.Mostrar todos los diccionarios")
    print("3.salir")
    try:
        return int(input("Ingreas una opccion:\n"))
    except ValueError as e:
        print(e)
def menu_diccionario():
    print("Que tipo deseas ingresar:\n")
    print("1.Entero (int):\n")
    print("2.String (str):\n")
    print("3.Lista (list):\n")
    print("4.Terminar diccionario")
    try:
        return int(input("selecciona tipo de dato:\n"))
    except ValueError as e:
        print(e)

def crear_diccionario():
    nombre=input("Dime el nombre del diccionario:\n")
    custom={"nombre":nombre}
    creando=True
    while creando:
        opcion=menu_diccionario()
        if opcion==1 or opcion=="int":
            clave=input("Dime la clave:\n")
            try:
                valor=int(input("Dime el valor:\n"))
                custom[clave]=valor
            except ValueError as e:
                print("El valor no es entero: " ,e)
        elif opcion==2 or opcion=="str":
            clave=input("ingresa la clave:\n")
            valor=input("Ingresa el valor:\n")
            custom[clave]=valor
        elif opcion==3 or opcion=="list":
            lista=[]
            seguirIngresando=True
            clave=input("Dime el valor de la clave de la lista:\n")
            while seguirIngresando:
                tipo=input("Dime el tipo de dato (int/str):\n").lower()
                if tipo=="int":
                    try:
                        lista.append(int(input("Ingresa el valor entero:\n")))
                    except ValueError as e:
                        print(" el valor no es entero" ,e)
                elif tipo=="str":
                    lista.append(input("Ingresa el valor string:\n"))
                else:
                    print("Tipo ingresado no valido:\n")
                if input("Deseas seguir ingresando (si/no):\n").lower() != "si":
                    seguirIngresando=False
            custom[clave]=lista
        elif opcion==4:
            print(f"Nombre diccionario{nombre} terminado")
            creando=False
        else:
            print("Opcion incorrecta ")
        print(f"Diccionario {nombre} actual" ,custom)
    return custom
def mostar_diccionario(bibliotecas):
    if not bibliotecas:
        print("No hay diccionarios")
        return
    numero_diccionario=1
    for dic in bibliotecas:
        print(f"{numero_diccionario} : {dic["nombre"]}")
        for clave,valor in dic.items():
            if clave!="nombre":
                print(f"{clave}:{valor}")
        numero_diccionario+=1

def main():
    bibliotecas=[]
    continuar=True
    while continuar:
        option=menu()
        if option==1:
            nuevo_diccionario=crear_diccionario()
            bibliotecas.append(nuevo_diccionario)
            print(f"Nuevo diccionario {nuevo_diccionario["nombre"]} se agrego a la biblioteca")
        elif option==2:
            mostar_diccionario(bibliotecas)
        elif option==3:
            print(f"total de diccionarios: {len(bibliotecas)}")
            continuar=False
        else:
            print("opcion no valida")
if __name__ == "__main__":
    main()
