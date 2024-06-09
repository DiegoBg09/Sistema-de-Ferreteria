class Venta:
    def __init__(self, nro_compra, id_cliente, fecha_pago, modo_pago):
        self.__nro_compra = nro_compra
        self.__id_cliente = id_cliente
        self.__fecha_pago = fecha_pago
        self.__modo_pago = modo_pago

    def getNroCompra(self):
        return self.__nro_compra
    
    def getIdCliente(self):
        return self.__id_cliente

    def getFechaPago(self):
        return self.__fecha_pago

    def getModoPago(self):
        return self.__modo_pago

    def setNroCompra(self, nro_compra):
        self.__nro_compra = nro_compra

    def setIdCliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def setFechaPago(self, fecha_pago):
        self.__fecha_pago = fecha_pago

    def setModoPago(self, modo_pago):
        self.__modo_pago = modo_pago