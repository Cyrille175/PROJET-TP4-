from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
import sys
from deplacement import forward, backward, right, left, stand
from martypy import Marty
my_marty = Marty("wifi","192.168.0.107")

class Window(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("Panneau de contrôle de Marty")
        self.create_buttons()

    def create_buttons(self) :
        fw = QPushButton('Avant', self)
        fw.setGeometry(100,100,100,100)
        fw.clicked.connect(self.appui_fw)
        bw = QPushButton('Arrière', self)
        bw.setGeometry(100,200,100,100)
        bw.clicked.connect(self.appui_bw)
        r = QPushButton('Droite', self)
        r.setGeometry(100,100,200,100)
        r.clicked.connect(self.appui_r)
        l = QPushButton('Gauche', self)
        l.setGeometry(100,100,100,200)
        l.clicked.connect(self.appui_l)
        std = QPushButton('Stand', self)
        std.setGeometry(200,100,100,100)
        std.clicked.connect(self.appui_std)

    def appui_fw(self) :
        forward()
    
    def appui_bw(self) :
        backward()

    def appui_r(self) :
        right()

    def appui_l(self) :
        left()

    def appui_std(self) :
        stand()

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())