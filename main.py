



import datetime
print("Bonjour")
nom_1=input("Quel est ton nom ?")
date_1=int(input("En quelle année est-tu né ?"))
nom_2=input("Quel est le nom de ton/ta voisin(e) ?")
date_2=int(input("En quelle année est né ton voisin ?"))

now=datetime.datetime.now()
now_year=now.year
age1=(now_year-date_1)
age2=(now_year-date_2)



print(nom_1,"a",int(age1))
print(nom_2,"a",int(age2))

if age1>age2:
  print(nom_1,"est plus grand que",nom_2)
  diff_age2=(age1-age2)
  print("La différence d'age est de",diff_age2)

elif age1==age2:
  print(nom_1,"et",nom_2,"ont le meme age")

elif age2>age1:
  print(nom_2,"est plus age que",nom_1)
  diff_age1=(age2-age1)
  print("La différence d'age est de",diff_age1)

else:
  print("une situation inantendue a été rencontré")









import datetime

print("Bonjour")
nom_1=input("Quel est ton nom ?")
annee1=input("En quelle année est-tu né ?")
annee1=int(annee1)
nom_2=input("Quel est le nom de ton/ta voisin(e) ?")
annee2=input("En quelle année ton voisin est né ?")
annee2=int(annee2)


now=datetime.datetime.now()
now_year=now.year
age1=now_year-annee1
age2=now_year-annee2
diff_age1=(age2-age1)
diff_age2=(age1-age2)
print(nom_1,"a",age1)
print(nom_2,"a",age2)

if age1>age2:
  print(nom_1,"est plus grand que",nom_2)
  print("la différence d'age est de",diff_age2)


elif age1==age2:
  print(nom_1,"et",nom_2,"ont le meme age")


elif age2>age1:
  print(nom_2,"est plus grand que",nom_1)
  print("la différence d'age est de",diff_age1)

else:
  print("Une situation innatendue a été rencontrée.")


