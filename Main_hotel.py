from Hotel import *
def menu():
    print("1. Añadir huésped")
    print("2. Ver los huéspedes")
    print("3. Filtrar los que tengan habitación individual o doble")
    print("4. Suma total del dinero pagado por los huéspedes en mi hotel")
    print("5. Salir")

def main():
    val=True
    huespedes=[]
    while val:
        menu()
        opt=int(input(">> "))
        try:
            if opt==1:
                print("Introduce el nombre\n")
                nombre = input("=>")
                print("Seleciona el tipo de habitacion")
                print("Individual")
                print("Doble")
                Tipo_habitacion=input("=>")
                booking=Hotel(nombre=nombre,habitacion=Tipo_habitacion)
                huespedes.append(booking)
            elif opt==2:
                if len(huespedes)>0:
                    for huesped in huespedes:
                        print(huesped)
                else:
                    print("no hay huespedes registrados")
            elif opt==3:
                if len(huespedes)>0:
                    habitacion=input("Dime el tipo de habitacion individual o doble:\n").lower().strip()
                    for huesped in huespedes:
                        if huesped.get_habitacion()==habitacion:
                            print(huesped)
            elif opt==4:
                if len(huespedes)>0:
                    suma=0
                    for huesped in huespedes:
                        suma+=huesped.get_descuento_aplicado()
                    print("la suma total en dinero es : " ,suma)
            elif opt==5:
                val=False
            else:
                print("opcion no valida")
        except ValueError as e:
            print("[Error]", e, sep="=>" )

main()