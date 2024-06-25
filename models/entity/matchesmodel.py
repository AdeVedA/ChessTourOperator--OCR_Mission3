

class MatchModel:
    def __init__(self, player_id1, player_id2, result=None):
        self.player_id1 = player_id1
        self.player_id2 = player_id2
        self.result = None
        
    def set_result(self, winner):
        """établir le résultat du match et mettre à jour les points des joueurs.
        Args:
            winner (str): '1' for player_id1 wins, '2' for player_id2 wins, '0' for a draw.
        """
        self.result = winner
        if winner == 1:
            player_id1.win_point()
        elif winner == 2:
            player_id2.win_point()
        else:
            player_id1.tie_point()
            player_id2.tie_point()
            