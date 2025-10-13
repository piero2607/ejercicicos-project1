cambio_divisas=[
    ["bolivar venezolano",202.78],
    ["guaraní paraguayo",8_336.03],
    ["peso argentino",1_564.31],
    ["peso boliviano",8.0736],
    ["peso chileno",1_120.74],
    ["peso colombiano",4_562.79],
    ["peso uruguayo",46.602],
    ["real brasileño",6.2661],
    ["sol peruano",4.0908]]
pais_cambio=input('Dime la moneda del  pais en el cual quieres hacer el cambio:\n').lower()
cambio=False
for i in range(len(cambio_divisas)):
    if pais_cambio == cambio_divisas[i][0]:
        euros = float(input('Dime la cantida de euros:\n'))
        cambio = euros * cambio_divisas[i][1]
        print(f"el cambio de {pais_cambio}  es: {cambio:.2f}")
        cambio=True
if not cambio:
    print('la moneda no esta en lista')

