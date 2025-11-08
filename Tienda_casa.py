import random
import secrets

class Producto:
    def __init__(self,**kwargs):
        self.__nombre=kwargs.get("nombre",None)
        self.__categoria=kwargs.get("categoria",None)
        self.__precio_base=random.uniform(10,100)
        self.__descuento=random.uniform(1,50)
        self.__code=secrets.token_hex(5).upper()
        Producto.__validacion(nombre=self.__nombre,categoria=self.__categoria)
    @staticmethod
    def __validacion(**kwargs):
        if "nombre" in kwargs:
            if kwargs["nombre"] is None or kwargs["nombre"].strip()=="":
                raise ValueError("el nombre no puede estar vacio")
        if "categoria" in kwargs:
            if kwargs["categoria"] not in ["electronica","ropa","hogar"]:
                raise ValueError("categoria no valida")
    @property
    def precio_final(self):
        return self.__precio_base*(1-self.__descuento/100)

    def get_precio_final(self):
        return self.precio_final

    def get_categoria(self):
        return self.__categoria

    def __str__(self):
        return f"[{self.__code}] {self.__nombre}: {self.__categoria} => {round(self.get_precio_final(),2)}"
