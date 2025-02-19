# Ecrivez votre code ici !
import operations

nombre1 = float(input("Nombre 1 : "))
nombre2 = float(input("Nombre 2 : "))

operator = int(input("Addition : 1 ou Multiplication : 2  : "))

print(f"nombre1 : {nombre1}")
# print(f"nombre2 : {nombre2}")
# print(f"Opérateur : {operator}")

# input("Appuyez sur entrée pour continuer")

if operator == 1:
    # print("toto1")
    addition = operations.addition(nombre1,nombre2)
    print (f"Le résultat de l'addition est : {addition}")
elif operator == 2:
    # print("toto2")
    multiplication = operations.multiplication(nombre1,nombre2)
    print (f"Le résultat de la multiplication est : {multiplication}")
else:
    # print("totoX")
    print ("Le choix est uniquement 1 ou 2")


input("Appuyez sur entrée pour fermer le script")