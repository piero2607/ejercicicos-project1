Agenda={}
with open("Agenda.txt","r") as f:
    for linea in f:
        nombre,telefono=linea.strip().split(":")
        Agenda[nombre]=telefono
print(f"Datos actuales:")
for nombre,telefono in Agenda.items():
    print(f"{nombre}:{telefono}")
nombre=input(f"ingresa un nombre para verificar si esta en la lista o agregarlo:\n")
if nombre in Agenda:
    print(f"{nombre} ya esta en la lista su telefono es {Agenda[nombre]}")
else:
    telefono=input(f"{nombre} no esta en la lista introduce su nombre para agregarlo..")
    Agenda[nombre]=telefono
    print(f"{nombre} ah sido añadido correctamente")
with open("Agenda_actualizada.txt","w") as f:
    for nombre,telefono in Agenda.items():
        f.write(f"{nombre}:{telefono}\n")