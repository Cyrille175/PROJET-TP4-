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

# Parcours de chaque paire de positions successives
for i in range(len(positions) - 1):
    pos_actuelle = positions[i]
    pos_suivante = positions[i + 1]

    # Deplacement en x
    dx = pos_suivante["x"] - pos_actuelle["x"]
    if dx > 0:
        for _ in range(dx):
            deplacementD.right_case()
    elif dx < 0:
        for _ in range(-dx):
            deplacementD.left_case()

    # Deplacement en y
    dy = pos_suivante["y"] - pos_actuelle["y"]
    if dy > 0:
        for _ in range(dy):
            deplacementD.forward_case()
    elif dy < 0:
        for _ in range(-dy):
            deplacementD.backward_case()
            
            
# je dit que c'est plus precie que alterner les mouvemeent x et y !!!!!!
