from productos import *

class Fabrica:
    def crear_computador(self):
        pass

    def crear_partes(self):
        pass


class FabricaGeneral(Fabrica):
    def crear_computador(self,mensaje1,mensaje2):
        return ComputadorGeneral(mensaje1,mensaje2)

    def crear_partes(self,mensaje1,mensaje2):
        return PartesGeneral(mensaje1,mensaje2)
'''
class FabricaHP(Fabrica):
    def crear_computador(self):
        return ComputadorHP()

    def crear_partes(self):
        return PartesHP()'''