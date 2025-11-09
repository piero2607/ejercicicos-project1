from Alumno import *
def menu():
    def menu():
        print("\n1. Añadir alumno")
        print("2. Ver alumnos")
        print("3. Filtrar por curso")
        print("4. Ver media general de notas finales")
        print("5. Salir")
def main():
    alumnos=[]
    continuar=True
    while continuar:
        menu()
        try:
            opcion=int(input("Ingresa una opcion:\n"))
            if opcion==1:
                nombre=input("Ingresa el nombre del alumno:\n").lower()
                print("Cursos disponible:python,java,c++")
                curso=input("Ingresa el curso:\n").lower().strip()
                alumno=Alumno(nombre=nombre,curso=curso)
                alumnos.append(alumno)
            elif opcion==2:
                if len(alumnos)>0:
                    for a in alumnos:
                        print(a)
                else:
                    print("No hay alumnos registrados...")
            elif opcion==3:
                if len(alumnos)>0:
                    curso=input("Curso a filtar(python,java,c++)").lower().strip()
                    for a in alumnos:
                        if a.get_curso()==curso:
                            print(a)
                else:
                    print("No hay alumnos registrados...")
            elif opcion==4:
                if len(alumnos)>0:
                    media=0
                    for a in alumnos:
                        media+=a.get_nota_final()
                    media=media/len(alumnos)
                    print(f"La media de notas es:  {round(media,2)}")
                else:
                    print("No hay alumnos registrados")
            elif opcion==5:
                print("saliendo del sistema...")
                continuar=False
            else:
                print("Opcion invalida vuelve a ingresa una opción valida")
        except ValueError as e:
            print("[Error] =>" ,e )

