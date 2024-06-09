from Controlador.Gastos import Gasto

class GestionGastos:
    def __init__(self):
        self.dataGastos = []
        self.cargar()

    def cargar(self):
        archivo = open("Modelo/Gasto.txt", "r")
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            sueldos = columna[0]
            impuestos = columna[1]
            seguros = columna[2]
            servicios = columna[3].strip()
            objGto = Gasto(sueldos, impuestos, seguros, servicios)
            self.adicionaGasto(objGto)
        archivo.close()

    def grabar(self):
        archivo = open("Modelo/Gasto.txt", "w")
        for i in range(self.tamanoGestionGasto()):
            archivo.write(
                str(self.devolverGasto(i).getSueldos()) + "," +
                str(self.devolverGasto(i).getImpuestos()) + "," +
                str(self.devolverGasto(i).getSeguros()) + "," +
                str(self.devolverGasto(i).getServicios()) + "\n"
            )
        archivo.close()

    def adicionaGasto(self, objGto):
        self.dataGastos.append(objGto)

    def devolverGasto(self, pos):
        return self.dataGastos[pos]

    def tamanoGestionGasto(self):
        return len(self.dataGastos)

    def eliminarGasto(self, indice):
        del(self.dataGastos[indice])
