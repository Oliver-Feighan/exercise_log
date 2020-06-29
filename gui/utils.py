from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

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