

class MatchModel:
    def __init__(self, player_id1, score_p1, player_id2, score_p2):
        self.player_id1 = player_id1
        self.score_p1 = None
        self.player_id2 = player_id2
        self.score_p2 = None

    def __str__(self):
        if score_p1 == None:
            return f"Match : {self.player_id1} contre {self.player_id2} - en cours"
        elif score_p1 == 1:
            return f"Match : {self.player_id1} a vaincu {self.player_id2}"
        elif score_p2 == 1:
            return f"Match : {self.player_id1} a été vaincu par {self.player_id2}"
        else:
            return f"Match : {self.player_id1} et {self.player_id2} ont fait match nul"

    def __repr__(self):
        return f"([{self.player_id1}, {self.score_p1}],[{self.player_id2}, {self.score_p2}])"

    def set_result(self, winner):
        """établir le résultat du match et mettre à jour les points des joueurs.
        Args:
            winner (str): '1' for player_id1 wins, '2' for player_id2 wins, '0' for a draw.
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
            
    def to_tuple(self):
        """créer un tuple à partir des attributs de la class match
        """ 
        return tuple(f"[{self.player_id1}, {self.score_p1}], [{self.player_id2}, {self.score_p2}]")