feels_data = []
with open("real.feels", "r") as file:
    for line in file:
        color, emotion, led = line.strip().split(";")
        feels_data.append({
            "color": color.lower(),
            "emotion": emotion,
            "led": led
        })

def return_emotion(couleur_detectee, my_marty):
    couleur_detectee = couleur_detectee.lower()
    for item in feels_data:
        if item["color"] == couleur_detectee:
            return item["emotion"]

    print("La couleur n'existe pas dans le fichier real.feels")
    return "normal"
