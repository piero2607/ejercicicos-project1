import random
import secrets


class Tienda:
    def __init__(self,name,price):
        self.__validar(name,price)
        self.__name=name
        self.__price=price
        self.__stock=self.__generar_stock()


    def __validar(self,name,price):
        self.__comprobar_nombre(name)
        self.__comprobar_precio(price)

    @staticmethod
    def __comprobar_nombre(name):
        if name=="":
            raise ValueError("El titulo no puede estar vacio..")
        if name.isnumeric():
            raise ValueError("El titulo no puede ser numerico")
        if len(name)<3:
            raise ValueError("El titulo debe tener mas de 3 caracteres")

    @property
    def __code(self):
        return secrets.token_hex(16)

    @staticmethod
    def __generar_stock():
        return random.randint(0,1)

    @property
    def isActive(self):
        if self.__stock>0:
            return True
        return False
    @staticmethod
    def __comprobar_precio(price):
        if price<=0:
            raise ValueError("El precio debe ser un numero positivo")


    def __str__(self):
        return f"[{self.__code}] {self.__name} -> {self.__price}€ (stock: {self.__stock})"
