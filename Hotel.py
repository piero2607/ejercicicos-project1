import random
import secrets


class Hotel:
    def __init__(self,**kwargs):
        self.__nombre=kwargs.get("nombre",None)
        self.__habitacion=kwargs.get("habitacion",None)
        self.__noches=random.randint(1,7)
        self.__tarifa=random.uniform(30,60)
        self.__descuento=random.uniform(1,100)
        self.__code=secrets.token_hex(8).upper()

    @staticmethod
    def __validacion(**kwargs):
      if "habitacion" in kwargs:
          if kwargs.get("habitacion",None) not in ["doble","individual"]:
              raise ValueError("Tipo de habitacion no valida")
      if "nombre" in kwargs:
          if kwargs.get("nombre",None) is None:
              raise ValueError("El nombre no puede estar vacio")

    @property
    def __descuento_aplicado(self):
        return self.__tarifa - ((self.__tarifa * self.__descuento)/100)

    def get_descuento_aplicado(self):
        return self.__descuento_aplicado

    def get_habitacion(self):
        return self.__habitacion

    def __str__(self):
        return f"[{self.__code}] {self.__nombre} : {self.__habitacion} => [{self.__noches}] noches x [{self.get_descuento_aplicado()}]"