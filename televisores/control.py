from televisores.tv import TV

class Control:
    def __init__(self):
        self.__tv = ""

    def turnOn(self):
        self.tv.turnOn()
    
    def turnOff(self):
        self.tv.turnOff()

    def canalUp(self):
        self.tv.canalUp()

    def canalDown(self):
        self.tv.canalDown()

    def volumenUp(self):
        self.tv.volumenUp()
    
    def volumenDown(self):
        self.tv.volumenDown()

    def setCanal(self, numero_canal):
        self.tv.setCanal(numero_canal)

    def setVolumen(self, numero_volumen):
        self.tv.setVolumen(numero_volumen)

    def getTv(self):
        return self.__tv

    def setTv(self, tv):
        self.__tv = tv
    
    def enlazar(self, tv):
        self.setTv(tv)
        tv.setControl(self)
