nombres = input("Saisissez une liste de nombres séparés par des virgules: ")

# print (nombres)

liste = nombres.split(",")
print("Liste des nombres:", liste)

liste_entiers = []
for nombre in liste:
    nombre_entier = int(nombre)
    liste_entiers.append(nombre_entier)

somme = 0
for nombre in liste_entiers:
    somme += nombre
    
print("Somme des nombres:", somme)


moyenne = 0
for nombre in liste_entiers:
    moyenne += nombre / len(liste_entiers)
    
print("Moyenne des nombres:", moyenne)


nombre_au_dessus_moyenne = 0
for nombre in liste_entiers:
    if nombre > moyenne:
        nombre_au_dessus_moyenne += 1
        
print("Nombre de nombres supérieurs à la moyenne:", nombre_au_dessus_moyenne)



input("Appuyez sur Entrée pour fermer...")