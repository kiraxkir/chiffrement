
import sys
sys.path.append("projet_chiffrement/gui")

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_Form(object):
    #pour la fermuture de la fenetre 
    def closeEvent(self, event):
        reply = QMessageBox.question(
        self,
        'Window Close',
        'Are you sure you want to close the window?',
        QMessageBox.Yes | QMessageBox.No,
        QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    # pour ouvrir les autres fenetres 
    def open_encryption(self):
        from projet_chiffrement.gui.encryption_screen import Ui_encryption_screen
        
        self.windows=QtWidgets.QWidget()
        self.ui=Ui_encryption_screen()
        self.ui.setupUi(self.windows)
        self.windows.show()
        Form.close()
    def open_decryption(self):
        from projet_chiffrement.gui.decryption_screen import Ui_decryption_screen
        
        self.windows=QtWidgets.QWidget()
        self.ui=Ui_decryption_screen()
        self.ui.setupUi(self.windows)
        self.windows.show()
        Form.close()
    def open_instruction(self):
        from projet_chiffrement.gui.instruction_screen import instruction_screen
        self.windows=QtWidgets.QWidget()
        self.ui=instruction_screen()
        self.ui.setupUi(self.windows)
        self.windows.show()
        Form.close()

    def position( self):
        largeur = Form.width()
        hauteur = Form.height()
        print("Taille actuelle :", largeur, "x", hauteur)
        pos = Form.pos()  # Renvoie la position actuelle de la fenêtre (QPoint)
        print(pos.x(), pos.y())
    

    def setupUi(self, Form):

        Form.move(266,0)
        Form.setWindowTitle("hey")
        Form.setObjectName("Form")
        Form.setFixedSize(1411 , 1028)
        Form.resize(1411 , 981)
        Form.setStyleSheet("QWidget {\n"
"    background-color: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #daeaf6,\n"
"        stop:1 #a8c0d6\n"
"    );\n"
"    font-family: \'Segoe UI\', \'Arial\';\n"
"    font-size: 15px;\n"
"    color: #102a43;\n"
"}\n"
"\n"
"\n"
"/* Titre principal */\n"
"QLabel#mainTitle {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #1a252f;\n"
"    border:noone;\n"
"}\n"
"\n"
"/* Sous-titres ou descriptions */\n"
"QLabel#subTitle {\n"
"    font-size: 16px;\n"
"    color: #566573;\n"
"}\n"
"\n"
"/* Boutons d’action (chiffrer, déchiffrer, instructions) */\n"
"QPushButton {\n"
"    background-color: #00bcd4;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1c658c;\n"
"}\n"
"\n"
"/* Encadré si nécessaire (ex: instruction dans une frame) */\n"
"QGroupBox {\n"
"    border: 1px solid #aab7b8;\n"
"    border-radius: 6px;\n"
"    margin-top: 10px;\n"
"}\n"
"QGroupBox::title {\n"
"\n"
"    left: 10px;\n"
"    padding: 0 5px;\n"
"    color: #2e4053;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.mainTitle = QtWidgets.QLabel(Form)
        self.mainTitle.setGeometry(QtCore.QRect(410, 70, 541, 61))
        self.mainTitle.setObjectName("mainTitle")
        self.subTitle = QtWidgets.QLabel(Form)
        self.subTitle.setGeometry(QtCore.QRect(460, 170, 471, 31))
        self.subTitle.setObjectName("subTitle")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(410, 250, 561, 651))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_encryption = QtWidgets.QPushButton(self.frame )
        self.btn_encryption.clicked.connect(self.open_encryption)
        self.btn_encryption.setGeometry(QtCore.QRect(30, 160, 511, 71))
        self.btn_encryption.setObjectName("btn_encryption")
        self.btn_decryption = QtWidgets.QPushButton(self.frame)
        self.btn_decryption.clicked.connect(self.open_decryption)
        self.btn_decryption.setGeometry(QtCore.QRect(30, 320, 511, 71))
        self.btn_decryption.setObjectName("btn_decryption")
        self.btn_instruction = QtWidgets.QPushButton(self.frame)
        self.btn_instruction.clicked.connect(self.open_instruction)
        self.btn_instruction.setGeometry(QtCore.QRect(30, 480, 501, 71))
        self.btn_instruction.setStyleSheet("QPushButton {\n"
"    background-color: #f1c40f;\n"
"    color: #102a43;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 10px 20px;\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #fdff74;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #ffc662;\n"
"}")
        self.btn_instruction.setObjectName("btn_instruction")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(210, 70, 171, 31))
        self.label.setObjectName("label")
        self.btn_apropos = QtWidgets.QPushButton(Form)
        self.btn_apropos.clicked.connect(self.position)
        self.btn_apropos.setGeometry(QtCore.QRect(1130, 870, 151, 41))
        self.btn_apropos.setObjectName("btn_apropos")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.mainTitle.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:28pt;\">  CHIFFREMENT HYBRIDE </span></p></body></html>"))
        self.subTitle.setText(_translate("Form", "Protégez vos messages grâce à une combinaison de 2 chiffrement"))
        self.btn_encryption.setText(_translate("Form", " 🔐  Chiffrer un message"))
        self.btn_decryption.setText(_translate("Form", "🔓 Déchiffrer un message"))
        self.btn_instruction.setText(_translate("Form", "📘 Instructions"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Tableau de bord</span></p></body></html>"))
        self.btn_apropos.setText(_translate("Form", " À propos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
