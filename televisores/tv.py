from marca import Marca
from control import Control

class TV:
    numTV = 0
    def __init__(self, marca:Marca, estado:bool):
        self.__marca = marca
        self.__estado = estado
        self.__canal = 1
        self.__precio = 500
        self.__volumen = 1
        self.__control:Control = None
        TV.numTV += 1

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def canal(self):
        return self.__canal

    @canal.setter
    def canal(self, canal):
        if self.estado == True and canal >=1 and canal <= 120:
            self.__canal = canal

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    @property
    def volumen(self):
        return self.__volumen
    

    @volumen.setter
    def volumen(self, volumen):
        if self.estado == True and 0 <= volumen <= 7:
            self.__volumen = volumen

    @property
    def control(self):
        return self.__control

    @control.setter
    def control(self, control):
        self.__control = control

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    @property
    def estado(self):
        return self.__estado

    def canalUp(self):
        self.setCanal(self.canal + 1)

    def canalDown(self):
        self.setCanal(self.canal - 1)

    def volumenUp(self):
        self.setVolumen(self.volumen + 1)
    
    def volumenDown(self):
        self.setVolumen(self.volumen - 1)
