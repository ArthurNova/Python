import random

winable_round = int(input("Combien de manche gagnante voulez vous jouer ? : "))

options = ["pierre", "papier", "ciseaux" ]
player_score = 0
computer_score = 0
player_choice = 0
computer_choice = 0

while winable_round != player_score or winable_round != computer_score:
    player_choice = (input("Que jouez vous ? Tapez 'pierre', 'papier' ou 'ciseaux' "))

    while player_choice not in options:
        player_choice = (input("Vous devez jouer 'pierre' ou 'papier' ou 'ciseaux' (sans les guillemets) : "))
        print (player_choice)

    computer_choice = random.choice(options)

    if player_choice == computer_choice:
        print("Egalité")

    elif player_choice == "pierre" and computer_choice == "ciseaux" \
    or player_choice == "papier" and computer_choice == "pierre" \
    or player_choice == "ciseaux" and computer_choice == "papier" :
        
        player_score = player_score + 1
        print(f"Vous avez battu l'ordinateur : {computer_choice} en jouant : {player_choice}")
        print(f"Le score est de :  Joueur : {player_score} | ordinateur : {computer_score}")
        
        if player_score == winable_round:
            print(f"Vous avez gagné : {player_score} à {computer_score}")
            break
    else:
        computer_score = computer_score + 1
        print(f"L'ordinateur, vous : {computer_choice} a battu en jouant : {computer_choice} ! ")
        print(f"Le score est de :  Joueur : {player_score} | ordinateur : {computer_score}")
        
        if computer_score == winable_round:
            print(f"Vous avez perdu : {computer_score} à {player_score}")
            break