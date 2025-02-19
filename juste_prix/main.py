import random

nombre_aleatoire = random.randint(0, 10)
print (nombre_aleatoire)

choix = int(input("Choisir un nombre entre 0 et 10 : "))
tentatives = 1

while choix != nombre_aleatoire:

    if choix > nombre_aleatoire:
        print ("C'est moins")
        choix = int(input("Choisir un nombre entre 0 et 10 : "))
        tentatives = tentatives + 1 

    elif choix < nombre_aleatoire:
        print ("C'est plus")
        choix = int(input("Choisir un nombre entre 0 et 10 : "))
        tentatives = tentatives + 1 

else:
    score = int(100/ tentatives)
    print (f"Félicitations vous avez trouvé le prix : {nombre_aleatoire} en {tentatives} tentatives(s), votre score est de : {score} sur 100 !")