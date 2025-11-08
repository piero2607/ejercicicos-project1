import random
import secrets


<<<<<<< HEAD
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
=======
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


>>>>>>> 0ca8a6a (practicando 08/11/2025)
