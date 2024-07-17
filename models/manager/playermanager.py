import os
import json
from views.utilsviews import UtilsView as UV

datas_path = os.path.join(os.getcwd(), "datas", "players_data.json")


class PlayerCrud:

    @classmethod
    def get_all_players(cls, *args):
        """récupère les informations de tous les joueurs présents
        en base de données json
        Returns:
            players_list : liste de dictionnaires des joueurs
        """
        players_list = []
        if os.path.isfile(datas_path):
            with open(datas_path, 'r', encoding='utf-8') as file:
                try:
                    players_list = json.load(file)
                except json.JSONDecodeError:
                    pass
        # s'il n'y a pas de fichier/répertoire, on le crée
        else:
            os.makedirs(os.path.dirname(datas_path), exist_ok=True)
            UV.input_return_prints("noplayer")
        return players_list

    @classmethod
    def save_new_player(cls, players_list, player):
        """procédure de sauvegarde des informations d'un nouveau joueur
        dans la base de données json des joueurs
        Args :
                players_list : liste des joueurs
                player :
        """
        players_list.append(player.__dict__)
        with open(datas_path, 'w', encoding='utf8') as file:
            json.dump(players_list, file, ensure_ascii=False, indent=4)

    @classmethod
    def get_max_player_id(cls):
        """récupérer le numéro de joueur le plus élevé (pour nommer par
        incrémentation celui d'un nouveau joueur à inscrire avec la méthode
        suivante)
        """
        players_list = cls.get_all_players()
        max_player_id = max(
                [int(player["player_id"]) for player in players_list],
                default=0)
        return max_player_id

    @classmethod
    def get_player_id(cls, chess_id):
        """fonction chiffrant par incrémentation le numéro
        d'un nouveau joueur à inscrire
        """
        players_list = cls.get_all_players()
        for player in players_list:
            if player["chess_id"] == chess_id:
                return int(player["player_id"])
        max_player_id = cls.get_max_player_id()
        return max_player_id + 1

    @classmethod
    def get_player_name(cls, chess_id):
        """fonction retournant le nom de famille et le prénom d'un joueur
        à partir de son chess_id
        """
        players_list = cls.get_all_players()
        for player in players_list:
            if player['chess_id'] == str(chess_id):
                return f"{player["lastname"]} {player['firstname']}"

    @classmethod
    def get_player_inf_from__chess_id(cls, chess_id):
        """fonction retournant le nom, le prénom, la date de naissance (et
        le chess_id) d'un joueur à partir de son chess_id
        """
        players_list = cls.get_all_players()
        for player in players_list:
            if player["chess_id"] == chess_id:
                return [player["lastname"],
                        player['firstname'],
                        player['birth_date'],
                        player['chess_id']]
