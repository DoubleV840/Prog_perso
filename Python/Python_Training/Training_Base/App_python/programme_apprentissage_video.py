#VIDEO BRO CODE - PYTHON ON YOUTUBE

#Afficher des éléments
print() #Afficher des éléments

#Création d'une variable
string = "quelque chose" #Variable de type "str" 'string' (chaine de caractères)
entier = 24 #Variable de type "int" 'entier' (nombre entier)
float = 25.6 #Variable de type "float" 'float' (nombre décimal)
bool = True #Variable de type "bool" 'booleen' (True ou False)

#String méthodes
variable = "chaine"

len(variable) #Indique la longueur de la chaine
variable.find("a") #Indique la postion du caractère choisi
variable.capitalize() #Maj le premier caractère de la chaine
variable.upper() #Chaine en majuscule
variable.lower() #Chaine en minuscule
variable.isdigit() #True si la chaine est numérique, False sinon
variable.isalpha() #True si la chaine comporte que des lettres, False sinon
variable.count("a") #Combien il y a de caractère choisi, ici un seul 'a'
variable.replace("a", "o") #Remplace un caractère par un autre
variable*3 #Permet d'afficher la chaine plusieurs fois, ici 'chainechainechaine'

#Changement de type
x = 1
y = 2.0
z = "3"

y = int(y) #float to int, 2.0 to 2
z = int(z*3) #str to int, 333 to 9

x = float(x) #int to float, 1 to 1.0
z = float(z*3) #str to float, 333 to 9.0

x = str(x*3) #int to str, 1 to 111
y = str(y) #float to str, 2.0 to 2

#Entrer des elements
name = input("Quel est votre nom ?:") #Demande à l'utilisateur de saisir une valeur à l'execution du programme
name = int(input("Quel est votre nom ?:")) #Converti la valeur demandée en int
name = float(input("Quel est votre nom ?:")) #Converti la valeur demandée en float
name = str(input("Quel est votre nom ?:")) #Converti la valeur demandée en str

#Librairie 'math'
import math #Importer la library dans le code

pi = 3.14

round(pi) #Arrondi le nombre
math.ceil(pi) #Arrondi le nombre au dessus, ici 4
math.floor(pi) #Arrondi le nombre en dessous, ici 3
abs(pi) #Valeur absolue d'un nombre
pow(pi, 2) #Puissance d'un nombre, ici pi^2
math.sqrt(pi) #Racine d'un nombre
max() #Trouve le nombre maximum entre plusieurs variables
min() #Trouve le nombre minimum entre plusieurs variables

#Séparation d'un string --> indexing[start(inclu):stop(exclu):step]
name = "William Berger"

prenom = name[:7] #[0:7] #Ici on recupère 'William', start à W stop à ' '
nom = name[8:] #[8:end] #Ici on recupère 'Berger', start à B stop à la fin de la chaine
step_name = name[0:15:2] #[0:end:2] #Ici on affiche un caractère sur 2
resversed_name = name[::-1] #[0:end:-1] #Ici on affiche tout les caractères avec un pas de -1 soit inversés

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

#Try/Except --> use to not intterupt the flow of a program
result = 0
numerator = 1
denominator = 0
try:
      result = numerator / denominator
      print(result)
except ZeroDivisionError: #Si l'utilisateur essaie de diviser par zéro, une exception ZeroDivisionError  sera levée, 
                            #et le programme exécutera le bloc except  pour gérer cette erreur et afficher un message approprié.
    print("Erreur : division par zéro")
except ValueError: #Si l'utilisateur entre une autre valeur qu'un nombre
    print("Only number pls")
except Exception: #Dans les cas exetpionnel
    print("Something went wrong")
else:
    print(result)
finally: #Pour que le programme effectue tjs quelque chose
    print("Ceci s'affichera tjs")

#BOUCLES FOR / WHILE

#For, range[start(inclu),stop(exclu),step]
plateformes_sociales = ["Insta", "Facebook", "Twitter"]

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

#Control de boucles

#break : Termine une boucle instantanement
#continue : skip le prochain caratère d'une chaine
#pass : ne fais rien en particulier, remplace juste quelque chose

#Listes --> plusieurs éléments pour une seule variable

food = ["pizza", "pasta", "pain"]
food[0] =  "pizza"

drinks = ["café", "soda", "thé"]
dinner = ["pizza", "pates", "jambon"]

nourriture = [drinks, dinner]
nourriture[1][2] #nourriture[dinner][jambon]

food.append("glace") #Ajoute l'élément 'glace'
food.remove("pizza") #Supprime l'élément 'pizza'
food.pop() #Supprime le dernier élément
food.insert(0, "bonbon") #Ajoute 'bonbon' à la place [0]
food.sort() #Ordre alphabétique
food.clear() #Supprime tout les éléments de la liste

#Tuples (similaire aux listes) --> plusieurs éléments en une seule variable mais inchangeable et ordonné

student = ("William", 22, "garcon")

student.count("william") #Renvoie 1 car il y a qu'une fois 'William'
student.index("garcon") #Renvoie 2 car c'est le troisième index

#set --> désordonné et non-indexé et non les index ne sont pas duplicables

ustensils = {"fourchette", "couteau", "cuillière"}
dishes = {"bol", "assiette", "couteau"}

ustensils.add("verre") #Ajoute un element dans le set
ustensils.remove("fourchette") #Supprime un élément du set
ustensils.clear() #Supprime tout les éléments du set
ustensils.update(dishes) #Ajoute les élément de 'dishes' dans 'ustensils'
ustensils.difference(dishes) #Renvoie les éléments différents entre les 2 set
ustensils.intersection(dishes) #Renvoie les éléments identiques entre les 2 set

#Dictionnaires

pays = {"France": "Paris",
        "USA": "Washington DC",
        "Chine": "Pékin",
        "Russie": "Moscou"}
        
pays["France"] #Renvoie 'Paris'

pays.get() #Récupère la valeur associée à une clé spécifique. Indique aussi si l'élément existe ou non dans le dico
pays.keys() #Affiche juste les clés (ici capitales)
pays.values() #Affiche juste les valeurs (ici pays)
pays.items() #Correspond à tout les elements du dico
pays.update({"Allemagne":"Berlin"}) #Ajoute ou modifie un élément au dico
pays.pop() #Supprime un element du dico
pays.clear() #Supprime tout les elements du dico

#Fonctions --> block de code qui s'execute quand on l'appelle

def nom_fonctions(): #Déclaration de la fonction
    pass
    
nom_fonctions() #Appel de la fonction

def nom_fonction2(name): #Déclaration de la fonction avec une variable en argument
    print("Hello ", name)
    
nom_fonction2("William") #Appel de la fonction avec un str en argument

#Mots clé arguments

def nom_fonction3(first, middle, last): #Déclaration de la fonction
    print("hello", first, middle, last)
    
nom_fonction3("William", "Berger", "jsp") #Appel de la fonction classique
nom_fonction3(last="William", first="Berger", middle="jsp") #Appel de la fonction avec des mots clés pour definir l'odre des arguments

# *args --> paramètre qui vient remplacer tout les arguments dans un tuple

def add(*args): #Définition de la fonction avec un nombre d'argument indéfini (le nom importe peu tant que l'on met '*' devant)
    sum = 0
    for i in args:
        sum += i
    return sum

add(1, 2, 3, 4) #Ici appel de la fonction, on envoie 4 arguments. La fonction s'adapte automatiquement

# **kwargs  --> paramètre qui vient remplacer tout les arguments dans un dictionnaire

def nom_fontion4(**kwargs): #Définition de la fonction avec un nombre d'arguments (clé, valeur) indéfini
    print("Hello", end=" ")
    for keys, values in kwargs.items():
        print(values, end=" ")

nom_fontion4(title= "Mr.", first= "William", last= "Berger") #Appel de la fonction. On envoie 3 arguments (clé , valeur), la fonction s'adapte automatiquement
nom_fontion4 = {"title": "Mr.", #Ce dictionnaire est la traduction litérale de la fonction au dessus
                "first": "William",
                "last": "Berger"}

#str_format 

animal = "cow"
item = "moon"

print("The {} jumped over the {}".format(animal, item)) #Entre accolade on retrouve les variables à l'execution
print("The {0} jumped over the {1}".format(animal, item)) #Ici {0} = animal, {1} = item
print("The {1} jumped over the {0}".format(animal, item)) #Ici {0} = animal, {1} = item mais dans un ordre inversé
print("The {animal} jumped over the {item}".format(animal= "cow", item= "moon")) #Ici on a "déclaré" les variables directement dans la fontion

name = "William"

print("Hello ton nom est {}".format(name)) #On retrouve la variable 'nom' entre accolade
print("Hello ton nom est {:10}".format(name)) #Rajoute 10 espaces de caractère a str(name)
print("Hello ton nom est {:<10}".format(name)) #Rajoute 10 espaces de caractère a str(name) et place la variable au début de la chaine
print("Hello ton nom est {:>10}".format(name)) #Rajoute 10 espaces de caractère a str(name) et place la variable à la fin de la chaine
print("Hello ton nom est {:^10}".format(name)) #Rajoute 10 espaces de caractère a str(name) et place la variable au centre de la chaine

nombre= 3.14
nombre2 = 1000

print("Le nombre est {:.2f}".format(nombre)) #Nombre 2 chiffres après la vigule
print("Le nombre est {:,}".format(nombre2)) #Ajoute une virgule, ici 1,000
print("Le nombre est {:b}".format(nombre2)) #Transforme le nombre en binaire
print("Le nombre est {:o}".format(nombre2)) #Transforme le nombre en base 8
print("Le nombre est {:x}".format(nombre2)) #transforme le nombre en hexadecimal
print("Le nombre est {:e}".format(nombre2)) #Transforme le nombre en notation scientifique

#Librairie random
import random

random.rand(1, 6) #Génère un nombre aléatoire, ici entre 1 et 6
random.random() #Génere un nombre entre 0 et 1

random_list = ["Pierre", "Papier", "Sciseau"]

random.choice(random_list) #Fait un choix aléatoire entre les elements d'une liste

cards = ["As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "V", "D", "R"]

random.shuffle(cards) #Renvoie un mélange aléatoire des elements dans une liste

#Librairie os ---> Conseillé d'utiliser try/except pour assurer la continuité du program
import os

chemin = "/Users/william/Desktop/Programmation/Python/Python_Training/Training_Base/fichier_test.txt"

os.path.exists(chemin) #Permet de savoir si un élément existe quelque part
os.path.isfile(chemin) #Permet de savoir si c'est uin fichier
os.path.isdir(chemin) #Permet de savoir si c'est un dossier
os.replace() #source, destination #Permet de changer la place d'un fichier
os.remove(chemin) #Supprime un fichier
os.rmdir(chemin) #Supprime un dossier

#Ouvrir, fermer, modifier un fichier
with open("fichier_test.txt", "a") as file: #"a" = ajouter du texte, "w" = écrire un nouveau texte et supprimer l'ancien
    file.read() #Lis le fichier
    file.write("Nouveau texte dedans\nWesh\ton est la")
    file.close() #Ferme le fichier (Renvoie True si le fichier est fermé)
    
try:
    with open("fichier_test.txt") as onmetcequonveut:
        print(onmetcequonveut.read())
except FileNotFoundError: #Exception si le fichier ne peut pas s'ouvrir
    print("File not found")
    
#Librairie shutil ---> Copier des fichiers
import shutil

shutil.copyfile() #source, destination #Copie un fichier
shutil.copy() #source, destination #copyfile() + permission mode + destination peut etre un dossier
shutil.copy2() #copy() + file's creation and modification times
shutil.rmtree(chemin) #Supprime un dossier avec des fichiers dedans

#Modules --> permet de séparer un code en plusieurs sous programme

#Après la création d'un nouveau fichier .py on peut l'importer dans le programme principal
#Importation de fichier
import fichier_test #Importe un fichier .py
import fichier_test as test #Permet de donner un surnom à son fichier pour simplier les appels de fonction
from fichier_test import fonction1, fonction2 #Importe un ou plusieurs élements en particulier
from fichier_test import * #Importe toutes les éléments d'un fichier
#Appel de fonctionn incluse dans le fichier importé
fichier_test.fonction1() #Appel d'elements depuis un fichier externe
test.fonction1() #Appel d'élément depuis un fichier externe mais en utilisant un surnom
fonction1() #Appel d'élément grace à l'importation d'un element en particulier
fonction2() #Appel d'élément grace à l'importation d'un element en particulier

#class --> bloc de code qui définit les propriétés et les comportements d'un objet
#A refaire plus propre (difficile à comprendre)
class NomDeLaClasse: #Le nom commence par une majuscule conventionnellement
    # Définition des attributs de classe
    def __init__(self):
        pass
    # Définition des méthodes de classe
    def avancer():
        pass
    def freiner():
        pass

#Exemple de classe
class Car:  #Le nom commence par une majuscule conventionnellement

    # Définition des attributs de classe
    def __init__(self,make,model,year,color): #__init__ est une méthode de constructeur qui permet d'initialiser les attributs d'une instance
    #self --> je définis 'self' comme une variable qui fait la transition entre plusieurs éléments
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    # Définition des méthodes de classe
    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")

class Truck(Car): #Sous-classe de la classe 'Car'            #Une sous-classe herite des attributs de la classe principale et peut aussi avoir des attributs distaincts
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year, color) #Appel de la méthode d'initialisation de la classe parente pour initialiser les attributs hérités (pour eviter de se repeter)

#Il est possible de créer un sous-sous-classe et à les meme caractéristiques qu'une sous-classe (Grands parents, parents, enfants)
#Il est possible de créer une sous classe avec plus d'un parents

#from car import Car #Doit etre dans un autre fichier .py

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

car_1.drive()
car_2.stop()

#walrus operator --> := -> utile dans les situations où l'on souhaite assigner une valeur à une variable 
                            #en se basant sur une condition sans avoir à évaluer deux fois la même expression.
                            #Il est souvent utilisé pour simplifier le code et améliorer sa lisibilité.
#Exemple 1
happy = True
print(happy)
#Permet d'ecrire plutot ça:
print(happy := True)

#Exemple 2
foods = list()
while True:
    food = input("Quel nourriture veut tu ajouter a la liste ?")
    if food == "quit":
        break
    foods.append(food)
#Permet d'ecrire plutot ça:
foods = list()
while food := input("Quel nourriture veut tu ajouter a la liste ?") != "quit":
    foods.append(food)

#Adresser un fonction à une variable
say = print #Ici on assigne la fonction print à la variable say

say("Salut") #Ici on utilise 'say' comme la fonction 'print'

#Mettre une fonction en argument
def loud(text): #Ici création d'une fonction 
    return text.upper()

def hello(fonction):
    text = fonction("Hello") #Création d'une pseudo fonction 
    print(text)
    
hello(loud) #Appel de la fonction 'hello' avec la fonction 'loud' en argument

#Fonction lambda --> permet d'etre un racourci

double = lambda x : x*2
print(double(5))
multiply = lambda x, y: x*y
print(multiply(4,3))
addition = lambda x, y, z : x+y+z
print(addition(1,2,3))
full_name = lambda prenom, nom: f"{prenom} {nom}"
print(full_name("William", "Berger"))
age_check = lambda age: True if age >= 18 else False
print(age_check(19))

#Fonction sort() méthodes

student = ["William","Damien","Cyriaque","Delphine"] 
student2 = ("William","Damien","Cyriaque","Delphine")

student.sort() #Trie par ordre alphabétique
student.sort(reverse=True) #Trie par ordre alphabétique inversé (fonctionne pas avec les tuples)
nom_variable = sorted(student2) #Ici fonctionne avec les tuples

tuple_liste = [("William", "F", 60),
               ("Damien", "A", 33),
               ("Cyriaque", "D", 36)]

grade = lambda grades: grades[1] #[0] = 1ère colonne, [1] = 2ème ", [2] = 3ème "
tuple_liste.sort(key=grade) #Trie le tuple_liste en fonction de la deuxième colonne

age = lambda ages: ages[2]
tuple_liste.sort(key=age, reverse=True) #Trie le tuple_liste en fonction de la troisième colonne + inverse l'ordre

tuple_tuple = (("William", "F", 60),
               ("Damien", "A", 33),
               ("Cyriaque", "D", 36))

age = lambda ages: ages[2]
nom_variable = sorted(tuple_tuple, key=age) #Trie un tuple de tuple

#Fonction map()

store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_euros = lambda data: (data[0],data[1]*0.82) #Converti dollars en euros
#to_dollars = lambda data: (data[0],data[1]/0.82)

store_euros = list(map(to_euros, store)) #Creer une liste de 'store' avec la convertion en euro

#Fonction filter()

friends = [("Rachel",19),
           ("Monica",18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross",20)]

age = lambda data:data[1] >= 18 #Filtre les ages superieurs a 18, [1] = 2 ème colonne

drinking_buddies = list(filter(age, friends))

#Librairie reduce()
import functools

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x, y,:x * y,factorial) #Calcul factoriel des deux premier élément de la liste et repete pour le reste
print(result)

#Librairie zip() --> Permet de créer un objet zip 

zip() #Permet de regrouper plusieurs itérables (liste, tuples...) #1ère colonne ensemble puis 2ème colonne etc

#Librairie time() --> Permet de gérer le temps en général dans un programme
import time

time.ctime() #Renvoie la date et l'heure actuelle
time.time() #Permet de caculer le temps d'execution pour un evenement dans le code
time.localtime() #Renvoie les infos temporelle actuelles mais il est possible d'en utiliser qu'une partie (Heure, année...)
time.sleep() #Suspend l'exécution du programme pendant un nombre spécifié de secondes.

#Librairie Threading --> Permet de gérer l'execution de plusieurs evenements en fonction du temps
import threading

threading.Thread() #Classe permettant de créer et de manipuler des threads. Elle prend en argument la fonction cible (target) à exécuter dans le thread et les arguments (args) à passer à cette fonction.
threading.start() #Méthode de la classe Thread qui démarre l'exécution du thread.
threading.join() #Méthode de la classe Thread qui attend que le thread se termine.
threading.is_alive() #Méthode de la classe Thread qui vérifie si le thread est en cours d'exécution.
threading.Lock() #Classe de verrouillage pour la synchronisation entre threads.
threading.Event() #Classe d'événement pour la synchronisation entre threads.
threading.Semaphore() #Classe de sémaphore pour la gestion des ressources partagées entre threads.
threading.Timer() #Classe permettant de créer un thread qui exécute une fonction après un délai spécifié.
threading.current_thread() #Fonction qui renvoie l'objet Thread représentant le thread actuel.
threading.active_count() #Fonction qui renvoie le nombre total de threads en cours d'exécution.
threading.enumerate() #Fonction qui renvoie une liste de tous les threads en cours d'exécution.

#Librairie multiprocessing -->  permet de créer, gérer et communiquer entre des processus dans vos programmes Python, vous permettant ainsi de tirer parti du parallélisme pour accélérer l'exécution de tâches intensives en calcul.
import multiprocessing

multiprocessing.start() #Méthode de la classe Process qui démarre l'exécution du processus.
multiprocessing.Process() #Classe permettant de créer et de manipuler des processus. Elle prend en argument la fonction cible (target) à exécuter dans le processus et les arguments (args) à passer à cette fonction.
multiprocessing.join() #Méthode de la classe Process qui attend que le processus se termine.
multiprocessing.is_alive() #Méthode de la classe Process qui vérifie si le processus est en cours d'exécution.
multiprocessing.Queue() #Classe de file d'attente pour le partage de données entre processus.
multiprocessing.Pipe() #Classe de tube pour la communication bidirectionnelle entre processus.
multiprocessing.Lock() #Classe de verrouillage pour la synchronisation entre processus.
multiprocessing.Manager() #Classe de gestionnaire pour la création et la manipulation de données partagées entre processus.
multiprocessing.current_process() #Fonction qui renvoie l'objet Process représentant le processus actuel.
multiprocessing.active_children() #Fonction qui renvoie une liste de tous les processus enfants en cours d'exécution.

#GUI (fenêtre) Windows avec tkinter --> Tkinter fournit un ensemble de widgets (éléments d'interface utilisateur tels que boutons, zones de texte, menus, etc.) et des outils pour créer des fenêtres, des boîtes de dialogue et des mises en page graphiques.

from tkinter import *

window = Tk() #Créer une instance de la fenêtre principale

    #Contenu de la fenêtre
window.geometry("1440x900") #Taille de la fenêtre
window.title("Première fenêtre - App Python") #Titre de la fenêtre

icon = PhotoImage(file="nomdufichier.png") #Choix de l'icone de la fenetre
window.iconphoto(True, icon) #Lien de l'icone avec la fenetre

window.config(background="#00CC00") #Couleur de fond de la fenetre (possible d'ajouter une couleur en hexa)

    #Label --> outil qui permet d'ajouter du texte ou une image dans la fenetre
photo_label = PhotoImage(file="image.png") #Crée un objet PhotoImage à partir du fichier "image.png". Cette image sera utilisée plus tard dans le widget Label.

#Crée un widget Label dans la fenêtre spécifiée par la variable "window".
label = Label(window, 
              text="Hello World", 
              font=("Times New Roman",30,"bold"), 
              fg="blue", 
              bg="#00CC00",
              relief=RAISED,
              bd=10,
              padx=20, pady=20,
              image=photo_label,
              compound="top")
# - Le texte du label est défini sur "Hello World".
# - La police du texte est définie sur "Times New Roman" avec une taille de 30 et en gras.
# - La couleur du texte est définie sur "bleu".
# - La couleur d'arrière-plan du label est définie sur "#00CC00" (vert clair).
# - Le relief du label est défini sur "RAISED" (surélevé).
# - La taille de la bordure du label est définie sur 10 pixels.
# - Les marges internes (padding) du label sont définies sur 20 pixels.
# - L'image du label est définie sur l'objet PhotoImage "photo_label".
# - L'alignement de l'image et du texte dans le label est défini sur "top" (image en haut, texte en bas).

#label.pack() #Place le widget Label dans la fenêtre en utilisant la méthode pack(). Cette méthode ajuste automatiquement la position du widget.
#label.place(x= 0, y=0) #Place précisément le widget Label aux coordonnées (x=0, y=0) dans la fenêtre.

    #Boutton --> Fais quelque chose a l'appuie de celui ci
compteur = 0

def click():
    global compteur
    compteur += 1
    print(compteur)

button = Button(window,
                text= "Cliquez ici",
                command=click,
                font=("Comic Sans", 30),
                fg="yellow",
                bg="red",
                activeforeground="rose",
                activebackground="green",
                state=ACTIVE,
                )
button.pack()

    #entry --> crée zone de texte
    
entry = Entry(window,
              font=("Arial",20),
              show="*") #Permet d'entrer un mot de style mot de passe (Remplace tout les caractères par *)
entry.pack(side=LEFT) #Met le texte sur le coté gauche

    #Checkbutton --> Boutton cochable
    
def display():
    if x.get() == 1:
        print("You agree")
    else:
        print("You don't agree")
 
x = IntVar() #Crée une variable entieère pour stocker des entier (fonctionne aussi avec StringVar pour stocker des chaines)      
Checkbutton(window,
            text="I agree",
            variable=x,
            onvalue=1, #Valeur donnée à la case quand elle est cochée
            offvalue=0, #Valeur donnée à la case quand elle est non cochée
            command=display)
Checkbutton.pack()

    #Radio button (Bouttons a choix mutiples)

food = ["Pizza", "Hamburger", "Hotdog"]
x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window, 
                              text=food[index], #Ajoute du texte pour chaque buttons
                              variable=x, 
                              value=index) #Assigne différentes valeurs aux bouttons
    
    radiobutton.pack(anchor=W) #anchor -> aligner le tout

window.mainloop() #Lancer la boucle principale de l'application

