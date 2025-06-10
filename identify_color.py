from martypy import Marty

from emotionaction import applyEmotion
from lecture_feels import return_emotion
import time


def calibrate_colors(marty, foot):
    color_reference = {}

    print("=== MODE CALIBRAGE ===")
    print("Pose une couleur sous le pied de Marty.")
    print("Tape un nom de couleur (ex: 'rouge'), ou 'f' pour terminer le calibrage.")

    while True:
        color_name = input("Nom de la couleur (ou 'f' pour finir) : ").strip().lower()
        if color_name == "f":
            break

        input(f"Place la couleur '{color_name}' sous le pied et appuie sur Entrée...")

        if not marty.foot_on_ground(foot):
            print("Le pied n'est pas posé. Recommence.")
            continue  #me permet de ne pas executer le reste de la boucle
        marty.stand_straight(move_time=2000)
        color_values = marty.get_color_sensor_hex(foot)
        rh, gh, bh = color_values[1], color_values[2], color_values[3]
        r = int(rh,16)
        g = int(gh,16)
        b = int(bh,16)
        print(f"Couleur '{color_name}' enregistrée : R={r}, G={g}, B={b}")
        color_reference[color_name] = (r, g, b)

    return color_reference

def identify_color(marty, color_reference, foot, tolerance):
    color_values = marty.get_color_sensor_hex(foot)
    rh, gh, bh = color_values[1], color_values[2], color_values[3]
    r = int(rh,16)
    g = int(gh,16)
    b = int(bh,16)
    for color, ref_rgb in color_reference.items():
        if (abs(r - ref_rgb[0]) <= tolerance and
            abs(g - ref_rgb[1]) <= tolerance and
            abs(b - ref_rgb[2]) <= tolerance):
                return color


    return None

def reaction_emotion(couleurs):
    my_marty = Marty("wifi", "192.168.0.101")
    if not couleurs:
        print("Aucune couleur calibrée. Fin du programme.")
    else:
        print("\n=== MODE IDENTIFICATION EN BOUCLE ===")
        my_marty.stand_straight(move_time=2000)
        try:
            while True:
                couleur = identify_color(my_marty, couleurs, "left", 1)
                if couleur:
                    print(f" Couleur détectée : {couleur}")
                    emotion = return_emotion(couleur, my_marty)
                    print(f" Émotion associée : {emotion}")
                    # Je peux ici ajouter des actions (LED, mouvement, etc.)
                    applyEmotion(emotion)
                    break
                else:
                    print(" Aucune couleur reconnue.")
        except KeyboardInterrupt:
            print("Erreur avec la bibliotheque time")

