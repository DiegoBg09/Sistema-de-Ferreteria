from PyQt5 import QtWidgets, uic
from Controlador.GestionProductos import *

aPro = GestionProductos()

class VentanaProductos(QtWidgets.QMainWindow):
    def __init__(self):
        super(VentanaProductos, self).__init__()
        uic.loadUi("UI/VentanaProductos.ui", self)

        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnEditar.clicked.connect(self.editar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnGrabar.clicked.connect(self.grabar)
        self.btnRegresar.clicked.connect(self.regresar)
        self.listar()

    def obtenerCodigo(self):
        return self.txtCodigo.text()
        
    def obtenerArticulo(self):
        return self.txtArticulo.text()
        
    def obtenerDescripcion(self):
        return self.txtDescripcion.text()
        
    def obtenerCategoria(self):
        return self.cboCategoria.currentText()
        
    def obtenerCantidad(self):
        return self.txtCantidad.text()
        
    def obtenerProveedor(self):
        return self.txtProveedor.text()
        
    def obtenerPrecio(self):
        return self.txtPrecio.text()
    
    def limpiarTabla(self):
        self.tblProductos.clearContents()
        self.tblProductos.setRowCount(0)

    def valida(self):
        if self.txtCodigo.text() == "":
            self.txtCodigo.setFocus()
            return "Codigo del Producto...!"
        
        if self.txtArticulo.text() == "":
            self.txtArticulo.setFocus()
            return "Articulo...!"
        
        if self.txtDescripcion.text() == "":
            self.txtDescripcion.setFocus()
            return "Descripcion del Producto...!"
        
        if self.cboCategoria.currentText() == "":
            self.cboCategoria.setCurrentIndex(0)
            return "Categoria del Producto...!"
        
        if self.txtProveedor.text() == "":
            self.txtProveedor.setFocus()
            return "Proveedor del Producto...!"
        
        if self.txtPrecio.text() == "":
            self.txtPrecio.setFocus()
            return "Precio del Producto...!"
        
        else:
            return ""
    
    def listar(self):
        self.tblProductos.setRowCount(aPro.tamanoGestionProducto())
        self.tblProductos.setColumnCount(7)
        for i in range (aPro.tamanoGestionProducto()):
            self.tblProductos.setItem(i, 0, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getCodigo()))
            self.tblProductos.setItem(i, 1, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getArticulo()))
            self.tblProductos.setItem(i, 2, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getDescripcion()))
            self.tblProductos.setItem(i, 3, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getCantidad()))
            self.tblProductos.setItem(i, 4, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getCategoria()))
            self.tblProductos.setItem(i, 5, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getProveedor()))
            self.tblProductos.setItem(i, 6, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getPrecio()))

    def limpiarControles(self):
        self.txtCodigo.clear() 
        self.txtArticulo.clear()
        self.txtDescripcion.clear()
        self.cboCategoria.setCurrentIndex(0)
        self.txtCantidad.clear()
        self.txtProveedor.clear()
        self.txtPrecio.clear()

    def registrar(self):
        if self.valida() == "":
            objPro = Producto(self.obtenerCodigo(), self.obtenerArticulo(), self.obtenerDescripcion(), self.obtenerCategoria(), self.obtenerCantidad(), self.obtenerProveedor(), self.obtenerPrecio())
            codigo = self.obtenerCodigo()
            if aPro.buscarProducto(codigo) == -1:
                aPro.adicionaProducto(objPro)
                aPro.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Producto", "El codigo ingresado ya existe", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Producto", "Error en el " + self.valida(), QtWidgets.QMessageBox.Ok)

    def editar(self):
        if aPro.tamanoGestionProducto() == 0:
            QtWidgets.QMessageBox.information(self,"Modificar Producto", "No existen productos a modificar..!!")
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Modificar Producto", "Ingrese el codigo a modificar")
            pos = aPro.buscarProducto(codigo)
            if pos != -1:
                objProducto = aPro.devolverProducto(pos)
                self.btnEditar.setVisible(False)
                self.btnGrabar.setVisible(True)
                self.txtCodigo.setText(objProducto.getCodigo())
                self.txtCodigo.setVisible(False)
                self.lblCodigo.setVisible(False)
                self.txtArticulo.setText(objProducto.getArticulo())
                self.txtDescripcion.setText(objProducto.getDescripcion())
                self.cboCategoria.setCurrentText(objProducto.getCategoria())
                self.txtCantidad.setText(objProducto.getCantidad())
                self.txtProveedor.setText(objProducto.getProveedor())
                self.txtPrecio.setText(objProducto.getPrecio())

    def grabar(self):
        pos = aPro.buscarProducto(self.obtenerCodigo())
        objProducto = aPro.devolverProducto(pos)
        objProducto.setArticulo(self.obtenerArticulo())
        objProducto.setDescripcion(self.obtenerDescripcion())
        objProducto.setCategoria(self.obtenerCategoria()) 
        objProducto.setCantidad(self.obtenerCantidad())
        objProducto.setProveedor(self.obtenerProveedor())
        objProducto.setPrecio(self.obtenerPrecio())
        self.btnEditar.setVisible(True)
        self.btnGrabar.setVisible(False)
        self.limpiarTabla()
        self.limpiarControles()
        aPro.grabar()
        self.listar()
        self.txtCodigo.setVisible(True)
        self.lblCodigo.setVisible(True)
    
    def eliminar(self):
        if aPro.tamanoGestionProducto() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Producto", "No existen productos a eliminar...!!")
        else:
            fila = self.tblProductos.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                codigo = self.tblProductos.item(indiceFila, 0)
                pos = aPro.buscarProducto(codigo)
                aPro.eliminarProducto(pos)
                aPro.grabar()
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Producto", "Debes seleccionar una fila..!!", QtWidgets.QMessageBox.Ok)

    def regresar(self):
        from Vista.MenuPrincipal import MenuPrincipal
        self.menu_principal = MenuPrincipal()
        self.menu_principal.show()
        self.close()
