import requests
import random

lista_paises=["afghanistan", "albania", "algeria", "andorra", "angola", "antigua and barbuda", "argentina",
    "armenia", "australia", "austria", "azerbaijan", "bahamas", "bahrain", "bangladesh", "barbados",
    "belarus", "belgium", "belize", "benin", "bhutan", "bolivia", "bosnia and herzegovina",
    "botswana", "brazil", "brunei", "bulgaria", "burkina faso", "burundi", "cabo verde",
    "cambodia", "cameroon", "canada", "central african republic", "chad", "chile", "china",
    "colombia", "comoros", "congo (brazzaville)", "congo (kinshasa)", "costa rica", "croatia",
    "cuba", "cyprus", "czechia", "denmark", "djibouti", "dominica", "dominican republic", "ecuador",
    "egypt", "el salvador", "equatorial guinea", "eritrea", "estonia", "eswatini", "ethiopia",
    "fiji", "finland", "france", "gabon", "gambia", "georgia", "germany", "ghana", "greece",
    "grenada", "guatemala", "guinea", "guinea-bissau", "guyana", "haiti", "honduras", "hungary",
    "iceland", "india", "indonesia", "iran", "iraq", "ireland", "israel", "italy", "ivory coast",
    "jamaica", "japan", "jordan", "kazakhstan", "kenya", "kiribati", "kosovo", "kuwait", "kyrgyzstan",
    "laos", "latvia", "lebanon", "lesotho", "liberia", "libya", "liechtenstein", "lithuania",
    "luxembourg", "madagascar", "malawi", "malaysia", "maldives", "mali", "malta", "marshall islands",
    "mauritania", "mauritius", "mexico", "micronesia", "moldova", "monaco", "mongolia", "montenegro",
    "morocco", "mozambique", "myanmar", "namibia", "nauru", "nepal", "netherlands", "new zealand",
    "nicaragua", "niger", "nigeria", "north korea", "north macedonia", "norway", "oman", "pakistan",
    "palau", "palestine", "panama", "papua new guinea", "paraguay", "peru", "philippines", "poland",
    "portugal", "qatar", "romania", "russia", "rwanda", "saint kitts and nevis", "saint lucia",
    "saint vincent and the grenadines", "samoa", "san marino", "sao tome and principe",
    "saudi arabia", "senegal", "serbia", "seychelles", "sierra leone", "singapore", "slovakia",
    "slovenia", "solomon islands", "somalia", "south africa", "south korea", "south sudan",
    "spain", "sri lanka", "sudan", "suriname", "sweden", "switzerland", "syria", "taiwan", "tajikistan",
    "tanzania", "thailand", "timor-leste", "togo", "tonga", "trinidad and tobago", "tunisia",
    "turkey", "turkmenistan", "tuvalu", "uganda", "ukraine", "united arab emirates",
    "united kingdom", "united states", "uruguay", "uzbekistan", "vanuatu", "vatican city",
    "venezuela", "vietnam", "yemen", "zambia", "zimbabwe"]
pais_aleatorio=random.randint(0,len(lista_paises)-1)
pais=lista_paises[pais_aleatorio]
url=f"https://restcountries.com/v3.1/name/{pais}"
datos=requests.get(url).json()
pais_json=datos[0]["name"]["common"]
capital=datos[0]["capital"][0]
print(capital)
intentos=3
continuar=True
while intentos>0 and continuar:
    print(f"pais: {pais_json}\n")
    capital_intento=input(f"Dime la capital de {pais_json}:\n")
    if capital_intento.lower()==capital.lower():
        print("En hora buena paquete...")
        continuar=False
    else:
        intentos-=1
        if intentos>0:
            print(f"sigue intentando aun te quedan intentos... {intentos}")
        else:
            print(f"Eres un paquete la capital de {pais_json} era: {capital}")

