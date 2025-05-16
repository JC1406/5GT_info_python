from math import pi

def menu():
  print("Bienvenue dans ce programme permettant de calculer l'air des")
  print("Pour un triangle tapez 1")
  print("Pour un carré tapez 2")
  print("Pour un carré tapez 3")
  print("Pour un cercle tapez 4")
  print("Pour quitter tapez 5")

  choix=input("Quel est votrer choix ?")
  choix=int(choix)

  if choix==1:
    triangle()
  elif choix==2:
    carre()

  elif choix==3:
    rectangle()

  elif choix==4:
    cercle()

  elif choix==5:
    quit()

  else:
    print("une erreur a été rencontrée.... Oups!")

def triangle():
  base=input("Que vaut la base ?")
  base=float(base)
  hauteur=input("Que vaut la hauteur ?")
  hauteur=float(hauteur)
  aire=base*hauteur/2
  print("L'air du triangle vaut",round(aire,3))
  menu()

def carre():
  cote=input("Que vaut le cote ?")
  cote=float(cote)
  aire=cote**2
  print("L'air du carre vaut",round(aire,3))
  menu()

def cercle():
  rayon=input("Que vaut le rayon?")
  rayon=float(rayon)
  aire=pi*rayon**2
  print("L'aire d'un cercle vaut :",round(aire,3))
  menu()

def quit():
  print("Au revoir")

if __name__=="__main__":
  menu()