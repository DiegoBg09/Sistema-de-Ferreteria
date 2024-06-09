from Controlador.Proveedor import Proveedor

class GestionProveedor:
    def __init__(self):
        self.dataProveedor = []
        self.cargar()

    def cargar(self):
        archivo = open("Modelo/Proveedor.txt", "r") 
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            proveedor = columna[0]
            correo = columna[1]
            ruc = columna[2]
            fecha_salida = columna[3]
            suministro = columna[4]
            fecha_entrega = columna[5]
            contacto = columna[6]
            estado = columna[7].strip() 
            objPrv = Proveedor(proveedor, correo, ruc, fecha_salida, suministro, fecha_entrega, contacto, estado)
            self.adicionaProveedor(objPrv)
        archivo.close()

    def grabar(self):
        archivo = open("Modelo/Proveedor.txt", "w")
        for i in range(self.tamanoGestionProveedor()):
            archivo.write(
                str(self.devolverProveedor(i).getProveedor()) + "," +
                str(self.devolverProveedor(i).getCorreo()) + "," +
                str(self.devolverProveedor(i).getRuc()) + "," +
                str(self.devolverProveedor(i).getFechaSalida()) + "," +
                str(self.devolverProveedor(i).getSuministro()) + "," +
                str(self.devolverProveedor(i).getFechaEntrega()) + "," +
                str(self.devolverProveedor(i).getContacto()) + "," +
                str(self.devolverProveedor(i).getEstado()) + "\n"
            )
        archivo.close()

    def adicionaProveedor(self, objPro):
        self.dataProveedor.append(objPro)

    def devolverProveedor(self, pos):
        return self.dataProveedor[pos]

    def tamanoGestionProveedor(self):
        return len(self.dataProveedor)

    def buscarProveedor(self, proveedor):
        for i in range(self.tamanoGestionProveedor()):
            if proveedor == self.dataProveedor[i].getProveedor():
                return i
        return -1

    def eliminarProveedor(self, indice):
        del (self.dataProveedor[indice])
