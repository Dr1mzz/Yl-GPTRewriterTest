from PyQt5 import QtCore, QtWidgets


class Ui_RequestWidget(object):
    def setupUi(self, RequestWidget):
        RequestWidget.setObjectName("RequestWidget")
        RequestWidget.resize(501, 301)
        RequestWidget.setFixedSize(501, 301)
        self.verticalLayoutWidget = QtWidgets.QWidget(RequestWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 501, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableWidget)
        self.textBrowser_2 = QtWidgets.QTextBrowser(RequestWidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 0, 521, 31))
        self.textBrowser_2.setStyleSheet("background-color: rgb(125, 200, 200);\n" "")
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(RequestWidget)
        QtCore.QMetaObject.connectSlotsByName(RequestWidget)

    def retranslateUi(self, RequestWidget):
        _translate = QtCore.QCoreApplication.translate
        RequestWidget.setWindowTitle(_translate("RequestWidget", "RequestWidget"))
        self.textBrowser_2.setHtml(
            _translate(
                "RequestWidget",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt; font-weight:600; color:#ffffff;">Запросы:</span></p></body></html>',
            )
        )
