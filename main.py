import sys
from PyQt5.QtWidgets import QMainWindow, QMenuBar, QMenu, QStatusBar
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ScreenCaptureWindow(QMainWindow):
    def __init__(self):
        super(ScreenCaptureWindow, self).__init__()
        self.resize(700, 500)
        widget = QWidget()
        # Create buttons: close, record, screenshot.
        self.btn_close = QPushButton(QIcon("./icons/close.png"), "")
        self.btn_record = QPushButton(QIcon("./icons/record.png"), "")
        self.btn_screenshot = QPushButton(QIcon("./icons/screenshot.png"), "")
        # Create signals: pressed, released, clicked.
        self.btn_close.clicked.connect(self.clicked_btn_closed)
        # Add animated gif for Record button.
        self.movie = QMovie("./icons/record_anim.gif")
        # self.movie.start()
        self.movie.frameChanged.connect(self.update_movie)
        self.btn_record.pressed.connect(self.pressed_btn_record)
        self.btn_record.released.connect(self.released_btn_record)

        self.btn_screenshot.pressed.connect(self.pressed_btn_screenshot)
        self.btn_screenshot.released.connect(self.released_btn_screenshot)
        # Make buttons transparent.
        # self.btn_close.setStyleSheet("selection-color: rgb(129, 228, 255);background-color: qlineargradient(spread:pad, x1:0.915, y1:1, x2:1, y2:0, stop:0 rgba(120, 120, 120, 163), stop:1 rgba(255, 255, 255, 255));")
        self.btn_close.setStyleSheet( "background: transparent;")
        self.btn_record.setStyleSheet( "background: transparent;")
        self.btn_screenshot.setStyleSheet( "background: transparent;")
        # Layout
        layout = QVBoxLayout()
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.btn_screenshot)
        hlayout.addWidget( self.btn_record)
        hlayout.addWidget(self.btn_close)
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
        # Status bar. It creates a graping point fro resize.
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
            delta = QPoint(event.globalPos() - self.P)
            self.move(self.x() + delta.x(), self.y() + delta.y())
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


    def pressed_btn_record(self):
        print("pressed")
        self.btn_record.setIcon(QIcon("./icons/record_focused1.png"))
    def released_btn_record(self):
        print("pressed")
        self.movie.start()
    def update_movie(self):
        # Update Record GIF Icon
        self.btn_record.setIcon(QIcon(self.movie.currentPixmap()))
        self.movie.setScaledSize(QSize(205, 178))
        # self.movie.start()
    def pressed_btn_screenshot(self):
        self.btn_screenshot.setIcon(QIcon("./icons/screenshot_focused1.png"))
    def released_btn_screenshot(self):
        self.btn_screenshot.setIcon(QIcon("./icons/screenshot.png"))
    def clicked_btn_closed(self):
        self.btn_close.setIcon(QIcon("./icons/close_focused.png"))
        QTimer.singleShot(100,self.delayed_exit)
    def delayed_exit(self):
        self.close()


app = QApplication(sys.argv)
# Create the main window
window = ScreenCaptureWindow()
window.show()

sys.exit(app.exec_())
