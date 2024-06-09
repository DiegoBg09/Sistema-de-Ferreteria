class Gasto:
    def __init__(self, sueldos, impuestos, seguros, servicios):
        self.__sueldos = sueldos
        self.__impuestos = impuestos
        self.__seguros = seguros
        self.__servicios = servicios

    def getSueldos(self):
        return self.__sueldos

    def getImpuestos(self):
        return self.__impuestos

    def getSeguros(self):
        return self.__seguros

    def getServicios(self):
        return self.__servicios

    def setSueldos(self, sueldos):
        self.__sueldos = sueldos

    def setImpuestos(self, impuestos):
        self.__impuestos = impuestos

    def setSeguros(self, seguros):
        self.__seguros = seguros

    def setServicios(self, servicios):
        self.__servicios = servicios
