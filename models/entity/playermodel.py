from models.manager.playermanager import PlayerCrud


class PlayerModel:

    def __init__(self, player_id, lastname, firstname, birth_date,
                 chess_id, points=0, *args, **kwargs):
        self.player_id = player_id
        self.lastname = lastname
        self.firstname = firstname
        self.birth_date = birth_date
        self.chess_id = chess_id
        #self.elo_rank = elo_rank
        self.points = points

    def __repr__(self):
        return f"Player{self.player_id} : {self.firstname} {self.lastname}"

    def win_point(self):
        self.points += 1

    def tie_point(self):
        self.points += 0.5

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.chess_id})"

    #def get_dico(self):
    #    player_dic = self...

