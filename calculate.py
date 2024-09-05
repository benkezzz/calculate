from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import datetime
import sys
 
 
class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Калькулятор")
 
        self.w_width = 400
 
        self.w_height = 750
 
        self.setGeometry(100, 100, self.w_width, self.w_height)
 
        self.UiComponents()
 
        self.show()
 
    def UiComponents(self):

        #Заголовок
 
        head = QLabel("Сколько дней прошло до текущей даты", self)
 
        head.setWordWrap(True)
 
        head.setGeometry(0, 10, 400, 60)
 
        font = QFont('Times', 14)
        font.setBold(True)
 
        head.setFont(font)
 
        head.setAlignment(Qt.AlignCenter)

        #Заголовок над календарем
 
        b_label = QLabel("Выберите дату", self)
 
        b_label.setAlignment(Qt.AlignCenter)
        b_label.setGeometry(50, 95, 300, 25)
        b_label.setStyleSheet("QLabel"
                              "{"
                              "border : 1px solid black;"
                              "background : rgba(70, 70, 70, 25);"
                              "}")
        b_label.setFont(QFont('Times', 9))
 
        # Добавляем календарь

        self.calendar = QCalendarWidget(self)
 
        self.calendar.setGeometry(50, 120, 300, 180)
 
        self.calendar.setFont(QFont('Times', 6))
 
        date = QDate.currentDate()
 
        self.calendar.setMaximumDate(date)
 
        calculate = QPushButton("Посчитать", self)
 
        calculate.setGeometry(125, 330, 150, 40)
 
        calculate.clicked.connect(self.calculate)

        # Окно результата
 
        self.result = QLabel(self)
 
        self.result.setAlignment(Qt.AlignCenter)
        self.result.setGeometry(50, 400, 300, 60)
        self.result.setWordWrap(True)
        self.result.setStyleSheet("QLabel"
                                  "{"
                                  "border : 3px solid black;"
                                  "background : white;"
                                  "}")
        self.result.setFont(QFont('Times', 11))

        # Добавляем изображение

        self.picture = QLabel(self)
        
        self.pixmap = QPixmap('image.jpg')
 
        self.picture.setPixmap(self.pixmap)
 
        self.picture.resize(self.pixmap.width(),
                          self.pixmap.height())
        
        self.picture.setAlignment(Qt.AlignCenter)
        self.picture.setGeometry(-50, 500, 500, 200)

    # Функция расчета
 
    def calculate(self):
 
        re_date = self.calendar.selectedDate()
 
        year = re_date.year()
        month = re_date.month()
        day = re_date.day()
 
        current = QDate.currentDate()
 
        current = datetime.datetime.now()
 
        date = datetime.datetime(year, month, day)
 
        difference = current - date
 
        days = difference.days
 
        self.result.setText(str(days))
 
  
App = QApplication(sys.argv)
 
window = Window()
 
sys.exit(App.exec())