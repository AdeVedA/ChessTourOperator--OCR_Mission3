from views.utilsviews import UtilsView as UV
from views.reportviews import ReportView


class RoundView:

    @classmethod
    def roundheader(cls):
        """affiche le header Ascii-art du logiciel avec titre
        """
        header = "@  Rounds de votre Tournoi  @"
        menu_options = []
        UV.menu(header, menu_options)

    @classmethod
    def roundprint(cls, my_tournament, round_dict, previous=False):
        """mettre le dictionnaire du round en header/rows
        pour printer avec une fonction de rapport de round de reportview
        """
        header = round_dict[0].keys()
        rows = [game.values() for game in round_dict]
        if previous is True:
            ReportView.display_matches_list(
                rows, header, my_tournament.current_round - 1,
                my_tournament.name)
        else:
            ReportView.display_matches_list(
                rows, header, my_tournament.current_round,
                my_tournament.name)

    @classmethod
    def round_winners_input(cls):
        """inscription des résultats des matchs d'un round avec technique
        d'effacement/remplacement du message précédent pour affichage propre
        """
        choice = UV.valid_input("Voulez-vous inscrire les résultats "
                                "des matchs du round maintenant ?"
                                "\n1) pour Oui / 2) pour Non : ",
                                "choice")
        cursor_up = '\x1b[1A'
        erase_line = '\x1b[2K'
        print((cursor_up + erase_line)*3 + cursor_up)
        if choice == 1:
            round_results = UV.valid_input(
                "\nInscrivez les vainqueurs des matchs en cours dans l'"
                "ordre des matchs avec :\n1 pour joueur1, 2 pour joueur2, "
                "0 pour match nul, séparés par des virgules (ex : 1,2,0,2)\n"
                "et appuyez sur 'entrée'): ", "comma_integer_list", "2")
            print((cursor_up + erase_line)*3 + cursor_up)
            return round_results
        else:
            return None
