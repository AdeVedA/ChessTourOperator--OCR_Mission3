from views.utilsviews import UtilsView
from views.reportviews import ReportView

class RoundView:

    @classmethod
    def roundheader(cls):
        header = "@  Rounds de votre Tournoi  @"
        menu_options = []
        UtilsView.menu(header, menu_options)

    @classmethod
    def roundprint(cls,my_tournament,round_dict):
        matches_list_dict = round_dict
        header = matches_list_dict[0].keys()
        rows = [game.values() for game in matches_list_dict]
        ReportView.display_matches_list(rows,header,my_tournament.current_round,my_tournament.name)

    @classmethod
    def round_winners_input(cls, round_dict):
        '''choix des joueurs que l'on souhaite inscire à un tournoi
        '''
        choice = UtilsView.valid_input("voulez-vous inscrire les résultats "
            "des matchs du round ?\n1) pour Oui / 2) pour Non : ", "choice")
        if choice == 1:
            round_results = UtilsView.valid_input(
                "\ninscrivez les vainqueurs des matchs dans l'ordre des matchs"
                " avec :\n1 pour joueur1, 2 pour joueur2, 0 pour match nul, "
                "séparés par des virgules (ex : 1,2,0,2)\net appuyez sur "
                "'entrée'): ", "comma_integer_list")
            return round_results
        else:
            return None
    """
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
    """