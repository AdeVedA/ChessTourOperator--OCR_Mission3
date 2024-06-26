from views.utilsviews import UtilsView


class RoundView:

    @classmethod
    def display():
        header = "Gestion des rounds d'échecs"
        menu_options = ["1. Inscrire les résultats d'un round d'un tournoi",
                        "",
                        "2. Afficher les matchs d'un round",
                        "",
                        "",
                        "0. Retour au menu principal"]
        UtilsView.menu(header, menu_options)
