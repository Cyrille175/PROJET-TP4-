# Importation de QTimer pour gérer des événements temporisés
from PyQt6.QtCore import QTimer
# Importation des widgets nécessaires pour créer l’interface utilisateur
from PyQt6.QtWidgets import (
    QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox, QMessageBox
)
# Importation de QSize pour définir des tailles fixes d’éléments
from PyQt6.QtCore import QSize
# Importation de la classe Marty pour interagir avec le robot
from martypy import Marty

# Importation des fonctions de déplacement et de gestion du robot
from deplacements import forward, backward, right, left, stand, forward_case, backward_case, right_case, left_case
# Importation des fonctions pour sauvegarder ou vider les mouvements
from saveMovement import save_movement, flush_movement
# Importation de la fonction pour appliquer une émotion
from emotionaction import applyEmotion
# Importation de la fonction pour obtenir l’émotion associée à une couleur
from lecture_feels import return_emotion

# Définition de la classe principale de la fenêtre graphique
class Window(QWidget):
    def __init__(self):
        super().__init__()  # Appel au constructeur de la classe parente QWidget
        self.setWindowTitle("Panneau de contrôle de Marty")  # Définition du titre de la fenêtre
        self.my_marty = None  # Variable pour stocker l’objet Marty une fois connecté
        self.color_reference = {}  # Dictionnaire pour stocker les couleurs calibrées
        self.battery_label = QLabel("Batterie: N/A")  # Label affichant le niveau de batterie
        flush_movement()  # Vide les mouvements précédemment enregistrés
        self.init_ui()  # Initialisation de l’interface graphique

        # Configuration d’un timer qui mettra à jour la batterie toutes les 5 secondes
        self.battery_timer = QTimer()
        self.battery_timer.timeout.connect(self.update_battery)  # Connexion à la fonction update_battery
        self.battery_timer.start(5000)  # Démarrage du timer toutes les 5000 ms (5 sec)

    def init_ui(self):
        # Champ de saisie pour l’adresse IP de Marty
        self.inputIP = QLineEdit()
        self.inputIP.setPlaceholderText("Adresse IP de Marty")  # Texte indicatif
        self.inputIP.setFixedSize(QSize(200, 30))  # Taille fixe

        # Bouton pour lancer la connexion
        self.btn_connect = QPushButton("Connexion")
        self.btn_connect.setFixedSize(QSize(100, 30))  # Taille fixe
        self.btn_connect.clicked.connect(self.connect_to_marty)  # Connexion au gestionnaire de clic

        # Mise en page horizontale pour la barre supérieure
        top_bar = QHBoxLayout()
        top_bar.addWidget(self.inputIP)  # Ajout du champ IP
        top_bar.addWidget(self.btn_connect)  # Ajout du bouton de connexion
        top_bar.addStretch()  # Ajout d’un espace extensible
        top_bar.addWidget(self.battery_label)  # Ajout du label de batterie

        # Boutons de déplacement simples
        btn_fw = QPushButton("↑")
        btn_fw.clicked.connect(lambda: forward(self.my_marty))  # Avancer
        btn_bw = QPushButton("↓")
        btn_bw.clicked.connect(lambda: backward(self.my_marty))  # Reculer
        btn_l = QPushButton("←")
        btn_l.clicked.connect(lambda: left(self.my_marty))  # Tourner à gauche
        btn_r = QPushButton("→")
        btn_r.clicked.connect(lambda: right(self.my_marty))  # Tourner à droite
        btn_std = QPushButton("Stand")
        btn_std.clicked.connect(lambda: (flush_movement(), stand(self.my_marty)))  # Remise debout et vidage des mouvements

        # Mise en page des boutons de déplacement simple
        grid_simple = QGridLayout()
        grid_simple.addWidget(btn_fw, 0, 1)
        grid_simple.addWidget(btn_l, 1, 0)
        grid_simple.addWidget(btn_r, 1, 2)
        grid_simple.addWidget(btn_bw, 2, 1)
        grid_simple.addWidget(btn_std, 1, 3)

        # Encadré pour les déplacements simples
        group_simple = QGroupBox("Déplacements simples")
        group_simple.setLayout(grid_simple)

        # Boutons de déplacement avec réaction émotionnelle
        btn_fw1 = QPushButton("↑")
        btn_fw1.clicked.connect(lambda: self.move_and_react('forward_case'))
        btn_bw1 = QPushButton("↓")
        btn_bw1.clicked.connect(lambda: self.move_and_react('backward_case'))
        btn_l1 = QPushButton("←")
        btn_l1.clicked.connect(lambda: self.move_and_react('left_case'))
        btn_r1 = QPushButton("→")
        btn_r1.clicked.connect(lambda: self.move_and_react('right_case'))

        # Mise en page des déplacements avec réaction
        grid_case = QGridLayout()
        grid_case.addWidget(btn_fw1, 0, 1)
        grid_case.addWidget(btn_l1, 1, 0)
        grid_case.addWidget(btn_r1, 1, 2)
        grid_case.addWidget(btn_bw1, 2, 1)

        # Encadré pour les déplacements d’une case avec émotion
        group_case = QGroupBox("Déplacement d'une case avec émotion")
        group_case.setLayout(grid_case)

        # Champ de saisie pour le nom de la couleur à calibrer
        self.inputCalibrage = QLineEdit()
        self.inputCalibrage.setPlaceholderText("Nom de la couleur")  # Texte indicatif
        self.inputCalibrage.returnPressed.connect(self.valider_calibrage)  # Lancer la calibration quand on appuie sur Entrée

        # Bouton pour démarrer le calibrage
        btn_calibrage = QPushButton("Calibrer")
        btn_calibrage.clicked.connect(self.indiquer_calibrage)

        # Label pour afficher la couleur détectée
        self.label_detected_color = QLabel("Couleur détectée : N/A")

        # Bouton pour exécuter la chorégraphie de danse
        self.btn_dance = QPushButton("Lancer circle.dance")
        self.btn_dance.clicked.connect(self.executer_dance)

        # Mise en page horizontale du bas (calibrage + détection + danse)
        layout_bas = QHBoxLayout()
        layout_bas.addWidget(self.inputCalibrage)
        layout_bas.addWidget(btn_calibrage)
        layout_bas.addStretch()
        layout_bas.addWidget(self.label_detected_color)
        layout_bas.addWidget(self.btn_dance)

        # Mise en page centrale (les deux groupes de boutons)
        layout_milieu = QHBoxLayout()
        layout_milieu.addWidget(group_simple)
        layout_milieu.addWidget(group_case)

        # Mise en page principale verticale
        layout = QVBoxLayout()
        layout.addLayout(top_bar)
        layout.addLayout(layout_milieu)
        layout.addSpacing(15)  # Espace entre le milieu et le bas
        layout.addLayout(layout_bas)
        self.setLayout(layout)  # Application de la mise en page principale

    def connect_to_marty(self):
        ip = self.inputIP.text().strip()  # Récupération de l’IP entrée par l’utilisateur
        if not ip:
            print("Veuillez entrer une adresse IP.")
            return
        try:
            self.my_marty = Marty("wifi", ip)  # Connexion au robot via Wi-Fi
            print("Connexion réussie à Marty.")
        except Exception as e:
            print("Erreur de connexion :", e)

    def move_and_react(self, direction):
        # Selon la direction choisie, le mouvement est enregistré et exécuté
        if direction == "forward_case":
            save_movement('forward_case')
            forward_case(self.my_marty)
        elif direction == "backward_case":
            save_movement('backward_case')
            backward_case(self.my_marty)
        elif direction == "left_case":
            save_movement('left_case')
            left_case(self.my_marty)
        elif direction == "right_case":
            save_movement('right_case')
            right_case(self.my_marty)
        self.reagir_couleur()  # Analyse la couleur après le déplacement

    def indiquer_calibrage(self):
        print("Saisis le nom de la couleur, puis appuie sur Entrée.")  # Message d'instruction

    def valider_calibrage(self):
        if self.my_marty is None:
            print("Robot non connecté.")
            return
        color_name = self.inputCalibrage.text().strip().lower()  # Récupération du nom de la couleur
        if not color_name:
            print("Nom de couleur vide.")
            return
        if not self.my_marty.foot_on_ground("left"):
            print("Le pied n'est pas posé. Recommence.")
            return
        self.my_marty.stand_straight(move_time=2000)  # Mise debout pour lecture stable
        color_values = self.my_marty.get_color_sensor_hex("left")  # Lecture de la couleur
        r = int(color_values[1], 16)  # Conversion hexadécimale en entier
        g = int(color_values[2], 16)
        b = int(color_values[3], 16)
        self.color_reference[color_name] = (r, g, b)  # Enregistrement dans le dictionnaire
        print(f"Couleur '{color_name}' enregistrée : R={r}, G={g}, B={b}")

    def reagir_couleur(self):
        if not self.color_reference or self.my_marty is None:
            print("Pas de couleur calibrée ou robot non connecté.")
            return
        color_values = self.my_marty.get_color_sensor_hex("left")  # Lecture de la couleur actuelle
        r = int(color_values[1], 16)
        g = int(color_values[2], 16)
        b = int(color_values[3], 16)
        print(f"Couleur détectée : R={r}, G={g}, B={b}")
        for nom, (rc, gc, bc) in self.color_reference.items():  # Parcours des couleurs enregistrées
            if abs(r - rc) <= 2 and abs(g - gc) <= 2 and abs(b - bc) <= 2:
                print(f"→ Couleur reconnue : {nom}")
                self.label_detected_color.setText(f"Couleur détectée : {nom}")
                emotion = return_emotion(nom)  # Récupération de l’émotion associée
                print(f"→ Émotion : {emotion}")
                applyEmotion(nom, emotion, self.my_marty)  # Application de l’émotion au robot
                return
        print("→ Couleur non reconnue.")  # Si aucune couleur ne correspond

    # Mise à jour régulière du niveau de batterie
    def update_battery(self):
        if self.my_marty is None:
            self.battery_label.setText("Batterie: N/A")
            return
        try:
            battery = self.my_marty.get_battery_level()  # Lecture de la batterie
            self.battery_label.setText(f"Batterie : {battery}%")  # Affichage dans le label
        except Exception as e:
            print("Erreur lecture batterie :", e)
            self.battery_label.setText("Batterie: Erreur")

    def executer_dance(self):
        if not self.color_reference or self.my_marty is None:
            print("Veuillez calibrer et connecter Marty avant de lancer la danse.")
            return
        try:
            with open("dominance.dance", "r") as file:  # Ouverture du fichier .dance
                entete = file.readline()  # Lecture de l’en-tête
                print(f"Fichier ouvert : {entete.strip()}")
                for line in file:  # Parcours des lignes suivantes
                    number = int(line[0])  # Nombre de fois
                    direction = line[1].strip()  # Direction à suivre
                    for _ in range(number):  # Répétition du mouvement
                        if direction == "L":
                            left_case(self.my_marty)
                        elif direction == "U":
                            forward_case(self.my_marty)
                        elif direction == "R":
                            right_case(self.my_marty)
                        elif direction == "B":
                            backward_case(self.my_marty)
                        self.reagir_couleur()  # Réaction après chaque déplacement
        except FileNotFoundError:
            print("Fichier .dance introuvable.")  # Erreur si le fichier n’est pas trouvé
