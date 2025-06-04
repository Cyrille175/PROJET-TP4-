from martypy import Marty
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
                break

    return None

if __name__ == "__main__":
    my_marty = Marty("wifi", "192.168.0.107")
    my_marty.stand_straight(move_time =2000)
    couleurs = calibrate_colors(my_marty, "left")
    if not couleurs:
        print("Aucune couleur calibrée. Fin du programme.")
    else:
        print("\n=== MODE IDENTIFICATION EN BOUCLE ===")
        print("Place une couleur sous le pied. Appuie sur Ctrl+C pour arrêter.")
        try:
            while True:
                input(f"Appuies pour detecter une couleur")
                couleur = identify_color(my_marty, couleurs, "left", 1)
                if couleur:
                    print(f" Couleur détectée : {couleur}")
                    emotion = return_emotion(couleur, my_marty)
                    print(f" Émotion associée : {emotion}")
                    # Je peux ici ajouter des actions (LED, mouvement, etc.)
                else:
                    print(" Aucune couleur reconnue.")
                my_marty.walk(7, 'auto', 0, 25, 1500, None)
                my_marty.stand_straight(move_time=2000)

        except KeyboardInterrupt:
            print("\nFin du programme.")

