import random
import secrets


class Alumno:
    def __init__(self,**kwargs):
        self.__nombre=kwargs.get("nombre",None)
        self.__curso=kwargs.get("curso",None)
        self.__nota=random.uniform(0,10)
        self.__beca=random.uniform(0,100)
        self.__code=secrets.token_hex(4).upper()
        Alumno.__validar(nombre=self.__nombre,curso=self.__curso)

    @staticmethod
    def __validar(**kwargs):
        if "nombre" in kwargs:
            if kwargs["nombre"] is None or kwargs["nombre"].strip() =="":
                raise ValueError("El nombre no puede estar  en vacio")
        if "curso" in kwargs:
            if kwargs["curso"] not in ["python","java","c++"]:
                raise ValueError("Cursso no valido:opciones(python,java,c++)")

    @property
    def nota_final(self):
        resultado=self.__nota+(self.__nota*self.__beca/100)
        if resultado>10:
            return 10
        else:
            return round(resultado,2)

    def get_nota_final(self):
        return self.nota_final

    def get_curso(self):
        return self.__curso

    def __str__(self):
        return f"[{self.__code}] {self.__nombre} => {self.__curso} {self.nota_final} (beca:{round(self.__beca),1}%)"

