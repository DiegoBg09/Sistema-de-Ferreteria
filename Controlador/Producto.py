class Producto:
    def __init__(self, codigo, articulo, descripcion, categoria, cantidad, proveedor, precio):
        self.__codigo = codigo
        self.__articulo = articulo
        self.__descripcion = descripcion
        self.__categoria = categoria
        self.__cantidad = cantidad
        self.__proveedor = proveedor
        self.__precio = precio

    def getCodigo(self):
        return self.__codigo
    
    def getArticulo(self):
        return self.__articulo

    def getDescripcion(self):
        return self.__descripcion

    def getCategoria(self):
        return self.__categoria

    def getCantidad(self):
        return self.__cantidad

    def getProveedor(self):
        return self.__proveedor

    def getPrecio(self):
        return self.__precio

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def setArticulo(self, articulo):
        self.__articulo = articulo

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def setCategoria(self, categoria):
        self.__categoria = categoria

    def setCantidad(self, cantidad):
        self.__cantidad = cantidad

    def setProveedor(self, proveedor):
        self.__proveedor = proveedor

    def setPrecio(self, precio):
        self.__precio = precio
