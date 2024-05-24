# Dans cet exercice, vous devez :
# Afficher la phrase mdp_trop_court en majuscule si la longueur du mot de passe entrÃ© est Ã©gale Ã  0.
# Afficher la phrase mdp_trop_court avec une majuscule sur la premiÃ¨re lettre si la longueur du mot de passe entrÃ© est plus petite que 8.
# Afficher la phrase "Votre mot de passe ne contient que des nombres." si le mot de passe entrÃ© ne contient que des nombres.
# Afficher la phrase "Inscription terminÃ©e." si le mot de passe est valide.

mdp_trop_court = "votre mot de passe est trop court."
mot_de_passe = input("Entrez votre mot de passe! : ")
if len(mot_de_passe) == 0 :
    print(mdp_trop_court.upper())
elif len(mot_de_passe) < 8 :
    print(mdp_trop_court.capitalize()) 
elif mot_de_passe.isdigit():
    print("votre mot de passe ne contient que des nombres")
else:
    print("inscription termineé")
