from tv import TV

class Control:
    def __init__(self, tv:TV):
        self.tv = tv

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
        self.tv.canal = numero_canal

    def setVolumen(self, numero_volumen):
        self.tv.volumen = numero_volumen
    
    def enlazar(self, tv):
        self.tv = tv
        tv.control = self
