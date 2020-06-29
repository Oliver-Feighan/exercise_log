from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import gui.window_parameters as param
import os

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
        self.header.setStyleSheet("font: 20pt")
        self.tablewin.setMinimumSize(400, 150)
        self.tablelayout.addWidget(self.header, 0, 0)

    def clicked(self):
        self.tablewin.show()

class RunWindow(TableWindow):
    def __init__(self, param_dict):
        super().__init__(param_dict)
        #LOGDATE
        logdate_widget = QWidget()
        logdate_sublayout = QHBoxLayout()

        day = QComboBox()
        month = QComboBox()
        year = QComboBox()
        day.addItems([str(day) for day in range(1, 32)])
        month.addItems([str(month) for month in range(1, 13)])
        year.addItems([str(year) for year  in range(2020, 2051)])

        logdate_sublayout.addWidget(day, alignment=Qt.AlignCenter)
        logdate_sublayout.addWidget(month, alignment=Qt.AlignCenter)
        logdate_sublayout.addWidget(year, alignment=Qt.AlignCenter)

        logdate_widget.setLayout(logdate_sublayout)

        date_label = QLabel()
        date_label.setText("Date")
        self.tablelayout.addWidget(date_label, 1, 0)
        self.tablelayout.addWidget(logdate_widget, 1, 1)

        #DISTANCE
        distance_widget = QWidget()
        distance_sublayout = QHBoxLayout()

        distance = QLineEdit()
        unit = QComboBox()
        unit.addItems(["km", "miles"])

        distance_sublayout.addWidget(distance, alignment=Qt.AlignCenter)
        distance_sublayout.addWidget(unit, alignment=Qt.AlignCenter)

        distance_widget.setLayout(distance_sublayout)

        distance_label = QLabel()
        distance_label.setText("Distance")

        self.tablelayout.addWidget(distance_label, 2, 0)
        self.tablelayout.addWidget(distance_widget, 2, 1)

        #ELAVATION
        elavation_widget = QWidget()
        elavation_sublayout = QHBoxLayout()

        elavation_box = QSpinBox()
        elavation_box.setMinimum(0)
        elavation_box.setMaximum(500)
        elavation_box.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        elavation_box.setMinimumSize(70, 10)

        unit_label = QLabel()
        unit_label.setText("metres")

        elavation_sublayout.addWidget(elavation_box, alignment=Qt.AlignCenter)
        elavation_sublayout.addWidget(unit_label, alignment=Qt.AlignCenter)

        elavation_widget.setLayout(elavation_sublayout)

        elavation_label = QLabel()
        elavation_label.setText("Elavation")

        self.tablelayout.addWidget(elavation_label, 3, 0)
        self.tablelayout.addWidget(elavation_widget, 3, 1)


        #COMMENTS
        comment_box = QLineEdit()
        comment_box.setMinimumSize(100, 50)
        comment_label = QLabel()
        comment_label.setText("Comments")

        self.tablelayout.addWidget(comment_label, 4, 0)
        self.tablelayout.addWidget(comment_box, 4, 1)


        #RATING
        rating_widget = QWidget()
        rating_sublayout = QHBoxLayout()

        rating_box = QDoubleSpinBox()
        rating_box.setDecimals(1)
        rating_box.setSingleStep(0.5)
        rating_box.setMinimum(0.0)
        rating_box.setMaximum(10.0)
        rating_label = QLabel()
        rating_label.setText("Rating")

        rating_sublayout.addWidget(rating_box, alignment=Qt.AlignCenter)
        rating_widget.setLayout(rating_sublayout)

        self.tablelayout.addWidget(rating_label, 5, 0)
        self.tablelayout.addWidget(rating_widget, 5, 1)


        """   
        for count, run_input in enumerate(param.run_inputs):
            label_i = QLabel()
            label_i.setText(run_input)
            self.tablelayout.addWidget(label_i, count + 1, 0)

            input_i = QTextEdit()
            self.tablelayout.addWidget(input_i, count + 1 ,1)
        """


        self.tablewin.setLayout(self.tablelayout)


class MasterWindow(QMainWindow):
    app = QApplication([])
    app.setWindowIcon(QIcon('/Users/of15641/Documents/OwnProjects/exercise_log/run_image.png'))
    app.setApplicationName("Exercise log")
    app.setApplicationDisplayName("Exercise log")


    def picture(self):
        picture_label = QLabel()
        cwd = os.getcwd()
        pixmap = QPixmap(cwd + 'run_image.png')
        pixmap_resized = pixmap.scaled(100, 100, Qt.KeepAspectRatio)
        picture_label.setPixmap(pixmap_resized)

        self.layout.addWidget(picture_label)

    def table_buttons(self, row : int, column : int):
        self.layout.addWidget(QLabel("Input tables:"), row, column)

        self.run_button = TableButton({"text" : "Runs"})
        self.run_window = RunWindow({"table" : "Runs"})

        self.run_button.clicked.connect(self.run_window.clicked)
        self.calisthenics_button = TableButton({"text": "Calisthenics"})

        self.layout.addWidget(self.run_button, row+1, column)
        self.layout.addWidget(self.calisthenics_button, row+2, column)

    def weekly_data_setup(self):
        self.weekly_data = QLabel()
        weekly_text = " this will be the weekly data \n"
        for day in param.days:
            weekly_text += " %s: \n \n" % day
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
