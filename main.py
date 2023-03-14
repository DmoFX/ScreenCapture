import sys
from PyQt5.QtWidgets import QMainWindow,QMenuBar,QMenu,QStatusBar
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ScreenshotWindow(QMainWindow):
    def __init__(self):
        super(ScreenshotWindow, self).__init__()
        self.resize(700, 500)
        widget = QWidget()
        # Create the button
        self.pushButton = QPushButton("Finished")
        # self.pushButton.setGeometry(QRect(240, 190, 90, 31))
        self.pushButton.clicked.connect(app.quit)
        # Layout
        layout = QVBoxLayout()
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.pushButton)
        hlayout.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        spacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)
        hlayout.addItem(spacer)
        layout.addLayout(hlayout)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        # Transperent BG
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        # Status bar
        s = QStatusBar()
        self.setStatusBar(s)
        # s.showMessage("recording..")
        # t = self.addToolBar("play")

        self.P = self.pos()
        self.resized = 0

    def mousePressEvent(self, event):
        print("pressed")
        self.P = event.globalPos()
    def mouseMoveEvent(self, event):
        print("move")
        print(self.resized)
        if self.resized == 0:
            delta = QPoint(event.globalPos()-self.P)
            self.move(self.x()+delta.x(),self.y()+delta.y())
            self.P = event.globalPos()
        else:
            self.resized = 0
        # print(event.globalPos())
    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        print("resize")
        self.resized = 1

    def paintEvent(self, event=None):
        painter = QPainter(self)

        painter.setOpacity(0)
        painter.setBrush(Qt.red)
        painter.setPen(QPen(Qt.white))
        painter.drawRect(self.rect())
        # w = int(self.size().width())
        # h = int(self.size().height())
        # painter.drawRect(QRect(0,0,w,h))

        painter.setOpacity(1)
        # painter.setBrush(Qt.blue)
        painter.setPen(QPen(Qt.white, 7))
        w = int(self.size().width() * 1)
        h = int(self.size().height() * 1)
        painter.drawLines([QLine(0, 0, w, 0), QLine(w, 0, w, h), QLine(w, h, 0, h), QLine(0, h, 0, 0)])


app = QApplication(sys.argv)
# Create the main window
window = ScreenshotWindow()
window.show()

sys.exit(app.exec_())