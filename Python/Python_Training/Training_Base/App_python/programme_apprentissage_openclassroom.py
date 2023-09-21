                                             #PROGRAMME D'APPRENTISSAGE PYTHON (OPENCLASSROOM)


#DECLARER DES VARIABLES

#Déclarer une variable (chaine de caractère)
chaine_de_caractere = "Les dents de la mer"
#Déclarer une variable (entier, decimale)
nombre_int = 35; nombre_float = 3.14
#Déclarer une variable (chaine de caractère)
variable_booleenne = True

#AFFICHER ET ENTRER DES ELEMENTS

#Afficher une variable
print(chaine_de_caractere,chaine_de_caractere[4], nombre_int, nombre_float, variable_booleenne)
#ENTREZ UN ELEMENT
Entrez_nombre = input("Entrez un nombre : ")
print(f"Votre nombre est {Entrez_nombre}") #Afficher une variable ou on veut
print("Votre nombre est ", Entrez_nombre) #Seulement pour afficher la variable à la suite du texte


#DECLARER UNE LISTE/TUPLE ET LA MODIFIER (Pour plus de méthode de liste voir bible)

#Déclarer une liste
plateformes_sociales = ["ZFacebook", "Instagram", "Snapchat", "Twitter"]
#Afficher un élément de la liste
print(plateformes_sociales[1], plateformes_sociales[-1])
#Ajouter un élément à la liste
plateformes_sociales.append("TikTok")
print(plateformes_sociales)
#Supprimer un élément de la liste
plateformes_sociales.remove("Twitter")
print(plateformes_sociales)
#Afficher la longueur de la liste
print(len(plateformes_sociales))
#Trier la liste par ordre alphabétique
plateformes_sociales.sort()
print(plateformes_sociales)
#Déclarer un tuple (comme une liste mais non modifiable)
plateformes_sociales_tuple = ("Facebook", "Instagram", "TikTok", "Twitter")
print(plateformes_sociales_tuple)

#DECLARER UN DICTIONNAIRE ET LE MODIFIER

#Premiere manière de faire
new_dico_entreprise = {
    "PDG" : "William BERGER",
    "Directeur marketing" : "Francois Dupont",
    "RH" : "LEA CALEMBOUR",
    "Clients_importants": ["Jambon Beurre", "Tartine de nut"]
}
print(new_dico_entreprise)
print(new_dico_entreprise["Directeur marketing"])
#Deuxième manière de faire
dico_jsp = {}
dico_jsp["test"] = "Wesh canne a peche"
dico_jsp["pi"] = 3.14
print(dico_jsp["test"])
print(dico_jsp["pi"])
#Supprimer un élément du dictionnaire
del(new_dico_entreprise["Clients_importants"])
new_dico_entreprise.pop("RH")
print(new_dico_entreprise)
#Verifier l'existance d'un element
print("PDG" in new_dico_entreprise)
print("CHAT" in dico_jsp)

#CONDITIONS IF/ELSE/ELIF TRY/EXCEPT

ensoleille = False
neige = True

if ensoleille:
   print("on va à la plage !")
elif neige:
   print("on fait un bonhomme de neige")
else:
   print("on reste à la maison !")

#Avec opérateurs logiques -> && devient and / || devient or / ! devient not
avec_soleil = True
en_semaine = False

if avec_soleil and not en_semaine:
   print("on va à la plage !")
elif avec_soleil and en_semaine:
   print("on va au travail !")
else:
   print("on reste à la maison !")
   
#Avec les expressions comparatives (idem qu'en C ---> == / >= / <= / < / > / !=)
nombre_de_sieges = 30
nombre_dinvites = 25

if nombre_dinvites < nombre_de_sieges:
   print("On peut mettre plus d'invités")
else: 
   print("Pas plus d'invités")

#Try/Except
result = 0
numerator = 1
denominator = 0
try:
      result = numerator / denominator
      print(result)
except ZeroDivisionError:
        print("Erreur : division par zéro")
"""Si l'utilisateur essaie de diviser par zéro, une exception ZeroDivisionError  sera levée, 
et le programme exécutera le bloc except  pour gérer cette erreur et afficher un message approprié."""

#BOUCLES FOR / WHILE

#For
for test in plateformes_sociales:
    print(test)
    
for test2 in range(10):
    print(test2+1)

for x in range(10):
    print(f"Salut {x+1} fois")

for y in range(5, 11):
    print(f"{y}")

#While
nombre_start = 10
nombre_final = 50

while nombre_start < nombre_final:
    nombre_start += 1
print(nombre_start)
while nombre_start != nombre_final:
    nombre_start += 1
print(nombre_start)


#FONCTIONS

def add(a, b):
   return a + b
   
print(add(100, 20))

def somme(nombres):
   total = 0
   for somme in nombres:
      total += somme
   return total

nombres = [9,3]
print(somme(nombres))

def message():
   print("Salut")

message()


#MATCH/CASE ---> Comme switch/case

"""match choix:
    case '1':
        result = addition(num1, num2)
    case '2':
        result = soustraction(num1, num2)
    case '3':
        result = multiplication(num1, num2)
    case '4':
        result = division(num1, num2)
    case _:
        print("Choix invalide.")"""
        


age = 21
age += 1
nom = "will"
print("Ton age est :", age, nom)