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
    Enregistre les mouvements successifs compresses, ex : 2R, 3F...
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
    a appeler a  la fin (fermeture, bouton stop...) pour enregistrer le dernier mouvement
    """
    global last_move, move_count

    if last_move is not None and move_count > 0:
        code = direction_codes[last_move]
        with open("mouvement_path.txt", "a", encoding="utf-8") as f:
            f.write(f"{move_count}{code}\n")
    last_move = None
    move_count = 0
