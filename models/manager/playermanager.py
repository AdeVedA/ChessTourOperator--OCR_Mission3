import os
import json
from views.utilsviews import UtilsView

datas_path = os.path.join(os.getcwd(),"datas", "players_data.json")

class PlayerCrud:
    #def __init__(datas_path):
    #    self.datas_path = os.path.join(os.getcwd(),"datas", "players_data.json")
    
    @classmethod
    def get_all_players(cls):
        """_summary_

        Returns:
            players_list : liste des joueurs
        """
        players_list = []
        if os.path.isfile(datas_path):
            with open(datas_path, 'r', encoding='utf-8') as file:
                try:
                    players_list = json.load(file)
                except json.JSONDecodeError:
                    pass
        else:
            os.makedirs(os.path.dirname(datas_path), exist_ok=True)
            UtilsView.input_return_prints("noplayer")
        return players_list

    @classmethod
    def save_new_player(cls, players_list, player):
        players_list.append(player.__dict__)
        with open(datas_path, 'w', encoding='utf8') as file:
             json.dump(players_list, file, ensure_ascii=False, indent=4)

    @classmethod
    def add(cls, player_dict_inf):
        players.append(PlayerModel(player_dict_inf))

    @classmethod
    def get_by_name(cls, lastname, players_list):
        players = []
        for player in players_list.get_all_players():
            if player.lastname == lastname:
                return player
        return None

    @classmethod
    def get_max_player_id(cls):
        players_list = PlayerCrud.get_all_players()
        max_player_id = max([int(player["player_id"]) for player in players_list], default=0)
        return max_player_id

    @classmethod
    def get_player_id(cls, chess_id):
        players_list = PlayerCrud.get_all_players()
        for player in players_list:
            if player["chess_id"] == chess_id:
                return int(player["player_id"])
        max_player_id = PlayerCrud.get_max_player_id()
        return max_player_id + 1 
