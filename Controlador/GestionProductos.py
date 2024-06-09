from Controlador.Producto import Producto

class GestionProductos:
  def __init__(self):
    self.dataProductos = []
    self.cargar()

  def cargar(self):
    archivo = open("Modelo/Producto.txt", "r")
    for linea in archivo.readlines():
      columna = str(linea).split(",")
      codigo = columna [0]
      articulo = columna[1]
      descripcion = columna[2]
      categoria = columna[3]
      cantidad = columna[4]
      proveedor = columna[5]
      precio = columna[6].strip()
      objPro = Producto(codigo, articulo, descripcion, categoria, cantidad, proveedor, precio)
      self.adicionaProducto(objPro)
    archivo.close()

  def grabar(self):
    archivo = open("Modelo/Producto.txt", "w")
    for i in range(self.tamanoGestionProducto()):
      archivo.write(str(self.devolverProducto(i).getCodigo()) + "," + str(self.devolverProducto(i).getArticulo()) + "," + str(self.devolverProducto(i).getDescripcion()) + "," + str(self.devolverProducto(i).getCategoria()) + "," + str(self.devolverProducto(i).getCantidad()) + "," + str(self.devolverProducto(i).getProveedor()) + "," + str(self.devolverProducto(i).getPrecio()) + "\n")
    archivo.close()

  def adicionaProducto(self, objPro):
    self.dataProductos.append(objPro)

  def devolverProducto(self, pos):
    return self.dataProductos[pos]
  
  def tamanoGestionProducto(self):
    return len(self.dataProductos)
  
  def buscarProducto(self, codigo):
    for i in range(self.tamanoGestionProducto()):
      if codigo == self.dataProductos[i].getCodigo():
        return i 
    return -1
  
  def eliminarProducto(self, indice):
    del(self.dataProductos[indice])