from PyQt5 import QtWidgets, uic
from Controlador.GestionClientes import *

aCli = GestionClientes()

class VentanaClientes(QtWidgets.QMainWindow):
    def __init__(self):
        super(VentanaClientes, self).__init__()
        uic.loadUi("UI/GestionClientes.ui", self)

        self.btnGrabar.setVisible(False)

        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnEditar.clicked.connect(self.editar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnGrabar.clicked.connect(self.grabar)
        self.btnRegresar.clicked.connect(self.regresar)
        self.listar()

    def obtenerIdCliente(self):
        return self.txtIdCliente.text()

    def obtenerNombres(self):
        return self.txtNombres.text()

    def obtenerApellidos(self):
        return self.txtApellidos.text()

    def obtenerDni(self):
        return self.txtDni.text()

    def obtenerGenero(self):
        return self.cboGenero.currentText()

    def obtenerCelular(self):
        return self.txtCelular.text()

    def limpiarTabla(self):
        self.tblClientes.clearContents()
        self.tblClientes.setRowCount(0)

    def valida(self):
        if self.txtIdCliente.text() == "":
            self.txtIdCliente.setFocus()
            return "ID del Cliente...!"

        if self.txtNombres.text() == "":
            self.txtNombres.setFocus()
            return "Nombres...!"

        if self.txtApellidos.text() == "":
            self.txtApellidos.setFocus()
            return "Apellidos del Cliente...!"

        if self.txtDni.text() == "":
            self.txtDni.setFocus()
            return "DNI del Cliente...!"

        if self.cboGenero.currentText() == "":
            self.cboGenero.setCurrentIndex(0)
            return "Género del Cliente...!"

        if self.txtCelular.text() == "":
            self.txtCelular.setFocus()
            return "Celular del Cliente...!"

        else:
            return ""

    def listar(self):
        self.tblClientes.setRowCount(aCli.tamanoGestionCliente())
        self.tblClientes.setColumnCount(6)
        for i in range(aCli.tamanoGestionCliente()):
            self.tblClientes.setItem(i, 0, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getIdCliente()))
            self.tblClientes.setItem(i, 1, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getNombres()))
            self.tblClientes.setItem(i, 2, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getApellidos()))
            self.tblClientes.setItem(i, 3, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getDni()))
            self.tblClientes.setItem(i, 4, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getGenero()))
            self.tblClientes.setItem(i, 5, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getCelular()))

    def limpiarControles(self):
        self.txtIdCliente.clear()
        self.txtNombres.clear()
        self.txtApellidos.clear()
        self.txtDni.clear()
        self.cboGenero.setCurrentIndex(0)
        self.txtCelular.clear()

    def registrar(self):
        if self.valida() == "":
            objCli = Cliente(
                self.obtenerIdCliente(), self.obtenerNombres(), self.obtenerApellidos(),
                self.obtenerDni(), self.obtenerGenero(), self.obtenerCelular()
            )
            id_cliente = self.obtenerIdCliente()
            if aCli.buscarCliente(id_cliente) == -1:
                aCli.adicionaCliente(objCli)
                aCli.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Cliente", "El ID ingresado ya existe", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Error en el " + self.valida(), QtWidgets.QMessageBox.Ok)

    def editar(self):
        if aCli.tamanoGestionCliente() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Cliente", "No existen clientes a modificar..!!")
        else:
            id_cliente, _ = QtWidgets.QInputDialog.getText(self, "Modificar Cliente", "Ingrese el ID a modificar")
            pos = aCli.buscarCliente(id_cliente)
            if pos != -1:
                objCliente = aCli.devolverCliente(pos)
                self.btnEditar.setVisible(False)
                self.btnGrabar.setVisible(True)
                self.txtIdCliente.setText(objCliente.getIdCliente())
                self.txtIdCliente.setVisible(False)
                self.lblId.setVisible(False)
                self.txtNombres.setText(objCliente.getNombres())
                self.txtApellidos.setText(objCliente.getApellidos())
                self.txtDni.setText(objCliente.getDni())
                self.cboGenero.setCurrentText(objCliente.getGenero())
                self.txtCelular.setText(objCliente.getCelular())

    def grabar(self):
        pos = aCli.buscarCliente(self.obtenerIdCliente())
        objCliente = aCli.devolverCliente(pos)
        objCliente.setNombres(self.obtenerNombres())
        objCliente.setApellidos(self.obtenerApellidos())
        objCliente.setDni(self.obtenerDni())
        objCliente.setGenero(self.obtenerGenero())
        objCliente.setCelular(self.obtenerCelular())
        self.btnEditar.setVisible(True)
        self.btnGrabar.setVisible(False)
        self.limpiarTabla()
        self.limpiarControles()
        aCli.grabar()
        self.listar()
        self.txtIdCliente.setVisible(True)
        self.lblId.setVisible(True)

    def eliminar(self):
        if aCli.tamanoGestionCliente() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Cliente", "No existen clientes a eliminar...!!")
        else:
            fila = self.tblClientes.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                id_cliente = self.tblClientes.item(indiceFila, 0)
                pos = aCli.buscarCliente(id_cliente)
                aCli.eliminarCliente(pos)
                aCli.grabar()
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Cliente", "Debes seleccionar una fila..!!", QtWidgets.QMessageBox.Ok)

    def regresar(self):
        from Vista.MenuPrincipal import MenuPrincipal
        self.menu_principal = MenuPrincipal()
        self.menu_principal.show()
        self.close()
