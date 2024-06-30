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
        if input("voulez-vous inscrire les résultats des matchs de ce round ?"
                " O pour Oui / N pour Non :  ") == "O" or "o":
            while True:
                round_results = UtilsView.valid_input(
                    "inscrivez les vainqueurs des matchs dans l'ordre avec 1 "
                    "pour joueur1, 2 pour joueur2, 0 pour match nul, séparés "
                    "par des virgules (ex : 1,2,1,0,1,2) et appuyez sur 'entrée'): ", 
                    "comma_integer_list")
                return round_results
        else:
            return

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
