def nettoyer(texte):

    return texte.strip().lower().replace(" ", "")

def couleur_existe(couleur, nom_fichier="real.feels"):

    couleur = nettoyer(couleur)
    try:
        with open(nom_fichier, "r") as fichier:
            for ligne in fichier:
                champs = ligne.strip().split(";")
                if len(champs) >= 1 and nettoyer(champs[0]) == couleur:
                    return True
    except FileNotFoundError:
        print("Le fichier n'existe pas encore → donc la couleur n'existe pas non plus")
        return False
    return False

def ajouter_couleur_emotion(couleur, emotion, code_hex_rgb, nom_fichier="real.feels"):

    couleur = nettoyer(couleur)
    emotion = nettoyer(emotion)
    code_hex_rgb = nettoyer(code_hex_rgb)

    ligne = f"{couleur};{emotion};{code_hex_rgb}\n"

    try:
        with open(nom_fichier, "rb+") as fichier:
            fichier.seek(0, 2)  # Aller à la fin du fichier
            if fichier.tell() > 0:
                fichier.seek(-1, 2)
                last_char = fichier.read(1)
                if last_char != b"\n":
                    fichier.write(b"\n")
            fichier.write(ligne.encode())
    except FileNotFoundError:
        with open(nom_fichier, "wb") as fichier:
            fichier.write(ligne.encode())

    print(f"Ligne ajoutée : {ligne.strip()}")


# === Programme principal ===

print("=== AJOUT D'UNE NOUVELLE COULEUR DANS real.feels ===")

couleur = input("Nom de la couleur (ex: red) : ")
emotion = input("Émotion associée (ex: happy) : ")
code_hex = input("Code RGB hexadécimal (ex: ff0000) : ")

# Nettoyage automatique des entrées
couleur = nettoyer(couleur)
emotion = nettoyer(emotion)
code_hex = nettoyer(code_hex)

# Vérification et ajout
if not couleur_existe(couleur):
    ajouter_couleur_emotion(couleur, emotion, code_hex)
else:
    print(f"️ La couleur '{couleur}' existe déjà dans le fichier.")
