from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MessageWindow(QWindow):
    def __init__(self, text):
        super().__init__()
        self.layout = QGridLayout()
        self.widget = QWidget()
        self.message = QLabel()
        self.message.setText("text")
        self.widget.setMinimumSize(20, 50)
        self.layout.addWidget(self.message, 0, 0)


class TableWindow(QWindow):
    def __init__(self, param):
        super().__init__()
        self.tablelayout = QGridLayout()
        self.tablewin = QWidget()
        self.header = QLabel()
        self.header.setText(param.get("table"))
        self.header.setStyleSheet("font: 20pt")
        self.tablewin.setMinimumSize(400, 150)
        self.tablelayout.addWidget(self.header, 0, 0)

    def clicked(self):
        self.tablewin.show()