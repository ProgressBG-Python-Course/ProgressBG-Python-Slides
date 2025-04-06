import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

from db import DB

class LoginForm(qtw.QWidget):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)

        # init DB
        self.db = DB('users.db')

        self.setupUI()

        # connect signals
        self.btnLogin.clicked.connect(self.onLoginClick)
        self.btnCancel.clicked.connect(self.close)

        # set some properties of LoginForm widget(self)
        self.setWindowTitle('Login Form')
        # self.setGeometry(0, 0, 1024, 680)
        # self.show();


    def setupUI(self):
        # create form widgets:
        self.leUserName = qtw.QLineEdit(self)
        self.lePassword = qtw.QLineEdit(self)
        self.lePassword.setEchoMode(qtw.QLineEdit.EchoMode.Password)

        self.btnLogin = qtw.QPushButton('Login')
        self.btnCancel = qtw.QPushButton('Cancel')

        # create buttons layout:
        btnLayout = qtw.QHBoxLayout()
        btnLayout.addWidget(self.btnLogin,1)
        btnLayout.insertStretch(1,1)
        btnLayout.addWidget(self.btnCancel, 1)

        # create main Form layout
        mainLayout = qtw.QFormLayout()
        mainLayout.addRow('User Name', self.leUserName)
        mainLayout.addRow('Password', self.lePassword)
        mainLayout.addRow('', btnLayout)

        # attach mainLayout to our LoginForm widget (self)
        self.setLayout(mainLayout)

    def onLoginClick(self):
        userName = self.leUserName.text()
        password = self.lePassword.text()

        authenticated = self.db.authenticate(userName, password)

        if authenticated:
            qtw.QMessageBox.information(self,'Login Successful','Login Successful')
        else:
            qtw.QMessageBox.critical(self,'Login failed','Login failed')

    def closeEvent(self, event):
        # Show a confirmation dialog
        reply = qtw.QMessageBox.question(
            self,
            "Exit Confirmation",
            "Are you sure you want to exit?",
            qtw.QMessageBox.StandardButton.Yes | qtw.QMessageBox.StandardButton.No
        )

        if reply == qtw.QMessageBox.StandardButton.Yes:
            event.accept()  # Close the window
        else:
            event.ignore()  # Prevent closing the window


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);

    loginForm = LoginForm()
    loginForm.show()

    sys.exit(app.exec())