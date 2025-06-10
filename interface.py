from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtCore import QSize
import sys
from deplacement import forward, backward, right, left, stand, forward_case, backward_case, right_case, left_case
from saveMouvement import save_movement, flush_movement
from martypy import Marty
my_marty = Marty("wifi","192.168.0.101")    #Adresse à adapter

class Window(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("Panneau de contrôle de Marty")
        self.setContentsMargins(20, 20, 20, 20)

        desc1 = QLabel(self)
        desc1.setText('Déplacements en pas')
        desc1.move(60, 30)
        fw = QPushButton('↑', self)     #Boutons de déplacement d'1 pas
        fw.setFixedSize(QSize(80, 50))
        fw.move(80, 50)
        fw.clicked.connect(self.appui_fw)
        bw = QPushButton('↓', self)
        bw.setFixedSize(QSize(80, 50))
        bw.move(80, 150)
        bw.clicked.connect(self.appui_bw)
        r = QPushButton('→', self)
        r.setFixedSize(QSize(80, 50))
        r.move(160, 100)
        r.clicked.connect(self.appui_r)
        l = QPushButton('←', self)
        l.setFixedSize(QSize(80, 50))
        l.move(0, 100)
        l.clicked.connect(self.appui_l)

        std = QPushButton('Stand', self)    #Bouton pour se tenir droit
        std.setFixedSize(QSize(80, 50))
        std.move(330, 100)
        std.clicked.connect(self.appui_std)

        desc2 = QLabel(self)
        desc2.setText('Déplacements en cases')
        desc2.move(550, 30)
        fw1 = QPushButton('↑', self)   #Boutons de déplacement d'1 case
        fw1.setFixedSize(QSize(80, 50))
        fw1.move(580, 50)
        fw1.clicked.connect(self.appui_fw1)
        bw1 = QPushButton('↓', self)
        bw1.setFixedSize(QSize(80, 50))
        bw1.move(580, 150)
        bw1.clicked.connect(self.appui_bw1)
        r1 = QPushButton('→', self)
        r1.setFixedSize(QSize(80, 50))
        r1.move(660, 100)
        r1.clicked.connect(self.appui_r1)
        l1 = QPushButton('←', self)
        l1.setFixedSize(QSize(80, 50))
        l1.move(500, 100)
        l1.clicked.connect(self.appui_l1)       

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
        flush_movement()

    def appui_fw1(self) :
        forward_case()
        save_movement('forward_case')
    
    def appui_bw1(self) :
        backward_case()
        save_movement("backward_case")

    def appui_r1(self) :
        right_case()
        save_movement("right_case")

    def appui_l1(self) :
        left_case()
        save_movement("left_case")

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())