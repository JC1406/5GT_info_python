print("Bonjour, bienvenue dans ce programme de multiplication.")

question1=input("De quelle nombre voulez-vous connaître la table de multiplication ?")
question1=int(question1)

for i in range(11):
  print(i,"x",question1,"=",question1*i)
