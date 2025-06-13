from deplacements import left_case, forward_case, right_case, backward_case
from martypy import Marty

from identify_color import calibrate_colors, reaction_emotion
try:
    my_marty = Marty("wifi", "192.168.0.101")
except:
    print("Erreur de connexion")


couleurs = calibrate_colors(my_marty, 'left')

def open_file(fichier):
    dance_data = []
    with open(fichier, "r") as file:
        entete = file.readline()
        print(entete)
        for line in file:
            number = line[0]
            direction = line[1]
            dance_data.append({
                "number": number,
                "direction": direction
            })
    return dance_data



def deplacement(elements):
    reaction_emotion(couleurs)
    for item in elements:
        direction = item["direction"]
        number = int(item["number"])
        if (direction == "L"):
            for i in range(number):
                left_case()
                reaction_emotion(couleurs)

        if (direction == "U"):
            for i in range(number):
                forward_case()
                reaction_emotion(couleurs)

        if (direction == "R"):
            for i in range(number):
                right_case()
                reaction_emotion(couleurs)

        if (direction == "B"):
            for i in range(number):
                backward_case()
                reaction_emotion(couleurs)


elements = open_file("dominance.dance")
deplacement(elements)
