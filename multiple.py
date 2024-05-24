# Dans cet exercice, vous devez afficher la table de multiplication d'un nombre.
# Dans ce cas-ci votre script doit afficher la table de multiplication d'un nombre 7:
# 0 * 7 = 0
# 1 * 7 = 7
# 2 * 7 = 14
# 3 * 7 = 21
# 4 * 7 = 28
# 5 * 7 = 35
# 6 * 7 = 42
# 7 * 7 = 49
# 8 * 7 = 56
# 9 * 7 = 63
# 10 * 7 = 70

nombre = 7
a = 0
while a <= 10:
    resultat = nombre * a
    print("{} * {} = {}". format(a,nombre, resultat))
    a += 1
