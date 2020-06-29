from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import gui.utils

class RunWindow(gui.utils.TableWindow):
    def add_to_table(self, run_table):
        print("add")

    def __init__(self, param_dict, run_table):
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
        distance.setValidator(QDoubleValidator())

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

        #ADD
        input_button = QPushButton()
        input_button.setText("ADD")
        input_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        input_button.toggle()
        input_button.clicked.connect(lambda : self.add_to_table(run_table))

        self.tablelayout.addWidget(input_button, 6, 0, 1, 2)

        self.tablewin.setLayout(self.tablelayout)
