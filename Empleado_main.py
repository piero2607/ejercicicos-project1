from Empleado import *


def menu():
    print("\n1. Añadir empleado")
    print("2. Ver empleados")
    print("3. Filtrar empleados por puesto")
    print("4. Ver total de gasto en sueldos")
    print("5. Salir")

def main():
    empleados=[]
    continuar=True
    while continuar:
        menu()
        try:
            opcion=int(input("Introduce una opcion:\n"))
            if opcion==1:
                nombre=input("introduce el nombre del empleado:\n").strip()
                print("Puestos disponibles: junior | senior | manager")
                puesto=input("introduce un puesto:\n").lower().strip()
                empleado=Empleado(nombre=nombre,puesto=puesto)
                empleados.append(empleado)
            elif opcion==2:
                if len(empleados)>0:
                    for e in empleados:
                        print(e)
                else:
                    print("no hay empleados registrados...")
            elif opcion==3:
                if len(empleados)>0:
                    puesto = input("Filtrar por puesto (junior/senior/manager):\n>> ").lower().strip()
                    for e in empleados:
                        if e.get_puesto()==puesto:
                            print(e)
                else:
                    print("No hay empleados patra filtar")
            elif opcion==4:
                if len(empleados)>0:
                    total=0
                    for e in empleados:
                        total+=e.get_salario_total()
                    print(f"El total de sueldos pagados es: {round(total,2)},€")
            elif opcion==5:
                continuar=False
            else:
                print("opcion ingresada invalida")
        except ValueError as e:
            print("[EROOR] => ", e)



main()