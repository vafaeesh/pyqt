from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

import sys
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.input = QLineEdit()
        self.lable = QLabel()
        self.input.textChanged.connect(self.lable.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.lable)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
  

app = QApplication(sys.argv)
# Create splashscreen
splash_pix = QPixmap('splash.jpg')
splash = QSplashScreen(splash_pix, Qt.WindowType.WindowStaysOnTopHint)
# add fade to splashscreen 
opaqueness = 0.0
step = 0.1
splash.setWindowOpacity(opaqueness)
splash.show()
while opaqueness < 1:
    splash.setWindowOpacity(opaqueness)
    time.sleep(step) # Gradually appears
    opaqueness+=step
time.sleep(1) # hold image on screen for a while
splash.close() # close the splash screenapp.processEvents()
window = MainWindow()
window.show()
splash.finish(window)
app.exec()