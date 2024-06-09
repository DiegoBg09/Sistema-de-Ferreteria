class Inventario:
    def __init__(self, codigo, articulo, descripcion, precio):
        self.__codigo = codigo
        self.__articulo = articulo
        self.__descripcion = descripcion
        self.__precio = precio

    def getCodigo(self):
        return self.__codigo
    
    def getArticulo(self):
        return self.__articulo

    def getDescripcion(self):
        return self.__descripcion

    def getPrecio(self):
        return self.__precio

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def setArticulo(self, articulo):
        self.__articulo = articulo

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def setPrecio(self, precio):
        self.__precio = precio
