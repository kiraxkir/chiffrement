
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # ça permet d acceder au fichier parent a celui ci genre os.path.dirname(__file__), '..')) donne le chemin absolu avec ... a la fin et os.path.abspath resous ce chemin


from PyQt5.QtWidgets import QDialog,QFileDialog, QMessageBox

from PyQt5 import QtCore, QtGui, QtWidgets
import decryptage


class Ui_decryption_screen(object):
    def open_key(self):
        filename=QFileDialog.getOpenFileName(None,'open file', 'C:/Users/HP/Desktop/encryption_resultat' ,'txt file(*.txt)')
        self.lineEdit_key_encrypted_3.setText(filename[0])
        return filename[0]
    
        
    def open_private_key(self):
        filename=QFileDialog.getOpenFileName(None,'open file', 'C:/Users/HP/Desktop/encryption_resultat' ,'txt file(*.txt)', 'bin file(* .bin)')
        self.lineEdit_private_key_2.setText(filename[0])
        print(filename)

    def open_texte(self):
        filename= QFileDialog.getOpenFileName(
            None,
        'Open File',
        'C:/Users/HP/Desktop/encryption_resultat', 'Binary Files (*.bin)*'
            )
        self.lineEdit_file.setText(filename[0])
        print(filename)


    def decrypte(self) :

        name= self.name_line.text()
        fichier = self.lineEdit_file.text()
        private_key=self.lineEdit_private_key_2.text()
        key=self.lineEdit_key_encrypted_3.text()
        
        if name =='' :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("name is require")
            msg.setText(" entrer un nom dans le champ name !!!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        if fichier =='' :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("fichier requis")
            msg.setText(" entrer le chemin du fichier a dechiffrer")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        
        if private_key =='' :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("clé requis")
            msg.setText(" entrer le chemin de la clé privé ")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        if key =='' :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("clé requis")
            msg.setText(" entrer le chemin de la clé chiffré")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return

        try:
            decryptage.decryptage(fichier,key,private_key)
            
            # Message de succès
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Succès")
            msg.setText("Le message a été dechiffré avec succès.")
            msg.setDetailedText('le resultat est sauvegardé sur le bureau dans un dossier appelé dechiffrement_reussi')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        except Exception as error:
            # Affichage d'une erreur si le dechiffrement échoue
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erreur lors du chiffrement")
            msg.setText(f"Une erreur est survenue :\n{"les clé ne sont pas valide"}")
            msg.setDetailedText(str(error))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()  
    # def position( self):
    #     largeur = decryption_screen.width()
    #     hauteur = decryption_screen.height()

    #     print("Taille actuelle :", largeur, "x", hauteur)    

    #     pos = decryption_screen.pos()  # Renvoie la position actuelle de la fenêtre (QPoint)
    #     print(pos.x(), pos.y())  

    def setupUi(self, decryption_screen):
        decryption_screen.setObjectName("decryption_screen")
        decryption_screen.move(333 , 4)
        decryption_screen.setFixedSize( 1351 ,1055)

        decryption_screen.resize(1373, 1079)
        decryption_screen.setStyleSheet("/* === Fond général === */\n"
"QWidget {\n"
"    background-color: #dceeff;\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;\n"
"    font-size: 17px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
"/* === Titre principal === */\n"
"QLabel#mainTitle {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #0d3c61;\n"
"}\n"
"\n"
"/* === Sous-titres (File Path, Key Used, etc.) === */\n"
"QLabel {\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    color: #1c4966;\n"
"}\n"
"\n"
"/* === QLineEdit (champ de texte) === */\n"
"QLineEdit {\n"
"    background-color: white;\n"
"    border: 1px solid #3498db;\n"
"    border-radius: 5px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"/* === QPushButton (tous les boutons) === */\n"
"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 8px 16px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2e86c1;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2471a3;\n"
"}\n"
"\n"
"/* === Spécifique au bouton \"EXÉCUTER\" === */\n"
"QPushButton#btnExecuter {\n"
"    font-size: 16px;\n"
"    background-color: #1abc9c;\n"
"}\n"
"\n"
"QPushButton#btnExecuter:hover {\n"
"    background-color: #17a589;\n"
"}\n"
"\n"
"QPushButton#btnExecuter:pressed {\n"
"    background-color: #148f77;\n"
"}\n"
"\n"
"/* === Spécifique au bouton \"Retour\" === */\n"
"QPushButton#btnRetour {\n"
"    background-color: #763325;\n"
"}\n"
"\n"
"QPushButton#btnRetour:hover {\n"
"    background-color: #d35400;\n"
"}\n"
"\n"
"QPushButton#btnRetour:pressed {\n"
"    background-color: #ba4a00;\n"
"}\n"
"")
        self.frame = QtWidgets.QFrame(decryption_screen)
        self.frame.setGeometry(QtCore.QRect(200, 10, 1351, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.mainTitle = QtWidgets.QLabel(self.frame)
        self.mainTitle.setGeometry(QtCore.QRect(320, 10, 401, 51))
        self.mainTitle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mainTitle.setObjectName("mainTitle")
        self.label_2 = QtWidgets.QLabel(decryption_screen)
        self.label_2.setGeometry(QtCore.QRect(600, 100, 191, 41))
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(decryption_screen)
        self.frame_2.setGeometry(QtCore.QRect(350, 160, 771, 781))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 121, 31))
        self.label_3.setObjectName("label_3")
        self.name_line = QtWidgets.QLineEdit(self.frame_2)
        self.name_line.setGeometry(QtCore.QRect(190, 100, 361, 31))
        self.name_line.setStyleSheet("background-color: rgb(235, 242, 255);")
        self.name_line.setInputMask("")
        self.name_line.setText("")
        self.name_line.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.name_line.setObjectName("name_line")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(350, 220, 111, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(50, 310, 121, 31))
        self.label_6.setObjectName("label_6")
        self.lineEdit_file = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_file.setGeometry(QtCore.QRect(200, 310, 361, 31))
        self.lineEdit_file.setStyleSheet("background-color: rgb(235, 242, 255);")
        self.lineEdit_file.setObjectName("lineEdit_file")
        self.btn_browser_file = QtWidgets.QPushButton(self.frame_2)
        self.btn_browser_file.clicked.connect(self.open_texte)
        self.btn_browser_file.setGeometry(QtCore.QRect(600, 310, 141, 41))
        self.btn_browser_file.setStyleSheet("")
        self.btn_browser_file.setAutoDefault(False)
        self.btn_browser_file.setDefault(False)
        self.btn_browser_file.setFlat(False)
        self.btn_browser_file.setObjectName("btn_browser_file")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(30, 430, 161, 31))
        self.label_7.setObjectName("label_7")
        self.lineEdit_private_key_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_private_key_2.setGeometry(QtCore.QRect(200, 430, 351, 31))
        self.lineEdit_private_key_2.setStyleSheet("background-color: rgb(235, 242, 255);")
        self.lineEdit_private_key_2.setObjectName("lineEdit_private_key_2")
        self.btn_browser_private = QtWidgets.QPushButton(self.frame_2)
        self.btn_browser_private.clicked.connect(self.open_private_key)
        self.btn_browser_private.setGeometry(QtCore.QRect(600, 430, 141, 41))
        self.btn_browser_private.setStyleSheet("")
        self.btn_browser_private.setAutoDefault(False)
        self.btn_browser_private.setDefault(False)
        self.btn_browser_private.setFlat(False)
        self.btn_browser_private.setObjectName("btn_browser_private")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(10, 540, 181, 31))
        self.label_8.setObjectName("label_8")
        self.lineEdit_key_encrypted_3 = QtWidgets.QLineEdit(self.frame_2)
        
        self.lineEdit_key_encrypted_3.setGeometry(QtCore.QRect(210, 540, 351, 31))
        self.lineEdit_key_encrypted_3.setStyleSheet("background-color: rgb(235, 242, 255);")
        self.lineEdit_key_encrypted_3.setObjectName("lineEdit_key_encrypted_3")
        self.btn_browser_key = QtWidgets.QPushButton(self.frame_2)
        self.btn_browser_key.clicked.connect(self.open_key)
        self.btn_browser_key.setGeometry(QtCore.QRect(600, 530, 141, 41))
        self.btn_browser_key.setStyleSheet("")
        self.btn_browser_key.setAutoDefault(False)
        self.btn_browser_key.setDefault(False)
        self.btn_browser_key.setFlat(False)
        self.btn_browser_key.setObjectName("btn_browser_key")
        self.btnExecuter = QtWidgets.QPushButton(self.frame_2)
        self.btnExecuter.clicked.connect(self.decrypte)
    #    self.btnExecuter.clicked.connect(self.position)
        self.btnExecuter.setGeometry(QtCore.QRect(310, 660, 181, 41))
        self.btnExecuter.setStyleSheet("")
        self.btnExecuter.setObjectName("btnExecuter")
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setGeometry(QtCore.QRect(330, 250, 118, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.btnRetour = QtWidgets.QPushButton(decryption_screen)
        self.btnRetour.hide()
        self.btnRetour.setGeometry(QtCore.QRect(70, 40, 181, 41))
        self.btnRetour.setStyleSheet("")
        self.btnRetour.setObjectName("btnRetour")

        self.retranslateUi(decryption_screen)
        QtCore.QMetaObject.connectSlotsByName(decryption_screen)

    def retranslateUi(self, decryption_screen):
        _translate = QtCore.QCoreApplication.translate
        decryption_screen.setWindowTitle(_translate("decryption_screen", "Form"))
        self.mainTitle.setText(_translate("decryption_screen", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">CHIFFREMENT HYBRIDE </span></p></body></html>"))
        self.label_2.setText(_translate("decryption_screen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">FILE DECRYTION</span></p><p><br/></p></body></html>"))
        self.label_3.setText(_translate("decryption_screen", "<html><head/><body><p><span style=\" font-size:12pt;\">username :</span></p></body></html>"))
        self.name_line.setPlaceholderText(_translate("decryption_screen", "votre nom ..."))
        self.label_5.setText(_translate("decryption_screen", "<html><head/><body><p><span style=\" font-size:11pt;\">FILE PATH</span></p><p><br/></p></body></html>"))
        self.label_6.setText(_translate("decryption_screen", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">FILE PATH :</span></p></body></html>"))
        self.lineEdit_file.setPlaceholderText(_translate("decryption_screen", " Le message chiffré "))
        self.btn_browser_file.setWhatsThis(_translate("decryption_screen", "<html><head/><body><p><span style=\" font-size:12pt;\">chiffrer</span></p></body></html>"))
        self.btn_browser_file.setText(_translate("decryption_screen", "parcourir"))
        self.label_7.setText(_translate("decryption_screen", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">private key PATH :</span></p></body></html>"))
        self.lineEdit_private_key_2.setPlaceholderText(_translate("decryption_screen", " La clé privée "))
        self.btn_browser_private.setWhatsThis(_translate("decryption_screen", "<html><head/><body><p><span style=\" font-size:12pt;\">chiffrer</span></p></body></html>"))
        self.btn_browser_private.setText(_translate("decryption_screen", "parcourir"))
        self.label_8.setText(_translate("decryption_screen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">encrypted key PATH :</span></p></body></html>"))
        self.lineEdit_key_encrypted_3.setPlaceholderText(_translate("decryption_screen", " La clé chiffrée "))
        self.btn_browser_key.setWhatsThis(_translate("decryption_screen", "<html><head/><body><p><span style=\" font-size:12pt;\">chiffrer</span></p></body></html>"))
        self.btn_browser_key.setText(_translate("decryption_screen", "parcourir"))
        self.btnExecuter.setWhatsThis(_translate("decryption_screen", "<html><head/><body><p><span style=\" font-size:12pt;\">chiffrer</span></p></body></html>"))
        self.btnExecuter.setText(_translate("decryption_screen", "EXECUTER"))
        self.btnRetour.setWhatsThis(_translate("decryption_screen", "<html><head/><body><p><span style=\" font-size:12pt;\">chiffrer</span></p></body></html>"))
        self.btnRetour.setText(_translate("decryption_screen", "⬅ Retour"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    decryption_screen = QtWidgets.QWidget()
    ui = Ui_decryption_screen()
    ui.setupUi(decryption_screen)
    decryption_screen.show()
    sys.exit(app.exec_())
