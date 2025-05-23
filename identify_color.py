from martypy import Marty

from lecture_feels import return_emotion

my_marty = Marty("wifi", "192.168.0.103")
left_color = my_marty.get_ground_sensor_reading("left")
right_color = my_marty.get_ground_sensor_reading("right")


my_marty.get_ready()

calibration_couleurs = {
    "purple": (35,40),
    "green": (40,43),
    "blue": (45,50),
    "red":(100,115),
    "yellow": (120,140)
}


def detecter_couleur():
    for couleur, (min_val, max_val) in calibration_couleurs.items():
        if min_val <= left_color <= max_val:
            return couleur
    return "blue"

print(left_color)
color = detecter_couleur()
print(color)
emotion = return_emotion(color, my_marty)
print(emotion)


my_marty.eyes(emotion, 1000,  None)





# Pour le violet je recupere sur le coté gauche 37-38-39 et sur le coté droit 182-184
# Pour le vert je recupere sur le coté gauche 42 et sur le coté droit 174
# Pour le bleu je recupere sur le coté gauche 46 et sur le coté droit 183
# Pour le rouge je recupere sur le coté gauche 115 et sur le coté droit 185
# Pour le jaune je recupere sur le coté gauche 140 et sur le coté droit 188
