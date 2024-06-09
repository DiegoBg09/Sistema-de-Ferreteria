from PyQt5 import QtWidgets, uic
from Vista.ventanaProductos import VentanaProductos
from Vista.ventanaClientes import VentanaClientes
from Vista.ventanaReservas import VentanaReservas
from Vista.ventanaProveedores import VentanaProveedores
from Vista.ventanaInventario import VentanaInventario
from Vista.ventanaVentas import GestionVenta
from Vista.ventanaHistorialVentas import HistorialVentas
from Vista.ventanaPuntoVenta import VentanaPuntoVenta

qtCreatorFile = "UI/login.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MenuPrincipal(QtWidgets.QMainWindow):
        def __init__(self, parent = None):
                super(MenuPrincipal, self).__init__(parent)
                uic.loadUi("UI/MenuPrincipal.ui", self)

                self.btnProductos.clicked.connect(self.open_gestion_productos)
                self.btnInventario.clicked.connect(self.open_gestion_inventario)
                self.btnProveedores.clicked.connect(self.open_gestion_proveedores)
                self.btnPuntoVenta.clicked.connect(self.open_punto_venta)
                self.btnClientes.clicked.connect(self.open_gestion_clientes)
                self.btnVentas.clicked.connect(self.open_gestion_ventas)
                self.btnReservas.clicked.connect(self.open_gestion_reservas)
                self.btnHistorial.clicked.connect(self.open_historial_ventas)
                self.btnCerrarSesion.clicked.connect(self.open_cerrar_sesion)
                self.show()

        def open_gestion_productos(self):
             self.gestion_productos = VentanaProductos()
             self.gestion_productos.show()
             self.close()

        def open_gestion_inventario(self):
            self.gestion_inventario = VentanaInventario()
            self.gestion_inventario.show()
            self.close()

        def open_gestion_proveedores(self):
           self.gestion_proveedores = VentanaProveedores()
           self.gestion_proveedores.show()
           self.close()   

        def open_punto_venta(self):
            self.punto_venta = VentanaPuntoVenta()
            self.punto_venta.show()
            self.close() 
     
        def open_gestion_clientes(self):
            self.gestion_clientes = VentanaClientes()
            self.gestion_clientes.show()
            self.close()  

        def open_gestion_ventas(self):
           self.gestion_ventas = GestionVenta()
           self.gestion_ventas.show()
           self.close()
            
        def open_gestion_reservas(self):
            self.gestion_reservas = VentanaReservas()
            self.gestion_reservas.show()
            self.close()

        def open_historial_ventas(self):
            self.historial_ventas = HistorialVentas()
            self.historial_ventas.show()
            self.close() 

        def open_cerrar_sesion(self):
           from Vista.login import Login
           self.cerrar_sesion = Login()
           self.cerrar_sesion.show()
           self.close()