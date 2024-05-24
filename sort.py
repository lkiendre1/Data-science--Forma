# Le but de cet exercice est de remettre en ordre alphabÃ©tique les prÃ©noms prÃ©sents dans la chaÃ®ne de caractÃ¨res
# Vous devez crÃ©er une variable chaine_en_ordre qui, Ã  la fin de l'exercice doit contenir la chaÃ®ne de caractÃ¨re suivante:
# "Anne, Julien, Lucien, Marie, Pierre"
# N'hÃ©sitez pas Ã  faire des recherches et Ã  utiliser certaines des fonctions vues dans ce chapitre 

chaine = "Pierre, Julien, Anne, Marie, Lucien"
chaine_en_ordre = ", ".join(sorted(chaine.split(", ")))

print(chaine_en_ordre)


