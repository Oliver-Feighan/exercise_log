from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import gui.window_parameters as param

class TableButton(QPushButton):
    def __init__(self, param):
        super().__init__()
        self.setText("%s" % param.get("text"))
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.toggle()

class MasterWindow(QMainWindow):
    app = QApplication([])

    def table_buttons(self):
        self.layout.addWidget(QLabel("Input tables:"), alignment=(Qt.AlignLeft | Qt.AlignCenter))

        self.run_button = TableButton({"text" : "run"})
        self.calisthenics_button = TableButton({"text": "calisthenics"})

        self.layout.addWidget(self.run_button, alignment=(Qt.AlignLeft | Qt.AlignJustify))
        self.layout.addWidget(self.calisthenics_button, alignment=(Qt.AlignLeft | Qt.AlignJustify))

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercise Log")
        self.layout = QVBoxLayout()

        self.table_buttons()

        self.win = QWidget()

        self.win.setLayout(self.layout)
        self.win.setGeometry(param.master_window["x"],
                             param.master_window["y"],
                             param.master_window["width"],
                             param.master_window["height"])
        self.win.show()
        self.app.exec_()
