from models.manager.playermanager import PlayerCrud

class Round:

    def __init__(self, name, start_date, end_date=None, matches=[]):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.matches = matches if matches else []
    
    def __str__(self):
        return f'le tournoi "{self.name}", commencé le {self.start_date}, {self.end_date if self.end_date != None else None}, {self.matches}'

    def __repr__(self):
        return f"{self.name}, {self.start_date}, {self.end_date}, {self.matches}"

    def to_json(self):
        """convertit un objet round en dictionnaire serialisable
        """
        _round = {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "matches": []
        }
        for _match in self.matches:
            _round['matches'].append(_match.to_json())
        return _round

    def to_dict(self):
        """permet d'envoyer un dico à l'affichage de rapport de matchs
        """
        matches_list_dict = []
        for _match in self.matches:
            one_match = {}
            one_match['joueur 1']=PlayerCrud.get_player_name(_match.player_id1)
            if _match.score_p1==None:
                one_match['winner']="en cours"
            elif _match.score_p1==1:
                one_match['winner']=PlayerCrud.get_player_name(_match.player_id1)
            elif _match.score_p2==1:
                one_match['winner']=PlayerCrud.get_player_name(_match.player_id2)
            else:
                one_match['winner']="match nul"
            if _match.player_id2!=None:
                one_match['joueur 2']=PlayerCrud.get_player_name(_match.player_id2)
            else:
                one_match['winner']=PlayerCrud.get_player_name(_match.player_id1)
                one_match['joueur 2']:"joueur1 sans adversaire"
            matches_list_dict.append(one_match)
        return matches_list_dict
    
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

