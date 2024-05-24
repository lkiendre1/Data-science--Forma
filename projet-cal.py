'''Dans ce projet, vous devez créer une calculatrice en ligne de commande qui demande 
à l'utilisateur de saisir deux nombres et qui affiche ensuite le résultat de l'addition 
de ces deux nombres. Vous devez également gérer le cas de figure dans lequel l'utilisateur
ne rentre pas de données valides.
Si l'utilisateur rentre une lettre, un symbole ou quoi que ce soit d'autre qu'un nombre, 
vous devrez lui demander de nouveau de saisir deux valeurs valides.'''
def calcul():
    while True :
        try:
            x = int(input("entrer un nombre : "))
            y = int(input("entrer un deuxième : "))
            z = x + y
            print(z) 
            break
        except ValueError:
            print("Erreur saisissez un nombre entier svp !")
calcul()


        


    


 
        
    

