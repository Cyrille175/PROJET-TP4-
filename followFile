import deplacementD


positions = []

with open("cirle.dance", "r", encoding="utf-8") as f:
    lignes = f.readlines()

# On ignore la premiere ligne ("ABS 5"):
for ligne in lignes[1:]:
    ligne = ligne.strip()
    if ligne and len(ligne) == 2 and ligne.isdigit():
        x = int(ligne[0])
        y = int(ligne[1])
        positions.append({"x": x, "y": y})

print(positions) # test


# follow mouvement algorithme:

# Exemple de fonctions de mouvement (à adapter à ton robot réel)



# Exemple de positions extraites du fichier (x, y)
positions = [
    {"x": 2, "y": 2},
    {"x": 2, "y": 3},
    {"x": 2, "y": 4},
    {"x": 3, "y": 4},
    {"x": 4, "y": 4}
]

# Parcours de chaque paire de positions successives
for i in range(len(positions) - 1):
    pos_actuelle = positions[i]
    pos_suivante = positions[i + 1]

    dx = pos_suivante["x"] - pos_actuelle["x"]
    dy = pos_suivante["y"] - pos_actuelle["y"]

    # Bouger en x
    if dx == 1:
        deplacementD.right_case()
    elif dx == -1:
        deplacementD.left_case()

    # Bouger en y
    if dy == 1:
        deplacementD.forward_case()
    elif dy == -1:
        deplacementD.backward_case()

