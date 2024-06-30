from views.utilsviews import UtilsView
from views.reportviews import ReportView

class RoundView:

    @classmethod
    def roundheader(cls):
        header = "@  Rounds de votre Tournoi  @"
        menu_options = []
        UtilsView.menu(header, menu_options)

    def roundprint(cls,rounds):
        matches_list_dict = round_matches
        header = matches_list_dict[0].keys()
        rows = [game.values() for game in matches_list_dict]
        ReportView.display_matches_list(rows, header)

    @classmethod
    def display(cls):
        header = "Gestion des rounds d'un tournoi"
        menu_options = ["1. Inscrire les résultats d'un round d'un tournoi",
                        "",
                        "2. Afficher les matchs d'un round",
                        "",
                        "",
                        "0. Retour au menu principal"]
        UtilsView.menu(header, menu_options)
