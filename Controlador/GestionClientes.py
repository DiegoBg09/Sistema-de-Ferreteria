from Controlador.Cliente import Cliente

class GestionClientes:
    def __init__(self):
        self.dataClientes = []
        self.cargar()

    def cargar(self):
        archivo = open("Modelo/Cliente.txt", "r")
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            id_cliente = columna[0]
            nombres = columna[1]
            apellidos = columna[2]
            dni = columna[3]
            genero = columna[4]
            celular = columna[5].strip()
            objCli = Cliente(id_cliente, nombres, apellidos, dni, genero, celular)
            self.adicionaCliente(objCli)
        archivo.close()

    def grabar(self):
        archivo = open("Modelo/Cliente.txt", "w")
        for i in range(self.tamanoGestionCliente()):
            archivo.write(
                str(self.devolverCliente(i).getIdCliente()) + "," +
                str(self.devolverCliente(i).getNombres()) + "," +
                str(self.devolverCliente(i).getApellidos()) + "," +
                str(self.devolverCliente(i).getDni()) + "," +
                str(self.devolverCliente(i).getGenero()) + "," +
                str(self.devolverCliente(i).getCelular()) + "\n"
            )
        archivo.close()

    def adicionaCliente(self, objCli):
        self.dataClientes.append(objCli)

    def devolverCliente(self, pos):
        return self.dataClientes[pos]

    def tamanoGestionCliente(self):
        return len(self.dataClientes)

    def buscarCliente(self, id_cliente):
        for i in range(self.tamanoGestionCliente()):
            if id_cliente == self.dataClientes[i].getIdCliente():
                return i
        return -1

    def eliminarCliente(self, indice):
        del self.dataClientes[indice]
