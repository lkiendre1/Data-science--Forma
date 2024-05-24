#Ecrivez un programme qui affiche une table de conversion de sommes d'argents exprimées
#en euros, en dollars canadiens. La progression de sommes de la table sera "géométrique",
#comme dans l'exemple ci-dessous:

montant_euros = 1
while True:
    montant_dollars = montant_euros * 1.65
    print("{} euro(s) = {:.2f} dollar(s)".format(montant_euros, montant_dollars))
    montant_euros *= 2  # Multiplication par 2 pour la progression géométrique
    continuer = input("Souhaitez-vous continuer à convertir ? o/n : ")
    if continuer != "o":
        print("Merci !")
        break

     
       
