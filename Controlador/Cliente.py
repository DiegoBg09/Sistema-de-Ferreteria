class Cliente:
    def __init__(self, id_cliente, nombres, apellidos, dni, genero, celular):
        self.__id_cliente = id_cliente
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__dni = dni
        self.__genero = genero
        self.__celular = celular

    def getIdCliente(self):
        return self.__id_cliente
    
    def getNombres(self):
        return self.__nombres

    def getApellidos(self):
        return self.__apellidos

    def getDni(self):
        return self.__dni

    def getGenero(self):
        return self.__genero

    def getCelular(self):
        return self.__celular

    def setIdCliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def setNombres(self, nombres):
        self.__nombres = nombres

    def setApellidos(self, apellidos):
        self.__apellidos = apellidos

    def setDni(self, dni):
        self.__dni = dni

    def setGenero(self, genero):
        self.__genero = genero

    def setCelular(self, celular):
        self.__celular = celular
