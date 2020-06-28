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


class TableWindow(QWindow):
    def __init__(self, param):
        super().__init__()
        self.tablelayout = QGridLayout()
        self.tablewin = QWidget()
        self.header = QLabel()
        self.header.setText(param.get("table"))
        self.tablewin.setFixedSize(300, 300)
        self.tablelayout.addWidget(self.header, 0, 0)

    def clicked(self):
        self.tablewin.show()

class RunWindow(TableWindow):
    def __init__(self, param_dict):
        super().__init__(param_dict)
        for count, run_input in enumerate(param.run_inputs):
            label_i = QLabel()
            label_i.setText(run_input)
            self.tablelayout.addWidget(label_i, count + 1, 0)

            input_i = QTextEdit()
            self.tablelayout.addWidget(input_i, count + 1 ,1)



        self.tablewin.setLayout(self.tablelayout)


class MasterWindow(QMainWindow):
    app = QApplication([])
    app.setWindowIcon(QIcon('/Users/of15641/Documents/OwnProjects/exercise_log/run_image.png'))
    app.setApplicationName("Exercise log")
    app.setApplicationDisplayName("Exercise log")


    def picture(self):
        picture_label = QLabel()
        pixmap = QPixmap('/Users/of15641/Documents/OwnProjects/exercise_log/run_image.png')
        pixmap_resized = pixmap.scaled(100, 100, Qt.KeepAspectRatio)
        picture_label.setPixmap(pixmap_resized)

        self.layout.addWidget(picture_label)

    def table_buttons(self, row : int, column : int):
        self.layout.addWidget(QLabel("Input tables:"), row, column)

        self.run_button = TableButton({"text" : "runs"})
        self.run_window = RunWindow({"table" : "runs"})

        self.run_button.clicked.connect(self.run_window.clicked)
        self.calisthenics_button = TableButton({"text": "calisthenics"})

        self.layout.addWidget(self.run_button, row+1, column)
        self.layout.addWidget(self.calisthenics_button, row+2, column)

    def weekly_data_setup(self):
        self.weekly_data = QLabel()
        weekly_text = "this will be the weekly data \n"
        for day in param.days:
            weekly_text += "%s: \n \n" % day
        self.weekly_data.setText(weekly_text)
        self.weekly_data.setMinimumSize(70, 45)
        self.weekly_data.setStyleSheet("background-color: white")
        self.layout.addWidget(self.weekly_data, 1, 2, 8, 1)

    def __init__(self):
        super().__init__()
        self.win = QWidget()
        self.win.setWindowTitle("Exercise Log")
        self.layout = QGridLayout()
        self.win.setLayout(self.layout)

        self.text = QLabel()
        self.text.setText("Exercise log")
        self.text.setStyleSheet("font: 20pt")

        self.layout.addWidget(self.text, 0, 0)

        self.table_buttons(1, 0)

        self.weekly_data_setup()


        """
        self.toolbar = QToolBar()
        self.toolbar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layout.addWidget(self.toolbar, 1, 0)
        self.toolbar.addAction("add")
        self.toolbar.addAction("read")
        """
        self.win.setFixedSize(param.master_window["width"], param.master_window["height"])

        self.win.show()
        self.app.exec_()
