class TV:
    numTV = 0
    def __init__(self, marca, estado:bool):
        self.__marca = marca
        self.__estado = estado
        self.__canal = 1
        self.__precio = 500
        self.__volumen = 1
        self.__control = None
        TV.numTV += 1

    def getMarca(self):
        return self.__marca

    def setMarca(self, marca):
        self.__marca = marca

    def getCanal(self):
        return self.__canal

    def setCanal(self, canal):
        if self.__estado == True and canal >=1 and canal <= 120:
            self.__canal = canal

    def getPrecio(self):
        return self.__precio

    def setPrecio(self, value):
        self.__precio = value

    def getVolumen(self):
        return self.__volumen
    
    def setVolumen(self, volumen):
        if self.__estado == True and 0 <= volumen <= 7:
            self.__volumen = volumen

    def getControl(self):
        return self.__control

    def setControl(self, control):
        self.__control = control

    def getEstado(self):
        return self.__estado

    def setEstado(self, estado):
        self.__estado = estado

    def turnOn(self):
        self.setEstado(True)

    def turnOff(self):
        self.setEstado(False)

    def canalUp(self):
        self.setCanal(self.getCanal() + 1)

    def canalDown(self):
        self.setCanal(self.getCanal() - 1)

    def volumenUp(self):
        self.setVolumen(self.getVolumen() + 1)
    
    def volumenDown(self):
        self.setVolumen(self.getVolumen() - 1)

    @staticmethod
    def getNumTV(self):
        return self.numTV
    
    @staticmethod
    def setNumTV(numTV):
        TV.numTV = numTV
