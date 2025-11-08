def menu():
    opcion = int(input("1.entero (int):\n"
                   "2.string (str):\n"
                   "3.lista (list):\n"
                   "4.salir:..."))
    print("Diccionario custom...")
    continuar=True
    custom={}
    while continuar:
        option=menu()
        if option==1:
            clave=input("Dime la clave:\n")
            valor=int(input("Dime el valor (int):\n"))
            custom[clave]=valor
        elif opcion==2:
            clave=input("Dime la clave:\n")
            valor=input("Dime el valor:\n")
            custom[clave]=valor
        elif option==3:
            seguirIngresando=True
            clave=input("Dime la clave:\\n")
            lista=[]
            while seguirIngresando:
                tipo=input("Que tipo deseas ingresar(int/str):\n")
                if tipo=="int":
                    lista.append(int(input("Dime el valor entero:\n")))
                else:
                    lista.append(input("Dime el valor string:\n"))
                if input("Deseas seguir ingresando valores a la lista (si/no):\n") !="si":
                    seguirIngresando=False
            custom[clave]=lista
        elif option==4:
            continuar=False
        else:
            print("opcion ingresada invalida....")

        print("diccionaro actual",custom)
    print("fin del diccionario custpom...")
    print("diccionario final" ,custom)
