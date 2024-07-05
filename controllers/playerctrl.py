from views.playerviews import PlayerView
from views.utilsviews import UtilsView
from models.entity.playermodel import PlayerModel
from models.manager.playermanager import PlayerCrud
from .reportsctrl import ReportController


class PlayerController:
    """Contrôleur pour gérer les joueurs"""
    
    @classmethod
    def player_menu(cls):
        '''Permet à l'utilisateur de lancer une des fonctions de gestion des joueurs'''
        while True:
            choice = PlayerView.display()
            match choice:
                case "1":
                    PlayerController.register_player()
                case "2":
                    ReportController.display_players()
                case "0":
                    break
                case _:
                    UtilsView.input_return_prints("choice_error")

    @classmethod
    def register_player(cls):
        '''inscription d'un joueur dans la base de données'''
        player_infos = PlayerView.player_infos()
        player_infos["player_id"] = int(f"{(PlayerCrud.get_player_id(player_infos["chess_id"]))}")
        player = PlayerModel(**player_infos)
        players_list = PlayerCrud.get_all_players()
        PlayerCrud.save_new_player(players_list, player)
        UtilsView.input_return_prints("player_reg", player_infos["firstname"], player_infos["lastname"])
        return

