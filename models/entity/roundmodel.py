from models.manager.playermanager import PlayerCrud


class Round:
    """Représente un tournoi
    avec un nom, des matchs et des dates de début et de fin."""
    def __init__(self, name, start_date, end_date=None, matches=[]):
        """Initialise une nouvelle instance de la classe Round.
        Args:
        name (str): Le nom du tournoi.
        start_date ("datetime"): date de début du tournoi.
        end_date ("datetime"): date de fin du tournoi. None si non spécifiée.
        matches (list): liste de dictionnaires matchs joués dans le tournoi.
                        Defaut liste vide [] si non spécifiée.
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.matches = matches if matches else []

    def to_json(self):
        """Convertit l'objet Round en un dictionnaire JSON serialisable.
        Returns:
            dict: Un dictionnaire contenant les informations du tournoi et
                les matchs associés.
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
        """Prépare les données du round pour un affichage avec résultat
        dans un rapport.
        Returns:
            list: Une liste de dictionnaires contenant les informations des
                matchs et les noms des joueurs.
        """
        matches_list_dict = []
        for _match in self.matches:
            one_match = {}
            ply1 = _match.player_id1
            ply2 = _match.player_id2
            one_match['joueur 1'] = PlayerCrud.get_player_name(ply1)
            if _match.score_p1 is None:
                one_match['winner'] = "en cours"
            elif _match.score_p1 == 1:
                one_match['winner'] = PlayerCrud.get_player_name(ply1)
            elif _match.score_p2 == 1:
                one_match['winner'] = PlayerCrud.get_player_name(ply2)
            else:
                one_match['winner'] = "match nul"
            if _match.player_id2 is not None:
                one_match['joueur 2'] = PlayerCrud.get_player_name(ply2)
            else:
                one_match['winner'] = PlayerCrud.get_player_name(ply1)
                one_match['joueur 2'] = "sans adversaire"
            matches_list_dict.append(one_match)
        return matches_list_dict

    def __str__(self):
        return f'le tournoi "{self.name}", commencé le {self.start_date}, \
            {self.end_date if self.end_date is not None else None}, \
                {self.matches}'

    def __repr__(self):
        return f"{self.name}, {self.start_date}, \
            {self.end_date}, {self.matches}"
