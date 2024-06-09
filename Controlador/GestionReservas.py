from Controlador.Reserva import Reserva

class GestionReservas:
  def __init__(self):
    self.dataReservas = []
    self.cargar()

  def cargar(self):
    archivo = open("Modelo/Reserva.txt", "r")
    for linea in archivo.readlines():
      columna = str(linea).split(",")
      NroPedido = columna[0]
      nombres = columna[1]
      apellidos = columna[2]
      dni = columna[3]
      contacto = columna[4]
      hora = columna[5]
      direccion = columna[6].strip()
      objReserva = Reserva(NroPedido, nombres, apellidos, dni, contacto, hora, direccion)
      self.adicionaReserva(objReserva)
    archivo.close()

  def grabar(self):
    archivo = open("Modelo/Reserva.txt", "w")
    for i in range(self.tamanoGestionReservas()):
      archivo.write(str(self.devolverReserva(i).getNroPedido())+ ","  + str(self.devolverReserva(i).getNombres()) + "," + str(self.devolverReserva(i).getApellidos()) + "," + str(self.devolverReserva(i).getDni()) + "," + str(self.devolverReserva(i).getContacto()) + "," + str(self.devolverReserva(i).getHora()) + "," + str(self.devolverReserva(i).getDireccion()) + "," + "\n")
    archivo.close()

  def adicionaReserva(self, objReserva):
    self.dataReservas.append(objReserva)

  def devolverReserva(self, pos):
    return self.dataReservas[pos]
  
  def tamanoGestionReservas(self):
    return len(self.dataReservas)
  
  def buscarReserva(self, NroPedido):
    for i in range(self.tamanoGestionReservas()):
      if NroPedido == self.dataReservas[i].getNroPedido():
        return i 
    return -1
  
  def eliminarReserva(self, indice):
    del(self.dataReservas[indice])
