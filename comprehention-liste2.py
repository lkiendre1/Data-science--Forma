# Dans cet exercice, nous avons une liste qui contient 50 nombres
# Le but de cet exercice est de rÃ©cupÃ©rer dans la liste nombres_pairs, uniquement les nombres pairs de la premiÃ¨re liste

nombres = range(51)
nombres_pairs = [i for i in nombres if i % 2 == 0]
print(nombres_pairs)