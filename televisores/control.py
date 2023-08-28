from televisores.tv import TV

class Control:
    def __init__(self):
        self.__tv = ""

    def getTv(self):
        return self.__tv

    def setTv(self, tv):
        self.__tv = tv
    
    def enlazar(self, tv):
        self.setTv(tv)
        tv.setControl(self)

    def turnOn(self):
        self.getTv().turnOn()
    
    def turnOff(self):
        self.getTv().turnOff()

    def canalUp(self):
        self.getTv().canalUp()

    def canalDown(self):
        self.tgetTv().canalDown()

    def volumenUp(self):
        self.__tv.volumenUp()
    
    def volumenDown(self):
        self.__tv.volumenDown()

    def setCanal(self, numero_canal):
        self.__tv.setCanal(numero_canal)

    def setVolumen(self, numero_volumen):
        self.__tv.setVolumen(numero_volumen)


