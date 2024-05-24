'''Dans cet exercice vous devez afficher les lettres du mot 'Python' dans le sens inverse. Votre script devra donc afficher :

n
o
h
t
y
P'''
programme = "Python"
inves = programme[::-1] # recupere tout les elements la variable programme en commencant par la fin
for i in inves : # ensuite une boucle pour afficher chaque element 
    print(i)