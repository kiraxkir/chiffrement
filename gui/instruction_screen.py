
from PyQt5 import QtCore, QtGui, QtWidgets


class instruction_screen(object):
    
    def retour_main(self):
        from ui_main import Ui_Form
        self.windows=QtWidgets.QWidget()
        self.ui=Ui_Form()
        self.ui.setupUi(self.windows)
        self.windows.show()
        # Form.hide()

        

    

    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(2082, 1102)
        Form.setStyleSheet("/* Fond général */\n"
"QWidget {\n"
"    background-color: #102a43;\n"
"    color: #f0f4f8;\n"
"    font-family: \"Segoe UI\", \"Arial\", sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* TextBrowser (les deux champs de texte) */\n"
"QTextBrowser {\n"
"    background-color: #243b53;\n"
"    color: #f0f4f8;\n"
"    border: 2px solid #486581;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"/* Bouton Accueil */\n"
"QPushButton {\n"
"    background-color: #102a43;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5fa8d3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2c699a;\n"
"}\n"
"")
        self.btn_retour = QtWidgets.QPushButton(Form)
        self.btn_retour.clicked.connect(self.retour_main)
        self.btn_retour.hide()
        self.btn_retour.setGeometry(QtCore.QRect(80, 50, 151, 41))
        self.btn_retour.setObjectName("btn_retour")
        self.titreInstruction = QtWidgets.QLabel(Form)
        self.titreInstruction.setGeometry(QtCore.QRect(860, 80, 221, 61))
        self.titreInstruction.setStyleSheet("QLabel#titreInstruction {\n"
"    color: #f0f4f8;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    letter-spacing: 2px;\n"
"    border-bottom: 2px solid #3e7cb1;\n"
"    padding-bottom: 5px;\n"
"    margin-bottom: 10px;\n"
"}")
        self.titreInstruction.setObjectName("titreInstruction")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(160, 200, 721, 771))
        self.groupBox.setObjectName("groupBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(40, 30, 641, 721))
        self.textBrowser.setToolTipDuration(0)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(1040, 190, 751, 771))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 30, 691, 721))
        self.textBrowser_2.setToolTipDuration(0)
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_2.setLineWidth(0)
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_retour.setText(_translate("Form", "⬅ Retour"))
        self.titreInstruction.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">INSTRUCTIONS</span></p></body></html>"))
        self.groupBox.setTitle(_translate("Form", "INSTRUCTION POUR LE CHIFFFRMENT"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI,Arial,sans-serif\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:600;\">📄 Tutoriel d\'utilisation de l\'application de chiffrement</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Écrivez votre message</span><span style=\" font-size:14px;\"><br />Créez un fichier texte (</span><span style=\" font-family:\'Courier New\'; font-size:14px;\">.txt</span><span style=\" font-size:14px;\">) contenant le message que vous souhaitez chiffrer. (File path)</span></li>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<li style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">L es clés sont générées automatiquement</span><span style=\" font-size:14px;\"><br />Lors du chiffrement, une </span><span style=\" font-size:14px; font-weight:600;\">clé</span><span style=\" font-size:14px;\"> est créée automatiquement. Elle est composée de deux parties :</span></li>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">🔐 Une </span><span style=\" font-size:14px; font-weight:600;\">clé chiffrée</span></li>\n"
"<li style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">🔑 Une </span><span style=\" font-size:14px; font-weight:600;\">clé privée</span></li></ul>\n"
"<li style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Résultat du chiffrement</span><span style=\" font-size:14px;\"><br />Le message chiffré est enregistré dans un fichier </span><span style=\" font-family:\'Courier New\'; font-size:14px;\">.txt</span><span style=\" font-size:14px;\"> sur votre </span><span style=\" font-size:14px; font-weight:600;\">Bureau</span><span style=\" font-size:14px;\">, dans un dossier nommé </span><span style=\" font-family:\'Courier New\'; font-size:14px; font-weight:600;\">encryption_result</span><span style=\" font-size:14px;\">, avec votre </span><span style=\" font-size:14px; font-weight:600;\">nom d\'utilisateur</span><span style=\" font-size:14px;\"> comme nom de fichier.</span></li>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"><br /></p>\n"
"<li style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Sécurité des clés</span><span style=\" font-size:14px;\"><br />Les clés sont </span><span style=\" font-size:14px; font-weight:600;\">personnelles et confidentielles</span><span style=\" font-size:14px;\">.<br />➤ </span><span style=\" font-size:14px; font-weight:600;\">Conservez-les précieusement</span><span style=\" font-size:14px;\"> : elles sont nécessaires uniquement pour </span><span style=\" font-size:14px; font-weight:600;\">déchiffrer</span><span style=\" font-size:14px;\"> votre message.</span></li></ol></body></html>"))
        self.groupBox_2.setTitle(_translate("Form", "INSTRUCTION POUR LE DECHIFFREMENT "))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI,Arial,sans-serif\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">🔓 Tutoriel pour déchiffrer un message</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Lorsque vous avez chiffré votre message, trois fichiers ont été générés automatiquement :</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">📄 Le </span><span style=\" font-size:14px; font-weight:600;\">message chiffré</span></li>\n"
"<li style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">🔐 La </span><span style=\" font-size:14px; font-weight:600;\">clé chiffrée</span></li>\n"
"<li style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">🔑 La </span><span style=\" font-size:14px; font-weight:600;\">clé publique</span></li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Pour pouvoir déchiffrer Le message, vous avez besoin des ces deux</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\"> </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">fichiers (chiffrée et privée) ainsi que du </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">message chiffré</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">.</span></p>\n"
"<hr />\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">✅ Étapes à suivre pour le déchiffrement :</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px; font-weight:600;\">Renseignez les champs requis :</span></li>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">La </span><span style=\" font-size:14px; font-weight:600;\">clé chiffrée </span></li>\n"
"<li style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">La </span><span style=\" font-size:14px; font-weight:600;\">clé privée </span></li>\n"
"<li style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">Le </span><span style=\" font-size:14px; font-weight:600;\">message chiffré</span></li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">⚠️ </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">Attention :</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\"> Utilisez uniquement les clés d\'origine. Si vous utilisez une mauvaise clé, le message ne pourra pas être déchiffré correctement.</span></p>\n"
"<li style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px; font-weight:600;\">Entrez votre nom d\'utilisateur.</span></li>\n"
"<li style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">Le résultat du déchiffrement sera automatiquement enregistré sur votre </span><span style=\" font-size:14px; font-weight:600;\">Bureau</span><span style=\" font-size:14px;\">, dans un fichier nommé </span><span style=\" font-family:\'Courier New\'; font-size:14px; font-weight:600;\">decryption_resultat + username.txt</span><span style=\" font-size:14px;\">.</span></li></ol></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = instruction_screen()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
