from views.mainview import MainMenuView
from controllers.playerctrl import PlayerController
from controllers.tournamentsctrl import TournamentController
from controllers.reportsctrl import ReportController
from views.utilsviews import UtilsView
from colorama import Fore


class MainController:

    @classmethod
    def run():
        MainMenuView().firstscreen()
        while True:
            choice = MainMenuView().display()
            match choice:
                case "1":
                    PlayerController.player_menu()
                case "2":
                    TournamentController.tournament_menu()
                case "3":
                    ReportController.report_menu()
                case "0":
                    UtilsView.input_return_prints("quit")
                    break
                case _:
                    UtilsView.input_return_prints("choice_error")
