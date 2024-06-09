from PyQt5 import QtWidgets, uic
from Controlador.GestionInventario import *

aInv = GestionInventario()

class VentanaInventario(QtWidgets.QMainWindow):
    def __init__(self):
        super(VentanaInventario, self).__init__()
        uic.loadUi("UI/VentanaInventario.ui", self)

        self.btnAgregar.clicked.connect(self.agregar)
        self.btnEditar.clicked.connect(self.editar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnGrabar.clicked.connect(self.grabar)
        self.btnRegresar.clicked.connect(self.regresar)
        self.btnBuscar.clicked.connect(self.buscar)
        self.listar()

    def obtenerCodigo(self):
        return self.txtCodigo.text()
        
    def obtenerArticulo(self):
        return self.txtArticulo.text()
        
    def obtenerDescripcion(self):
        return self.txtDescripcion.text()
        
    def obtenerPrecio(self):
        return self.txtPrecio.text()
    
    def limpiarTabla(self):
        self.tblInventario.clearContents()
        self.tblInventario.setRowCount(0)

    def valida(self):
        if self.txtCodigo.text() == "":
            self.txtCodigo.setFocus()
            return "Codigo del Inventario...!"
        
        if self.txtArticulo.text() == "":
            self.txtArticulo.setFocus()
            return "Articulo...!"
        
        if self.txtDescripcion.text() == "":
            self.txtDescripcion.setFocus()
            return "Descripcion del Inventario...!"
        
        if self.txtPrecio.text() == "":
            self.txtPrecio.setFocus()
            return "Precio del Inventario...!"
        
        else:
            return ""
    
    def listar(self):
        self.tblInventario.setRowCount(aInv.tamanoGestionInventario())
        self.tblInventario.setColumnCount(4)
        for i in range(aInv.tamanoGestionInventario()):
            self.tblInventario.setItem(i, 0, QtWidgets.QTableWidgetItem(aInv.devolverInventario(i).getCodigo()))
            self.tblInventario.setItem(i, 1, QtWidgets.QTableWidgetItem(aInv.devolverInventario(i).getArticulo()))
            self.tblInventario.setItem(i, 2, QtWidgets.QTableWidgetItem(aInv.devolverInventario(i).getDescripcion()))
            self.tblInventario.setItem(i, 3, QtWidgets.QTableWidgetItem(aInv.devolverInventario(i).getPrecio()))

    def limpiarControles(self):
        self.txtCodigo.clear() 
        self.txtArticulo.clear()
        self.txtDescripcion.clear()
        self.txtPrecio.clear()

    def buscar(self):
        self.limpiarTabla()
        if aInv.tamanoGestionInventario() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Inventario", "No existen productos a consultar....!!!!", QtWidgets.QMessageBox.Ok)
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Consultar Inventario", "Ingrese el codigo a consultar")
            pos = aInv.buscarInventario(codigo)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Inventario", "El codigo ingresado no existe....!!!!", QtWidgets.QMessageBox.Ok)
            else:
                self.tblInventario.setRowCount(1)
                self.tblInventario.setItem(0, 0, QtWidgets.QTableWidgetItem(aInv.devolverInventario(pos).getCodigo()))
                self.tblInventario.setItem(0, 1, QtWidgets.QTableWidgetItem(aInv.devolverInventario(pos).getArticulo()))
                self.tblInventario.setItem(0, 2, QtWidgets.QTableWidgetItem(aInv.devolverInventario(pos).getDescripcion()))
                self.tblInventario.setItem(0, 3, QtWidgets.QTableWidgetItem(aInv.devolverInventario(pos).getPrecio()))


    def agregar(self):
        if self.valida() == "":
            objInv = Inventario(self.obtenerCodigo(), self.obtenerArticulo(), self.obtenerDescripcion(), self.obtenerPrecio())
            codigo = self.obtenerCodigo()
            if aInv.buscarInventario(codigo) == -1:
                aInv.adicionaInventario(objInv)
                aInv.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Inventario", "El codigo ingresado ya existe", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Inventario", "Error en el " + self.valida(), QtWidgets.QMessageBox.Ok)

    def editar(self):
        if aInv.tamanoGestionInventario() == 0:
            QtWidgets.QMessageBox.information(self,"Modificar Inventario", "No existen productos a modificar..!!")
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Modificar Inventario", "Ingrese el codigo a modificar")
            pos = aInv.buscarInventario(codigo)
            if pos != -1:
                objInventario = aInv.devolverInventario(pos)
                self.btnEditar.setVisible(False)
                self.btnGrabar.setVisible(True)
                self.txtCodigo.setText(objInventario.getCodigo())
                self.txtCodigo.setVisible(False)
                self.lblCodigo.setVisible(False)
                self.txtArticulo.setText(objInventario.getArticulo())
                self.txtDescripcion.setText(objInventario.getDescripcion())
                self.txtPrecio.setText(objInventario.getPrecio())

    def grabar(self):
        pos = aInv.buscarInventario(self.obtenerCodigo())
        objInventario = aInv.devolverInventario(pos)
        objInventario.setArticulo(self.obtenerArticulo())
        objInventario.setDescripcion(self.obtenerDescripcion())
        objInventario.setPrecio(self.obtenerPrecio())
        self.btnEditar.setVisible(True)
        self.btnGrabar.setVisible(False)
        self.limpiarTabla()
        self.limpiarControles()
        aInv.grabar()
        self.listar()
        self.txtCodigo.setVisible(True)
        self.lblCodigo.setVisible(True)
    
    def eliminar(self):
        if aInv.tamanoGestionInventario() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Inventario", "No existen productos a eliminar...!!")
        else:
            fila = self.tblInventario.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                codigo = self.tblInventario.item(indiceFila, 0)
                pos = aInv.buscarInventario(codigo)
                aInv.eliminarInventario(pos)
                aInv.grabar()
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Inventario", "Debes seleccionar una fila..!!", QtWidgets.QMessageBox.Ok)

    def regresar(self):
        from Vista.MenuPrincipal import MenuPrincipal
        self.menu_principal = MenuPrincipal()
        self.menu_principal.show()
        self.close()
