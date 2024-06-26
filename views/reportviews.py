from views.utilsviews import UtilsView
from tabulate import tabulate
tabulate.MIN_PADDING = 0


class ReportView:

    @classmethod
    def display(cls):
        "affiche le dit menu en utilisant une methode d'UtilsView pour mise en page"
        header = "Rapports sur les joueurs et les tournois"
        menu_options = [
            "1. Liste des joueurs par ordre alphabétique",
            "",
            "2. Liste des joueurs d'un tournoi par ordre alphabétique",
            "",
            "",
            "3. Liste des tournois",
            "",
            "4. Nom et dates d'un tournoi donné",
            "",
            "5. rounds et matches d'un tournoi", 
            "",
            "",
            "", 
            "0. Retour au menu principal"
            ]
        UtilsView.menu(header, menu_options)
        choice = input()
        return choice

    @classmethod
    def display_players_list(cls, rows, header):
        "affiche le un tableau des joueurs en utilisant une methode d'UtilsView pour mise en page"
        UtilsView.clear_screen()
        UtilsView.style_print(content=f"{tabulate(rows, header,
                              maxheadercolwidths=[9, None, None, 10, 8, 6],
                              tablefmt='rounded_outline', numalign="left")}")

    @classmethod    
    def display_tournaments_list(cls, rows, header):
        "affiche le un tableau des tournois en utilisant une methode d'UtilsView pour mise en page"
        UtilsView.clear_screen()
        UtilsView.style_print(content=f"{tabulate(rows, header, 
            maxheadercolwidths=[10, 30, 26, 35, 10, 10, 7, 6, 12, 8],
            maxcolwidths=[10, 30, 26, 35, 10, 10, 5, 6, 11, 8],
            tablefmt='rounded_grid', numalign="left")}")
        print('\n')
        UtilsView.input_return_prints("continue")

    """
    @classmethod
    def display_tournament(tournament):
        '''affichage des données d'un tournoi'''
        print("Nom du tournoi : ", tournament.name)
        print("Lieu du tournoi : ", tournament.location)
        print("Description du tournoi : ", tournament.description)
        print("dates du tournoi : ", tournament.start_date, "-", tournament.end_date)
        print("rounds : ", tournament.rounds_nbr)        
    """
    