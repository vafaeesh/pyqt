import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog, QPushButton, QVBoxLayout, QApplication, QSplashScreen 
from PyQt6.QtCore import QTimer

class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.flashSplash()
        
        self.b1 = QPushButton('Display screensaver')
        self.b1.clicked.connect(self.flashSplash)

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.b1)

    def flashSplash(self):
        self.splash = QSplashScreen(QPixmap('splash.jpg'))

        # By default, SplashScreen will be in the center of the screen.
        # You can move it to a specific location if you want:
        # self.splash.move(10,10)

        self.splash.show()

        # Close SplashScreen after 2 seconds (2000 ms)
        QTimer.singleShot(2000, self.splash.close)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Dialog()
    main.show()
    sys.exit(app.exec())
