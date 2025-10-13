Correos={}
with open("Correos.txt","r") as f:
    for linea in f:
        correo,nombre=linea.strip().split(":")
        Correos[correo]=nombre
for correo,nombre in Correos.items():
    print(f"{correo}:{nombre}")
entrada=input(f"introduceun nombre para verificar su correo:\n".lower())
if entrada in Correos:
    print(f"el correo ya esta registrado{Correos[entrada]}")
else:
    nombre=input(f"aun no esta registrado dame el correo para agregarlo a la lista:\n")
    Correos[entrada]=nombre
    print(f"{entrada} ah sido registrado {nombre}")
with open(f"correos actualizados.txt","w") as f:
    for correo,nombre in Correos.items():
        f.write(f"{correo}:{nombre}\n")