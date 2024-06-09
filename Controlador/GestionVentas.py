from Controlador.Ventas import Venta

class GestionVentas:
    def __init__(self):
        self.dataVentas = []
        self.cargar()

    def cargar(self):
        archivo = open("Modelo/Compra.txt", "r")
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            nro_compra = columna[0]
            id_cliente = columna[1]
            fecha_pago = columna[2]
            modo_pago = columna[3].strip()
            objVen = Venta(nro_compra, id_cliente, fecha_pago, modo_pago)
            self.adicionaVenta(objVen)
        archivo.close()
    
    def grabar(self):
        archivo = open("Modelo/Venta.txt", "w")
        for i in range(self.tamanoGestionVenta()):
            archivo.write(str(self.devolverVenta(i).getNroCompra()) + "," + str(self.devolverVenta(i).getIdCliente()) + "," + str(self.devolverVenta(i).getFechaPago()) + "," + str(self.devolverVenta(i).getModoPago()) + "\n")
        archivo.close()


    def adicionaVenta(self, objVen):
        self.dataVentas.append(objVen)

    def devolverVenta(self, pos):
        return self.dataVentas[pos]

    def tamanoGestionVenta(self):
        return len(self.dataVentas)

    def buscarVenta(self, nro_compra):
        for i in range(self.tamanoGestionVenta()):
            if nro_compra == self.dataVentas[i].getNroCompra():
                return i
        return -1

    def eliminarVenta(self, indice):
        del(self.dataVentas[indice])
