from Controlador.Inventario import Inventario

class GestionInventario:
  def __init__(self):
    self.dataInventario = []
    self.cargar()

  def cargar(self):
    archivo = open("Modelo/Inventario.txt", "r")
    for linea in archivo.readlines():
      columna = str(linea).split(",")
      codigo = columna[0]
      articulo = columna[1]
      descripcion = columna[2]
      precio = columna[3].strip()
      objInv = Inventario(codigo, articulo, descripcion, precio)
      self.adicionaInventario(objInv)
    archivo.close()

  def grabar(self):
    archivo = open("Modelo/Inventario.txt", "w")
    for i in range(self.tamanoGestionInventario()):
      archivo.write(str(self.devolverInventario(i).getCodigo()) + "," + str(self.devolverInventario(i).getArticulo()) + "," + str(self.devolverInventario(i).getDescripcion()) + "," + str(self.devolverInventario(i).getPrecio()) + "\n")
    archivo.close()

  def adicionaInventario(self, objInv):
    self.dataInventario.append(objInv)

  def devolverInventario(self, pos):
    return self.dataInventario[pos]
  
  def tamanoGestionInventario(self):
    return len(self.dataInventario)
  
  def buscarInventario(self, codigo):
    for i in range(self.tamanoGestionInventario()):
      if codigo == self.dataInventario[i].getCodigo():
        return i 
    return -1
  
  def eliminarInventario(self, indice):
    del(self.dataInventario[indice])