class MatchModel:
    """Représente un match
    avec un joueur, son score, un adversaire et le score de l'adversaire"""
    def __init__(self, player_id1, score_p1, player_id2, score_p2):
        """Initialise une instance de la classe MatchModel
        avec les identifiants des joueurs et leurs scores.
        Args:
            player_id1 (str): Identifiant du premier joueur.
            score_p1 (float/None): Score du premier joueur, initialisé à None.
            player_id2 (str): Identifiant du second joueur.
            score_p2 (float/None): Score du second joueur, initialisé à None.
        """
        self.player_id1 = player_id1
        self.score_p1 = score_p1
        self.player_id2 = player_id2
        self.score_p2 = score_p2

    def to_json(self):
        """convertit un objet match pour serialisation en JSON
        returns:
            _match : liste contenant 2 listes type [joueur, points du joueur]
        """
        _match = [[f"{self.player_id1}", int(self.score_p1)
                   if self.score_p1 is not None else 0],
                  [f"{self.player_id2}", int(self.score_p2)
                   if self.score_p2 is not None else 0]]
        return _match

    def set_result(self, winner):
        """Définit le résultat du match et met à jour les scores des joueurs.
        Args:
            winner (str): '1' si player_id gagne,
            '2' si player_id2 gagne, '0' en cas de match nul.
        Returns:
            tuple[float or integer]: Scores du match mis à jour.
        """
        if winner == 1:
            self.score_p1 = 1
            self.score_p2 = 0
        elif winner == 2:
            self.score_p1 = 0
            self.score_p2 = 1
        elif winner == 0:
            self.score_p1 = 0.5
            self.score_p2 = 0.5
        return self.score_p1, self.score_p2

    def to_tuple(self):
        """Crée un tuple à partir des attributs de l'instance Match.
        Returns:
            tuple[list]: Tuple contenant les informations sur les joueurs
                et leurs scores.
        """
        return ([f"{self.player_id1}", self.score_p1],
                [f"{self.player_id2}", self.score_p2])

    def __str__(self):
        if self.score_p1 is None:
            return f"Match : {self.player_id1} \
                contre {self.player_id2} - en cours"
        elif self.score_p1 == 1:
            return f"Match : {self.player_id1} \
                a vaincu {self.player_id2}"
        elif self.score_p2 == 1:
            return f"Match : {self.player_id1} \
                a été vaincu par {self.player_id2}"
        else:
            return f"Match : {self.player_id1} \
                et {self.player_id2} ont fait match nul"

    def __repr__(self):
        return [[{self.player_id1}, {self.score_p1}],
                [{self.player_id2}, {self.score_p2}]]
