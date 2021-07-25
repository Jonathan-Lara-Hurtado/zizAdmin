# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ventanaPrincipalBoceto.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaPrincipalBoceto(object):
    def setupUi(self, VentanaPrincipalBoceto):
        VentanaPrincipalBoceto.setObjectName("VentanaPrincipalBoceto")
        VentanaPrincipalBoceto.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Recursos/Imagenes/zizIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VentanaPrincipalBoceto.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(VentanaPrincipalBoceto)
        self.centralwidget.setObjectName("centralwidget")
        VentanaPrincipalBoceto.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(VentanaPrincipalBoceto)
        self.statusbar.setObjectName("statusbar")
        VentanaPrincipalBoceto.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaPrincipalBoceto)
        QtCore.QMetaObject.connectSlotsByName(VentanaPrincipalBoceto)

    def retranslateUi(self, VentanaPrincipalBoceto):
        _translate = QtCore.QCoreApplication.translate
        VentanaPrincipalBoceto.setWindowTitle(_translate("VentanaPrincipalBoceto", "ziz administrador"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaPrincipalBoceto = QtWidgets.QMainWindow()
    ui = Ui_VentanaPrincipalBoceto()
    ui.setupUi(VentanaPrincipalBoceto)
    VentanaPrincipalBoceto.show()
    sys.exit(app.exec_())
