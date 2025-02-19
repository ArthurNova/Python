# Ecrivez votre code ici !
nombre1 = input("Entrez un nombre : ")
nombre2 = input("Entrez un nombre : ")

print(nombre1)
print(nombre2)

if not nombre1.isnumeric() or not nombre2.isnumeric():
    print('Les deux nombres doivent être entiers')
    raise SystemExit("Fin du programme")
    
nombre1 = int(nombre1)
nombre2 = int(nombre2)

operator = input("Choisir un opérateur parmi '+','-','*' ou '/'")
# print(operator)
if not operator == "+" and not operator == "-" and not operator == "*" and not operator == "/":
    print("'L'opérateur doit être '+' ou '-' ou '*' ou '/'")
    raise SystemExit("Fin du programme")

if operator == "+":
    resultat = nombre1 + nombre2
    
elif operator == "-":
    resultat = nombre1 - nombre2
    
elif operator == "*":
    resultat = nombre1 * nombre2
    
elif operator == "/":

    if nombre2 == 0:
        print ("Impossible de diviser un nombre par 0")
        raise SystemExit("Fin du programme")
    
    resultat = round(nombre1 / nombre2, 2)

print(f"Le résultat de l'opération est: {round(resultat, 2)}")
input("Appuyez sur Entrée pour fermer...")
