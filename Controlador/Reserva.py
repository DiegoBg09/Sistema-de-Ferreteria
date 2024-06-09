class Reserva:
    def __init__(self, nombres, apellidos, dni, contacto, hora, direccion, NroPedido):
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__dni = dni
        self.__contacto = contacto
        self.__hora = hora
        self.__direccion = direccion
        self.__NroPedido = NroPedido

    def getNombres(self):
        return self.__nombres

    def getApellidos(self):
        return self.__apellidos

    def getDni(self):
        return self.__dni

    def getContacto(self):
        return self.__contacto

    def getHora(self):
        return self.__hora

    def getDireccion(self):
        return self.__direccion

    def getNroPedido(self):
        return self.__NroPedido

    def setNombres(self, nombres):
        self.__nombres = nombres

    def setApellidos(self, apellidos):
        self.__apellidos = apellidos

    def setDni(self, dni):
        self.__dni = dni

    def setContacto(self, contacto):
        self.__contacto = contacto

    def setHora(self, hora):
        self.__hora = hora

    def setDireccion(self, direccion):
        self.__direccion = direccion

    def setNroPedido(self, NroPedido):
        self.__NroPedido = NroPedido
