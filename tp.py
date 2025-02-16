#print('hello,world')
#import sys
#print(sys.version)
#exit
#if 5 > 2:
#print('five is greter thn tow')
'''x = 5
y = "jhon" 
print(x,y)'''
'''x = 4
x = 'sally'
print(x)'''
'''x=str('3')
y=int(3)
z=float(3)
print(x,y,z)
x = 5
y ="jhon"
print(type(x))
print(type(y))
x='jhon'
x="jhon"
print(type(x))
x,y,z = "orange","banana","cherry"
print(x,y,z)
x=y=z="oange"
print(x)
print(y)
print(z)
fruits=["apple","ornge","banana"]
x,y,z=fruits
print(x)
print(y)
print(z)
x = 'python is awesome'
print(x)
x="python"
y='is'
z="awesome"
print(x+y+z)
x=3
y=4
print(x+y)
x="yassine"
def myfunc():
 print("python is "+x)
myfunc()
x="yasiine"
def myfunc():
 x = "yaaaw"
 print("life is",x)
myfunc()
print("life is",x)
for i in range(1,10):
    print("bonjour tout le monde")
for i in range (1,51):
  print(i +  (i+1))
num=int(input('saisir le nombre:'))
for i in range(1,num):
    s=i+(i+1)
    print(s)'''

liste_noms = ['Imad', 'Ilham', 'Tarik', 'Ali', 'Souhaib', 'Karima']

# Fonction pour afficher la liste des noms
def afficher_liste():
    if len(liste_noms) == 0:
        print("La liste est vide.")
    else:
        print("Liste des noms :")
        for nom in liste_noms:
            print(nom)

# Fonction pour rechercher un nom dans la liste
def rechercher_nom():
    nom = input("Entrez le nom à rechercher : ")
    if nom in liste_noms:
        print(f"{nom} est dans la liste.")
    else:
        print(f"{nom} n'est pas dans la liste.")

# Fonction pour insérer un nouveau nom à la position donnée
def inserer_nom():
    nom = input("Entrez le nom à insérer : ")
    if nom in liste_noms:
        print(f"{nom} est déjà dans la liste.")
    else:
        try:
            position = int(input("Entrez la position où insérer le nom (index de 0 à n): "))
            if 0 <= position <= len(liste_noms):
                liste_noms.insert(position, nom)
                print(f"{nom} a été ajouté à la position {position}.")
            else:
                print("Position invalide. Elle doit être entre 0 et", len(liste_noms))
        except ValueError:
            print("Veuillez entrer un nombre entier valide pour la position.")

# Fonction pour supprimer un nom de la liste
def supprimer_nom():
    nom = input("Entrez le nom à supprimer : ")
    if nom in liste_noms:
        liste_noms.remove(nom)
        print(f"{nom} a été supprimé.")
    else:
        print(f"{nom} n'est pas dans la liste.")

# Fonction pour vider la liste
def vider_liste():
    liste_noms.clear()
    print("La liste a été vidée.")

# Fonction principale du menu
def menu():
    while True:
        print("\nVeuillez frapper une lettre : ")
        print("A : Afficher la liste des noms")
        print("R : Rechercher un nom dans la liste")
        print("I : Insérer un nouveau nom dans la liste")
        print("S : Supprimer un nom de la liste")
        print("V : Vider la liste")
        print("T : Terminer")
        
        choix = input("Choisissez une option : ").upper()
        
        if choix == 'A':
            afficher_liste()
        elif choix == 'R':
            rechercher_nom()
        elif choix == 'I':
            inserer_nom()
        elif choix == 'S':
            supprimer_nom()
        elif choix == 'V':
            vider_liste()
        elif choix == 'T':
            print("Fin du programme.")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

# Exécution du programme
menu()






