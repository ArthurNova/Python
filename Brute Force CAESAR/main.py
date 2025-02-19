file_input = open ("Brute force caesar/input.txt","r")
file_output = open ("Brute force caesar/output.txt","a")

# print(f.read())

def dechiffrement_caesar(texte_chiffre, cle):
    texte_dechiffre = ""

    # Boucle à travers chaque caractère de la chaine
    for char in texte_chiffre:
        # Vérifie si le caractère est une lettre
        if char.isalpha():
            # Gère la différence entre majuscule et la minuscule
            debut = ord('A') if char.isupper() else ord('a') # ord = fonction qui renvoie le code ASCII d'un caractère
            # Décalage avec la clé en inversant pour le déchiffrement
            position_initiale = ord(char) - debut # Calcule de la position de la lettre dans l'alphabet (0 à 25) | ord(char renvoie le code ASCII du caractère
            nouvelle_position = (position_initiale - cle) % 26 # calcule du décalage avec la clé (nombre de décalage) | %26 permet de revenir bouclé entre 0 et 25 uniquement (Z + décalage de 1 = A)
            nouveau_char = chr(debut + nouvelle_position) # Modification de la chaine de caractère avec le calcule réalisé précedement | chr() permet d'obtenir le carctère ASCII de la nouvelle position
            texte_dechiffre += nouveau_char # Ajoute le caractère déchiffré (text_dechiffre) à la chaine (texte_chiffre), ce qui construie progressivement le texte chiffré
        else:
            # Si ce n'est pas une lettre, on le garde tel quel (espaces, ponctuation, etc.)
            texte_dechiffre += char

    return texte_dechiffre

# Exemple d'utilisation
texte_chiffre = (file_input.read())
cle = 3 # La clé correspond au décalage utilisé pour le chiffrement, ici A -> D
texte_dechiffre = dechiffrement_caesar(texte_chiffre, cle) # Utilisation de la fonction de déchiffrement 
file_output.write(texte_dechiffre)
# print(texte_dechiffre) # Affichage de la chaine de carctère déchiffré

file_output.close()


