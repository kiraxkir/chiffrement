# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # ça permet d acceder au fichier parent a celui ci genre os.path.dirname(__file__), '..')) donne le chemin absolu avec ... a la fin et os.path.abspath resous ce chemin

from PyQt5.QtWidgets import QDialog,QFileDialog, QMessageBox

from PyQt5 import QtCore, QtGui, QtWidgets


from cryptage import cryptage


class Ui_encryption_screen(object):

    def retour_main(self):
        from ui_main import Ui_Form
        self.windows=QtWidgets.QWidget()
        self.ui=Ui_Form()
        self.ui.setupUi(self.windows)
        self.windows.show()

    
    # def position( self):
    #     largeur = encryption_screen.width()
    #     hauteur = encryption_screen.height()

    #     print("Taille actuelle :", largeur, "x", hauteur)    

    #     pos = encryption_screen.pos()  # Renvoie la position actuelle de la fenêtre (QPoint)
    #     print(pos.x(), pos.y())  


    def open_file(self):
        filename=QFileDialog.getOpenFileName(None,'open file', 'C:/Users/HP/Desktop/encryption_resultat' ,'txt file(*.txt)')
        self.lineEdit_file.setText(filename[0])
    

    def chiffrement(self) :
        texte=self.lineEdit_file.text()
        name=self.name_line.text()

        if name =='' :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("name is require")
            msg.setText(" entrer un nom dans le champ name !!!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return

        if texte =='' :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("required file")
            msg.setText("entrer le chemin du message !")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        
        try:
            cryptage(texte, name)

            # Message de succès
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Succès")
            msg.setText("Le message a été chiffré avec succès.")
            msg.setDetailedText('le resultat est sauvegardé sur le bureau dans un dossier appelé chiffrement_reussi')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        except Exception as error:
            # Affichage d'une erreur si le chiffrement échoue
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erreur lors du chiffrement")
            msg.setText(f"Une erreur est survenue :\n{str(error)}")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
    def setupUi(self, encryption_screen):
        encryption_screen.setWindowTitle("Fenêtre de chiffrement")     
        encryption_screen.setObjectName("encryption_screen")
        encryption_screen.move(197,3)
        encryption_screen.setFixedSize(1538 , 1055)

      #  encryption_screen.resize(1569, 1122)

        encryption_screen.setStyleSheet("/* === Fond général === */\n"
                                        
"QWidget {\n"
"    background-color: #dceeff;\n"
"    font-family: \'Segoe UI\', Arial, sans-serif;\n"
"    font-size: 14px;\n"
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
"    background-color: #e67e22;\n"
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
        self.frame_2 = QtWidgets.QFrame(encryption_screen)
        self.frame_2.setGeometry(QtCore.QRect(470, 190, 711, 931))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(70, 160, 121, 31))
        self.label_3.setObjectName("label_3")
        self.name_line = QtWidgets.QLineEdit(self.frame_2)
        self.name_line.setGeometry(QtCore.QRect(190, 160, 301, 41))
        self.name_line.setStyleSheet("background-color: rgb(235, 242, 255);")
        self.name_line.setInputMask("")
        self.name_line.setText("")
        self.name_line.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.name_line.setObjectName("name_line")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(320, 60, 121, 31))
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(310, 90, 141, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(320, 300, 111, 31))
        self.label_5.setObjectName("label_5")
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setGeometry(QtCore.QRect(300, 320, 118, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(40, 390, 121, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(290, 670, 101, 31))
        self.label_7.setObjectName("label_7")
        self.line_3 = QtWidgets.QFrame(self.frame_2)
        self.line_3.setGeometry(QtCore.QRect(290, 700, 91, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(90, 780, 81, 31))
        self.label_8.setObjectName("label_8")
        self.line_key = QtWidgets.QLineEdit(self.frame_2)
        self.line_key.setGeometry(QtCore.QRect(190, 770, 351, 41))
        self.line_key.setStyleSheet("background-color: rgb(235, 242, 255);")
        self.line_key.setObjectName("line_key")
        self.btnExecuter = QtWidgets.QPushButton(self.frame_2)
        self.btnExecuter.clicked.connect(self.chiffrement)
        #self.btnExecuter.clicked.connect(self.position)

        self.btnExecuter.setGeometry(QtCore.QRect(260, 560, 181, 41))
        self.btnExecuter.setStyleSheet("")
        self.btnExecuter.setObjectName("btnExecuter")
        self.btn_browser = QtWidgets.QPushButton(self.frame_2)
        self.btn_browser.clicked.connect(self.open_file)

        self.btn_browser.setGeometry(QtCore.QRect(520, 390, 141, 41))
        self.btn_browser.setStyleSheet("")
        self.btn_browser.setAutoDefault(False)
        self.btn_browser.setDefault(False)
        self.btn_browser.setFlat(False)
        self.btn_browser.setObjectName("btn_browser")
        self.lineEdit_file = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_file.setGeometry(QtCore.QRect(160, 390, 331, 41))
        self.lineEdit_file.setStyleSheet("background-color: rgb(235, 242, 255);")
        self.lineEdit_file.setObjectName("lineEdit_file")
        self.label_2 = QtWidgets.QLabel(encryption_screen)
        self.label_2.setGeometry(QtCore.QRect(720, 130, 281, 41))
        self.label_2.setObjectName("label_2")
        self.btnRetour = QtWidgets.QPushButton(encryption_screen)
        self.btnRetour.hide()
        self.btnRetour.clicked.connect(self.retour_main)
        self.btnRetour.setGeometry(QtCore.QRect(30, 30, 141, 41))
        self.btnRetour.setStyleSheet("")
        self.btnRetour.setAutoDefault(False)
        self.btnRetour.setDefault(False)
        self.btnRetour.setFlat(False)
        self.btnRetour.setObjectName("btnRetour")
        self.mainTitle = QtWidgets.QLabel(encryption_screen)
        self.mainTitle.setGeometry(QtCore.QRect(690, 30, 281, 51))
        self.mainTitle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mainTitle.setObjectName("mainTitle")

        self.retranslateUi(encryption_screen)
        QtCore.QMetaObject.connectSlotsByName(encryption_screen)

    def retranslateUi(self, encryption_screen):
        _translate = QtCore.QCoreApplication.translate
        encryption_screen.setWindowTitle(_translate("encryption_screen", "chiffrement"))


        self.label_3.setText(_translate("encryption_screen", "<html><head/><body><p><span style=\" font-size:12pt;\">username :</span></p></body></html>"))
        self.name_line.setPlaceholderText(_translate("encryption_screen", "votre nom ..."))
        self.label_4.setText(_translate("encryption_screen", "<html><head/><body><p><span style=\" font-size:10pt;\">identification</span></p></body></html>"))
        self.label_5.setText(_translate("encryption_screen", "<html><head/><body><p><span style=\" font-size:11pt;\">FILE PATH</span></p><p><br/></p></body></html>"))
        self.label_6.setText(_translate("encryption_screen", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">FILE PATH :</span></p></body></html>"))
        self.label_7.setText(_translate("encryption_screen", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">KEY USED</span></p></body></html>"))
        self.label_8.setText(_translate("encryption_screen", "<html><head/><body><p><span style=\" font-size:10pt;\">Cle utilisé :</span></p></body></html>"))
        self.btnExecuter.setWhatsThis(_translate("encryption_screen", "<html><head/><body><p><span style=\" font-size:12pt;\">chiffrer</span></p></body></html>"))
        self.btnExecuter.setText(_translate("encryption_screen", "EXECUTER"))
        self.btn_browser.setWhatsThis(_translate("encryption_screen", "<html><head/><body><p><span style=\" font-size:12pt;\">chiffrer</span></p></body></html>"))
        self.btn_browser.setText(_translate("encryption_screen", "parcourir"))
        self.label_2.setText(_translate("encryption_screen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">FILE ENCRYPTION</span></p></body></html>"))
        self.btnRetour.setWhatsThis(_translate("encryption_screen", "<html><head/><body><p><span style=\" font-size:12pt;\">chiffrer</span></p></body></html>"))
        self.btnRetour.setText(_translate("encryption_screen", "⬅ Retour"))
        self.mainTitle.setText(_translate("encryption_screen", "<html><head/><body><p><span style=\" font-size:22pt; text-decoration: underline;\">CHIFFREMENT</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    encryption_screen = QtWidgets.QWidget()
   

    ui = Ui_encryption_screen()
    ui.setupUi(encryption_screen)
    encryption_screen.show()
    sys.exit(app.exec_())
