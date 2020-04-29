import sys, os
import requests
from PyQt5 import QtCore, QtWidgets, QtGui, sip


def login():
    if os.path.isfile('AutoLoginInfo.dat'):
        myFile = open('AutoLoginInfo.dat', 'r')
        usernameList = myFile.readline().split('\n')
        passwordList = myFile.readline().split('\n')
        if usernameList[0] != None:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
            }
            data = {
                'username': usernameList[0],
                'userpwd': passwordList[0],
            }
            url = 'http://192.168.242.254/cgi-bin/ace_web_auth.cgi?web_jumpto=&orig_referer='
            session = requests.Session()
            session.post(url, headers=headers, data=data)

        myFile.close()        


class setUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(400, 200)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        # self.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)

        textFont = QtGui.QFont('consolas', 14, QtGui.QFont.Bold)
        labelFont = QtGui.QFont('consolas', 10)
        self.text = QtWidgets.QLabel("NUK NETWORK LOGIN")
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setFont(textFont)

        self.label1 = QtWidgets.QLabel("USERNAME")
        self.label1.setFont(labelFont)

        self.label2 = QtWidgets.QLabel("PASSWORD")
        self.label2.setFont(labelFont)

        self.user = QtWidgets.QLineEdit(self)
        self.user.setFont(labelFont)

        self.pwd = QtWidgets.QLineEdit(self)
        self.pwd.setFont(labelFont)

        self.button = QtWidgets.QPushButton("SAVE")
        self.button.setFont(labelFont)

        if os.path.isfile('AutoLoginInfo.dat'):
            myFile = open('AutoLoginInfo.dat', 'r')
            usernameList = myFile.readline().split('\n')
            passwordList = myFile.readline().split('\n')

            if(usernameList[0] != None):
                self.user.setText(usernameList[0])

            if(passwordList[0] != None):
                self.pwd.setText(passwordList[0])

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.user)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.pwd)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.save_data)     


    def save_data(self):
        username = self.user.text()
        password = self.pwd.text()
        if username == '' or password == '':
            QtWidgets.QMessageBox.information(self, 'Info', 'Empty fields! Please, try again.')
        else:
            myFile = open("AutoLoginInfo.dat", "w")
            myFile.write(username+'\n')
            myFile.write(password)
            myFile.close()
            QtWidgets.QMessageBox.information(self, 'Info', 'Data has been saved!')

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
           if self.windowState() & QtCore.Qt.WindowMinimized:
                window.hide()
        QtWidgets.QWidget.changeEvent(self, event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = setUI()
    window.setWindowTitle("NUK AutoNet")

    trayIcon = QtWidgets.QSystemTrayIcon(QtGui.QIcon('icon.png'))
    trayIcon.setToolTip('NUK AutoNet')
    trayIcon.show()

    menu = QtWidgets.QMenu()
    openAction = menu.addAction('Open')
    exitAction = menu.addAction('Exit')
    openAction.triggered.connect(window.show)
    exitAction.triggered.connect(app.quit)

    trayIcon.setContextMenu(menu)
    QtWidgets.QApplication.setQuitOnLastWindowClosed(False)
    login()
    sys.exit(app.exec_())