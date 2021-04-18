from productos import *

def funcion_decorador(num): 
    valores=["1","2"]

    def funcion_interior(clase):
        class FabricaExtend (clase):
            if num in valores:
                def crear_montura(self):
                    if num == "1":
                        return MonturaHumanos()
                    else:
                        return MonturaOrcos()
                def crear_cuerpo(self):
                    if num == "1":
                        return CuerpoHumanos()
                    else:
                        return CuerpoOrcos()
            else:
                def crear_montura(self):
                    pass

                def crear_cuerpo(self):
                    pass   
        return FabricaExtend
    return funcion_interior

@funcion_decorador(num = "3")
class Fabrica:
    def crear_arma(self):
        pass

    def crear_escudo(self):
        pass

@funcion_decorador(num = "1")
class FabricaHumanos(Fabrica):
    def crear_arma(self):
        return ArmaHumanos()

    def crear_escudo(self):
        return EscudoHumanos()

@funcion_decorador(num = "2")
class FabricaOrcos(Fabrica):
    def crear_arma(self):
        return ArmaOrcos()

    def crear_escudo(self):
        return EscudoOrcos()