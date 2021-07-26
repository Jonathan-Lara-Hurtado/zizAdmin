from PyQt5.QtWidgets import QMainWindow
from Librerias.Vistas.ventanaPrincipalBoceto import Ui_VentanaPrincipalBoceto


from PyQt5.QtWidgets import QSystemTrayIcon,QMenu
from PyQt5.QtGui import QIcon
from Librerias.Herramientas.herramientaPyinstaller import recurso_path


class VentanaPrincipal(QMainWindow,Ui_VentanaPrincipalBoceto):

    salida = False

    def __init__(self,*args,**kwargs):
        QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)

        self.btnZizWeb.clicked.connect(self.eventoZizWeb)
        self.tray = QSystemTrayIcon(self)
        if self.tray.isSystemTrayAvailable():
            self.tray.setIcon(QIcon(recurso_path("Recursos/Imagenes/zizIconV2.png")))
            
            #contexto Menu
            ctmenu = QMenu()
            accionVer = ctmenu.addAction("Ver/Ocultar")
            accionVer.triggered.connect(lambda:self.hide() if self.isVisible() else self.show())
            accionSalida = ctmenu.addAction("Salir")
            accionSalida.triggered.connect(self.eventoActivarSalida)

            self.tray.setContextMenu(ctmenu)
            self.tray.show()
        else:
            self.tray = None


    def eventoActivarSalida(self):
        self.salida = True
        self.close()
        
    def closeEvent(self,event):
        if self.salida:
            event.accept()
        else:
            self.hide()
            event.ignore()
    
    def eventoZizWeb(self):
        print("click")