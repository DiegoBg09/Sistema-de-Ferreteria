from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTime
from Controlador.GestionReservas import *

aRes = GestionReservas()

class VentanaReservas(QtWidgets.QMainWindow):
    def __init__(self):
        super(VentanaReservas, self).__init__()
        uic.loadUi("UI/VentanaReservas.ui", self)

        self.btnReservar.clicked.connect(self.reservar)
        self.btnEditar.clicked.connect(self.editar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnGrabar.clicked.connect(self.grabar)
        self.btnRegresar.clicked.connect(self.regresar)
        self.listar()
        
    def obtenerNombres(self):
        return self.txtNombres.text()
        
    def obtenerApellidos(self):
        return self.txtApellidos.text()
        
    def obtenerDni(self):
        return self.txtDni.text()
        
    def obtenerContacto(self):
        return self.txtContacto.text()

    def obtenerNroPedido(self):
        return self.txtNroPedido.text()
        
    def obtenerHora(self):
        return self.tmeHora.time().toString("HH:mm")
        
    def obtenerDireccion(self):
        return self.txtDireccion.text()
    
    def limpiarTabla(self):
        self.tblReservas.clearContents()
        self.tblReservas.setRowCount(0)

    def valida(self):
        if self.txtNroPedido.text() == "":
            self.txtNroPedido.setFocus()
            return "Número de Pedido...!"
        
        if self.txtNombres.text() == "":
            self.txtNombres.setFocus()
            return "Nombres...!"
        
        if self.txtApellidos.text() == "":
            self.txtApellidos.setFocus()
            return "Apellidos...!"
        
        if self.txtDni.text() == "":
            self.txtDni.setFocus()
            return "DNI...!"
        
        if self.txtContacto.text() == "":
            self.txtContacto.setFocus()
            return "Contacto...!"
        
        if self.tmeHora.time() == QTime(0, 0):
            self.tmeHora.setFocus()
            return "Hora...!"
        
        if self.txtDireccion.text() == "":
            self.txtDireccion.setFocus()
            return "Dirección...!"
        
        else:
            return ""
    
    def listar(self):
        self.tblReservas.setRowCount(aRes.tamanoGestionReservas())
        self.tblReservas.setColumnCount(7)
        for i in range(aRes.tamanoGestionReservas()):
            self.tblReservas.setItem(i, 0, QtWidgets.QTableWidgetItem(aRes.devolverReserva(i).getApellidos()))
            self.tblReservas.setItem(i, 1, QtWidgets.QTableWidgetItem(aRes.devolverReserva(i).getDni()))
            self.tblReservas.setItem(i, 2, QtWidgets.QTableWidgetItem(aRes.devolverReserva(i).getContacto()))
            self.tblReservas.setItem(i, 3, QtWidgets.QTableWidgetItem(aRes.devolverReserva(i).getHora()))
            self.tblReservas.setItem(i, 4, QtWidgets.QTableWidgetItem(aRes.devolverReserva(i).getDireccion()))
            self.tblReservas.setItem(i, 5, QtWidgets.QTableWidgetItem(aRes.devolverReserva(i).getNroPedido()))
            self.tblReservas.setItem(i, 6, QtWidgets.QTableWidgetItem(aRes.devolverReserva(i).getNombres()))


    def limpiarControles(self):
        self.txtNroPedido.clear() 
        self.txtNombres.clear()
        self.txtApellidos.clear()
        self.txtDni.clear()
        self.txtContacto.clear()
        self.tmeHora.clear()
        self.txtDireccion.clear()

    def reservar(self):
        if self.valida() == "":
            objRes = Reserva(self.obtenerNroPedido(), self.obtenerNombres(), self.obtenerApellidos(), self.obtenerDni(), self.obtenerContacto(), self.obtenerHora(), self.obtenerDireccion())
            NroPedido = self.obtenerNroPedido()
            if aRes.buscarReserva(NroPedido) == -1:
                aRes.adicionaReserva(objRes)
                aRes.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Reserva", "El número de pedido ingresado ya existe", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Reserva", "Error en el " + self.valida(), QtWidgets.QMessageBox.Ok)

    def editar(self):
        if aRes.tamanoGestionReservas() == 0:
            QtWidgets.QMessageBox.information(self,"Modificar Reserva", "No existen reservas a modificar..!!")
        else:
            NroPedido, _ = QtWidgets.QInputDialog.getText(self, "Modificar Reserva", "Ingrese el número de pedido a modificar")
            pos = aRes.buscarReserva(NroPedido)
            if pos != -1:
                objReserva = aRes.devolverReserva(pos)
                self.btnEditar.setVisible(False)
                self.btnGrabar.setVisible(True)
                self.txtNroPedido.setText(objReserva.getNroPedido())
                self.txtNroPedido.setVisible(False)
                self.lblNroPedido.setVisible(False)
                self.txtNombres.setText(objReserva.getNombres())
                self.txtApellidos.setText(objReserva.getApellidos())
                self.txtDni.setText(objReserva.getDni())
                self.txtContacto.setText(objReserva.getContacto())
                self.tmeHora.setTime(QTime.fromString(objReserva.getHora(), "HH:mm"))
                self.txtDireccion.setText(objReserva.getDireccion())

    def grabar(self):
        pos = aRes.buscarReserva(self.obtenerNroPedido())
        objReserva = aRes.devolverReserva(pos)
        objReserva.setNombres(self.obtenerNombres())
        objReserva.setApellidos(self.obtenerApellidos())
        objReserva.setDni(self.obtenerDni()) 
        objReserva.setContacto(self.obtenerContacto())
        objReserva.setHora(self.obtenerHora())
        objReserva.setDireccion(self.obtenerDireccion())
        self.btnEditar.setVisible(True)
        self.btnGrabar.setVisible(False)
        self.limpiarTabla()
        self.limpiarControles()
        aRes.grabar()
        self.listar()
        self.txtNroPedido.setVisible(True)
        self.lblNroPedido.setVisible(True)
    
    def eliminar(self):
        if aRes.tamanoGestionReservas() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Reserva", "No existen reservas a eliminar...!!")
        else:
            fila = self.tblReservas.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                NroPedido = self.tblReservas.item(indiceFila, 0)
                pos = aRes.buscarReserva(NroPedido)
                aRes.eliminarReserva(pos)
                aRes.grabar()
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Reserva", "Debes seleccionar una fila..!!", QtWidgets.QMessageBox.Ok)

    def regresar(self):
        from Vista.MenuPrincipal import MenuPrincipal
        self.menu_principal = MenuPrincipal()
        self.menu_principal.show()
        self.close()
