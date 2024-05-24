# Le but de cet exercice est de modifier le script afin d'afficher l'index de chaque lettre du mot 'Python'
# Pour l'instant, le script retourne une erreur. A vous de le corriger
# Votre script doit donc afficher:
#0
#1
#2
#3
#4
#5

mot = "Python"
for i in mot:
    b = mot.index(i)
    print(b)