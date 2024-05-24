
# Comment peut-on permettre Ã  l'utilisateur de sortir de la boucle
# en modifiant les lignes de code dans la boucle while ?

while True:  # Utilisation d'une boucle infinie
    continuer = input("Voulez-vous continuer ? o/n ")
    if continuer != "o":  # Si l'utilisateur ne veut pas continuer
        break  # Sort de la boucle
    print("On continue !")

   