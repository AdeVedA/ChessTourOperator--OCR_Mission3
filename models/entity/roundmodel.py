import datetime

class Round:

    def __init__(self, name, round_number, matches=[]):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.matches = matches if matches else []
        
        '''sauvegarde du round au propre dans le json avec résultat None = pas joué
        affichage des matchs au propre (UtilsView...)
        affichage menu d'input des résultats avec (1,2,0) (UtilsV)
        enregistrement résultats
        calcul des points
        nouveau round ?:
        appairement des joueurs selon points + requête "déjà joué"/sauvegarde
        affichage des matchs
        nouveau round ? ou fin :
        si fin de tournoi, affichage du classement/points des joueurs
        revoir les rapports
        flake8...
        readme...
        powerp
        '''

