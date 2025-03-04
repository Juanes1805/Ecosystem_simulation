import random
import math

# Clase base para los organismos
class Organismo:
    def __init__(self, x, y, energia):
        self.x = x
        self.y = y
        self.energia = energia

    def seguir_vivo(self):
        return self.energia > 0

    def morir(self):
        self.energia = 0


class Depredador(Organismo):
    def __init__(self, x, y, energia):
        super().__init__(x, y, energia)
    
    def cazar(self):
        pass

    def reproducir(self):
        pass

    def mover(self):
        pass

    def seguir_vivo(self):
        return super().seguir_vivo()
    
    def morir(self):
        return super().morir()

class Presa(Organismo):

    def __init__(self, x, y, energia):
        super().__init__(x, y, energia)

    def reproducir(self):
        pass

    def mover(self):
        pass

    def morir(self):
        return super().morir()
    
    def seguir_vivo(self):
        return super().seguir_vivo()

class Planta(Organismo):

    def regenerar(self):
        pass
