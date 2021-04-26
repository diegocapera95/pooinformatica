class Producto:
    def __init__(self):
        self.nombre = ""
        self.descripcion = ""
        self.tipo = ""


class Computador(Producto):
    def __init__(self):
        Producto.__init__(self)

class ComputadorGeneral(Computador):
    def __init__(self,mensaje1,mensaje2):
        self.nombre = mensaje1
        self.descripcion = mensaje2
        self.tipo="Computador"
'''
class ComputadorHP(Computador):
    def __init__(self):
        self.nombre = "computador"
        self.descripcion = "HP"
'''
class Partes(Producto):
    def __init__(self):
        Producto.__init__(self)

class PartesGeneral(Partes):
    def __init__(self,mensaje1,mensaje2):
        self.nombre = mensaje1
        self.descripcion = mensaje2
        self.tipo="Parte"
'''
class PartesHP(Partes):
    def __init__(self):
        self.nombre = "Parte"
        self.descripcion = "HP"
'''