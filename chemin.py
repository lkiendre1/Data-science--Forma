from pathlib import Path
repertoire = Path.home()
'''for f in repertoire.iterdir():# boucle qui permet de recuperer tout les fichiers 
    print(f.name)# contenue dans le dossier utilisateur
'''
'''dossier = [d for d in repertoire.iterdir() if d.is_dir()]# permet de lister tot les sous repertoires du repertoir
print(dossier)'''
# -------- pour scanner un dossier
# ici on utilise la methode glob 
for f in repertoire.glob("*.png"): # permet de recuperer tout les fichiers dont les extensions se terminent par png  
    print(f.name)




