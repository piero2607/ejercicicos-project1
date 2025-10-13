import requests
import random as r
poke_lista=["picachu","bulbasaur","charmander","squirtle","eevee"]
seleccionados=r.sample(poke_lista,3)
aciertos=0
for poke in seleccionados:
    print(f"Adivina el tipo {poke}")
    tipo_ingresado=input("tipo: " ).lower()
    url=f"https://pokeapi.co/api/v2/pokemon/{poke}"
    datos=requests.get(url).json()
    for t in datos["types"]:
        tipos=t["type"]["name"]
        if tipo_ingresado in tipos:
            print("correcto...")
            aciertos+=1
        else:
            print(f"eres tonto...tipo reales:{tipos} ")
    print(f"aciertos: {aciertos}/3")