class Proveedor:
    def __init__(self, proveedor, correo, ruc, fecha_salida, suministro, fecha_entrega, contacto, estado):
        self.__proveedor = proveedor
        self.__correo = correo
        self.__ruc = ruc
        self.__fecha_salida = fecha_salida
        self.__suministro = suministro
        self.__fecha_entrega = fecha_entrega
        self.__contacto = contacto
        self.__estado = estado

    def getProveedor(self):
        return self.__proveedor

    def getCorreo(self):
        return self.__correo

    def getRuc(self):
        return self.__ruc

    def getFechaSalida(self):
        return self.__fecha_salida

    def getSuministro(self):
        return self.__suministro

    def getFechaEntrega(self):
        return self.__fecha_entrega

    def getContacto(self):
        return self.__contacto

    def getEstado(self):
        return self.__estado

    def setProveedor(self, proveedor):
        self.__proveedor = proveedor

    def setCorreo(self, correo):
        self.__correo = correo

    def setRuc(self, ruc):
        self.__ruc = ruc

    def setFechaSalida(self, fecha_salida):
        self.__fecha_salida = fecha_salida

    def setSuministro(self, suministro):
        self.__suministro = suministro

    def setFechaEntrega(self, fecha_entrega):
        self.__fecha_entrega = fecha_entrega

    def setContacto(self, contacto):
        self.__contacto = contacto

    def setEstado(self, estado):
        self.__estado = estado
