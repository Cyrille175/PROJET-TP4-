from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys
from deplacement import forward, backward, right, left, stand, forward_case, backward_case, right_case, left_case
from martypy import Marty
my_marty = Marty("wifi","192.168.0.107")    #Adresse à adapter

class Window(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("Panneau de contrôle de Marty")
        vbox = QVBoxLayout()

        fw = QPushButton('Avant', self)
        fw.setGeometry(100,100,100,100)
        fw.clicked.connect(self.appui_fw)
        bw = QPushButton('Arrière', self)
        bw.setGeometry(100,100,100,100)
        bw.clicked.connect(self.appui_bw)
        r = QPushButton('Droite', self)
        r.setGeometry(100,100,100,100)
        r.clicked.connect(self.appui_r)
        l = QPushButton('Gauche', self)
        l.setGeometry(100,100,100,100)
        l.clicked.connect(self.appui_l)
        std = QPushButton('Stand', self)
        std.setGeometry(100,100,100,100)
        std.clicked.connect(self.appui_std)

        fw1 = QPushButton('Avant case', self)
        fw1.setGeometry(100,100,100,100)
        fw1.clicked.connect(self.appui_fw1)
        bw1 = QPushButton('Arrière case', self)
        bw1.setGeometry(100,100,100,100)
        bw1.clicked.connect(self.appui_bw1)
        r1 = QPushButton('Droite case', self)
        r1.setGeometry(100,100,100,100)
        r1.clicked.connect(self.appui_r1)
        l1 = QPushButton('Gauche case', self)
        l1.setGeometry(100,100,100,100)
        l1.clicked.connect(self.appui_l1)

        vbox.addWidget(fw)
        vbox.addWidget(bw)
        vbox.addWidget(r)
        vbox.addWidget(l)
        vbox.addWidget(std)
        vbox.addWidget(fw1)
        vbox.addWidget(bw1)
        vbox.addWidget(r1)
        vbox.addWidget(l1)

        self.setLayout(vbox)
        

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

    def appui_fw1(self) :
        forward_case()
    
    def appui_bw1(self) :
        backward_case()

    def appui_r1(self) :
        right_case()

    def appui_l1(self) :
        left_case()

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())