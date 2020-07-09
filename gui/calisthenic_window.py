from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from gui.utils import *
from datetime import *

class CalWindow(TableWindow):

    def add_to_table(self, cali_table):
        date = self.logdate_widget.selectedDate().toString("yyyy-MM-dd")
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        date = date.date()
        pushups = self.pushups_slider.value()
        pullups = self.pullups_slider.value()
        squats = self.squats_slider.value()

        comment = self.comment_box.text()
        rating = self.rating_box.text()

        write_data = (date, pushups, pullups, squats, comment, float(rating))

        data_check = cali_table.cali_data_check(write_data)

        if data_check:
            cali_table.write_to_table(write_data)
            self.tablelayout.addWidget(QLabel("added to database successfully"), 6, 0, 1, 2)


    def __init__(self, param_dict, cali_table):
        super().__init__(param_dict)
        # LOGDATE
        self.logdate_widget = QCalendarWidget()

        date_label = QLabel()
        date_label.setText("Date")
        self.tablelayout.addWidget(date_label, 1, 0)
        self.tablelayout.addWidget(self.logdate_widget, 1, 1)

        self.slider_widgets = QWidget()
        slider_sublayout = QGridLayout()

        # PUSHUPS
        self.pushups_slider = QSlider()
        self.pushups_slider.setMinimum(0)
        self.pushups_slider.setMaximum(100)
        self.pushups_slider.setValue(60)
        self.pushups_slider.setTickPosition(QSlider.TicksRight)
        self.pushups_slider.setTickInterval(10)

        pushups_label = QLabel("Pushups")
        pushups_value_label = QLabel(str(self.pushups_slider.value()))
        self.pushups_slider.valueChanged.connect(\
            lambda : pushups_value_label.setText(str(self.pushups_slider.value())))

        slider_sublayout.addWidget(pushups_label, 0, 0)
        slider_sublayout.addWidget(self.pushups_slider, 1, 0)
        slider_sublayout.addWidget(pushups_value_label, 2, 0)

        # PULLUPS
        self.pullups_slider = QSlider()
        self.pullups_slider.setMinimum(0)
        self.pullups_slider.setMaximum(30)
        self.pullups_slider.setValue(15)
        self.pullups_slider.setTickPosition(QSlider.TicksRight)
        self.pullups_slider.setTickInterval(10)

        pullups_label = QLabel("Pullups")
        pullups_value_label = QLabel(str(self.pullups_slider.value()))
        self.pullups_slider.valueChanged.connect(\
            lambda : pullups_value_label.setText(str(self.pullups_slider.value())))

        slider_sublayout.addWidget(pullups_label, 0, 1)
        slider_sublayout.addWidget(self.pullups_slider, 1, 1)
        slider_sublayout.addWidget(pullups_value_label, 2, 1)


        # SQUATS
        self.squats_slider = QSlider()
        self.squats_slider.setMinimum(0)
        self.squats_slider.setMaximum(100)
        self.squats_slider.setValue(75)
        self.squats_slider.setTickPosition(QSlider.TicksRight)
        self.squats_slider.setTickInterval(10)

        squats_label = QLabel("Squats")
        squats_value_label = QLabel(str(self.squats_slider.value()))
        self.squats_slider.valueChanged.connect(\
            lambda : squats_value_label.setText(str(self.squats_slider.value())))

        slider_sublayout.addWidget(squats_label, 0, 2)
        slider_sublayout.addWidget(self.squats_slider, 1, 2)
        slider_sublayout.addWidget(squats_value_label, 2, 2)

        self.tablelayout.addWidget(QLabel("reps"), 2, 0)
        self.slider_widgets.setLayout(slider_sublayout)
        self.tablelayout.addWidget(self.slider_widgets, 2, 1)


        # COMMENTS
        self.comment_box = QLineEdit()
        self.comment_box.setMinimumSize(100, 50)
        comment_label = QLabel()
        comment_label.setText("Comments")

        self.tablelayout.addWidget(comment_label, 3, 0)
        self.tablelayout.addWidget(self.comment_box, 3, 1)

        # RATING
        rating_widget = QWidget()
        rating_sublayout = QHBoxLayout()

        self.rating_box = QDoubleSpinBox()
        self.rating_box.setDecimals(1)
        self.rating_box.setSingleStep(0.5)
        self.rating_box.setMinimum(0.0)
        self.rating_box.setMaximum(10.0)
        rating_label = QLabel()
        rating_label.setText("Rating")

        rating_sublayout.addWidget(self.rating_box, alignment=Qt.AlignCenter)
        rating_widget.setLayout(rating_sublayout)

        self.tablelayout.addWidget(rating_label, 4, 0)
        self.tablelayout.addWidget(rating_widget, 4, 1)

        # ADD
        add_button = QPushButton()
        add_button.setText("ADD")
        add_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        add_button.toggle()
        add_button.clicked.connect(lambda: self.add_to_table(cali_table))

        self.tablelayout.addWidget(add_button, 5, 0, 1, 2)

        self.tablewin.setLayout(self.tablelayout)
