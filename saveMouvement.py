# saveMouvement.py

direction_codes = {
    "forward_case": "F",
    "backward_case": "B",
    "right_case": "R",
    "left_case": "L"
}

# Variables globales pour memoriser le dernier mouvement
last_move = None
move_count = 0

def save_movement(direction):
    """
    Enregistre les mouvements successifs, ex : 2R, 3F...
    """
    global last_move, move_count

    if direction not in direction_codes:
        return

    if direction == last_move:
        move_count += 1
    else:
        if last_move is not None:
            # Sauvegarder le mouvement precedent compresse
            code = direction_codes[last_move]
            with open("mouvement_path.txt", "a", encoding="utf-8") as f:
                f.write(f"{move_count}{code}\n")
        # Nouveau mouvement
        last_move = direction
        move_count = 1

def flush_movement():
    """
    supprime tout le contenu du fichier mouvement_path.txt
    """
    global last_move, move_count

    #vide le fichier
    open("mouvement_path.txt", "w", encoding="utf-8").close()

    #reinitialisation des variables internes
    last_move = None
    move_count = 0
