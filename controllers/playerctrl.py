from models.entity.playermodel import PlayerModel
from models.manager.playermanager import PlayerCrud
from .reportsctrl import ReportController
from views.playerviews import PlayerView
from views.utilsviews import UtilsView as UV


class PlayerController:
    """Contrôleur pour gérer les joueurs"""

    @classmethod
    def player_menu(cls):
        """Permet à l'utilisateur la gestion des joueurs"""
        while True:
            try:
                choice = PlayerView.display()
                match choice:
                    case "1":
                        cls.register_player()
                    case "2":
                        ReportController.display_players()
                    case "0":
                        break
                    case _:
                        UV.input_return_prints("choice_error")
            except (IndexError, ValueError, TypeError) as e:
                input(f"veuillez reprendre, erreur... {e} ")

    @classmethod
    def register_player(cls):
        '''inscription d'un joueur dans la base de données'''
        player_infos = PlayerView.player_infos()
        player_infos["player_id"] = int(f"{(
                PlayerCrud.get_player_id(player_infos["chess_id"]))}")
        player = PlayerModel(**player_infos)
        players_list = PlayerCrud.get_all_players()
        # sauvegarde
        PlayerCrud.save_new_player(players_list, player)
        # notification d'enregistrement du nouveau joueur
        UV.input_return_prints("player_reg",
                               player_infos["firstname"],
                               player_infos["lastname"])
        return
