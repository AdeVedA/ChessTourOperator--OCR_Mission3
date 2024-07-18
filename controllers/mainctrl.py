from controllers.playerctrl import PlayerController
from controllers.tournamentsctrl import TournamentController
from controllers.reportsctrl import ReportController
from views.mainview import MainMenuView
from views.utilsviews import UtilsView as UV


class MainController:
    """Contrôleur pour gérer le menu principal"""
    @classmethod
    def run(cls):
        MainMenuView.firstscreen()
        while True:
            choice = MainMenuView.display()
            match choice:
                case "1":
                    PlayerController.player_menu()
                case "2":
                    TournamentController.tournament_menu()
                case "3":
                    ReportController.report_menu()
                case "0":
                    UV.input_return_prints("quit")
                    break
                case _:
                    UV.input_return_prints("choice_error")
