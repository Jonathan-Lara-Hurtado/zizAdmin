import sys
from PyQt5.QtWidgets import QApplication
from Librerias.Clases.VentanaPrincipal import VentanaPrincipal





if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    aplicacion.setApplicationName("ziz admin")
    aplicacion.setApplicationVersion("1.0.0")
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(aplicacion.exec_())