from views.utilsviews import UtilsView as UV
from colorama import Fore
from tabulate import tabulate
tabulate.MIN_PADDING = 0


class ReportView:

    @classmethod
    def display(cls):
        """affiche le menu de rapports
        avec une methode d'UtilsView (UV) pour mise en page
        """
        header = "Rapports sur les joueurs et les tournois"
        menu_options = [
            "1. Liste des joueurs par ordre alphabétique",
            "",
            "2. Liste des joueurs d'un tournoi par ordre alphabétique",
            "",
            "",
            "3. Liste de tous les tournois",
            "",
            "4. Noms & dates des tournois",
            "",
            "5. Listes des rounds & matchs d'un tournoi",
            "   (classement & résultats des joueurs si tournoi fini)",
            "",
            "",
            "0. Retour au menu principal"
            ]
        UV.menu(header, menu_options)
        choice = input()
        return choice

    @classmethod
    def tour_choice_input(cls, args):
        """affiche un message demandant le choix du tournoi
        et valide la réponse avec le nombre de tournoi en argument
        """
        choice = UV.valid_input(
            "Inscrivez le numéro du tournoi "
            "qui vous intéresse (et appuyez sur 'entrée'): ",
            "integer_tour_choice", args)
        return choice

    @classmethod
    def display_players_list(cls, rows, header):
        """affiche un tableau `tabulate` des joueurs
        avec une methode d'UtilsView (UV)
        """
        UV.clear_screen()
        UV.style_print(content=f"{tabulate(rows, header,
                       maxheadercolwidths=[9, None, None, 10, 8, 6],
                       tablefmt='rounded_outline', numalign="left")}")

    @classmethod
    def display_tournaments_list(cls, rows, header):
        """affiche un tableau `tabulate` des tournois
        avec une methode d'UtilsView (UV)
        """
        UV.clear_screen()
        tab = f"{tabulate(rows, header,
                 maxheadercolwidths=[10, 30, 26, 35, 10, 10, 9, 9, 11, 8],
                 maxcolwidths=[10, 30, 26, 35, 10, 10, 9, 9, 11, 8],
                 tablefmt='rounded_grid', numalign="left")}"
        UV.style_print(content=tab)
        # print('\n')
        UV.input_return_prints("continue")

    @classmethod
    def display_matches_list(cls, rows, header, round_nbr, tournament_name):
        """affiche le un tableau `tabulate` des matchs
        avec une methode d'UtilsView (UV)
        """
        UV.style_print(
            content=f'Le round {round_nbr} du tournoi "{tournament_name}" '
            f"comporte les matchs suivants : \n", color=Fore.YELLOW)
        UV.style_print(
            content=f"{tabulate(
                rows, header, tablefmt='rounded_grid', numalign="left")}")
        print('\n')
        # UV.input_return_prints("continue")

    @classmethod
    def display_finished_tournament_players_list(cls, rows, header,
                                                 rounds_nbr, tournament_name,
                                                 end_date, location):
        """affiche un tableau `tabulate` des résultats finaux d'un tournoi
        avec une methode d'UtilsView (UV)
        """
        UV.style_print(content=f'Le tournoi "{tournament_name}" de '
                               f"{rounds_nbr} rounds s'achève en ce {end_date}"
                               f" sur ces résultats : \n", color=Fore.YELLOW)
        UV.style_print(content=f"{tabulate(rows, header,
                       tablefmt='rounded_grid', numalign="left")}")
        UV.style_print(content=f"\n Bonne fête à {location} pour "
                               f"tout le monde !!!\n", color=Fore.MAGENTA)
        UV.input_return_prints("continue")
