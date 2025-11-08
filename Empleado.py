import random
import secrets


class Empleado:
    def __init__(self,**kwargs):
        self.__nombre=kwargs.get("nombre",None)
        self.__puesto=kwargs.get("puesto",None)
        self.__horas=random.randint(30,60)
        self.__pago_hora=random.uniform(20,60)
        self.__bonus=random.uniform(0,30)
        self.__code=secrets.token_hex(8).upper()
        Empleado.__validacion(nombre=self.__nombre,puesto=self.__puesto)

    @staticmethod
    def __validacion(**kwargs):
        if "nombre" in kwargs:
            if kwargs["nombre"] is None or kwargs["nombre"].strip()=="":
                raise ValueError("El nombre no puede estar vacio")
        if "puesto" in kwargs:
            if kwargs["puesto"] not in ["junior","senior","manager"]:
                raise ValueError("El puesto debe ser junior,senior, o manager")

    @property
    def __salario_total(self):
        base=self.__horas*self.__pago_hora
        return base+(base*self.__bonus/100)

    def get_salario_total(self):
        return self.__salario_total

    def get_puesto(self):
        return self.__puesto

    def __str__(self):
        return f"[{self.__code}] {self.__nombre} : {self.__puesto} {round(self.get_salario_total(),2)}"