import os
import sys
import time
import re
from colorama import Fore, Style

spc = ' '
class UtilsView:

    @classmethod
    def menu(cls,header, menu_options):
        """Affiche un menu type avec infos en paramètres"""
        UtilsView.clear_screen()
        echec1 = f"███   ███   ███   ███   ███"
        echec2 = f"▀▀▀   ▀▀▀   ▀▀▀   ▀▀▀   ▀▀▀"
        echec3 = f"▄▄▄   ▄▄▄   ▄▄▄   ▄▄▄   ▄▄▄"
        UtilsView.style_print(content=f"{spc*9}#################################################\n")
        UtilsView.style_print(content=f"{spc*9}░▒░▒░▒░▒  {echec1[3:].center(30)}  ▒░▒░▒░▒\n", color=Fore.RED)
        UtilsView.style_print(content=f"{spc*9}░▒▀▄░▒░▒  {echec1[:-3].center(30)}  ▒░▒▄▀░▒\n")
        UtilsView.style_print(content=f"{spc*9}░▒░▒░▒░▒  {echec1[3:].center(30)}  ▒░▒░▒░▒\n", color=Fore.RED)
        UtilsView.style_print(content=f"{spc*9}░▒░       {echec2[:-3].center(30)}      ▒░▒\n", color=Fore.YELLOW)
        UtilsView.style_print(content=f"{spc*9}░▒░ {header.center(41)} ▒░▒\n", color=Fore.YELLOW)
        UtilsView.style_print(content=f"{spc*9}░▒░       {echec3[3:].center(30)}      ▒░▒\n", color=Fore.YELLOW)
        UtilsView.style_print(content=f"{spc*9}░▒░▒░▒░▒  {echec1[:-3].center(30)}  ▒░▒░▒░▒\n", color=Fore.RED)
        UtilsView.style_print(content=f"{spc*9}░▒▄▀░▒░▒  {echec1[3:].center(30)}  ▒░▒▀▄░▒\n")
        UtilsView.style_print(content=f"{spc*9}░▒░▒░▒░▒  {echec1[:-3].center(30)}  ▒░▒░▒░▒\n", color=Fore.RED)
        UtilsView.style_print(content=f"{spc*9}#################################################\n\n")
        if menu_options != []: #si menu_options=[] je n'affiche sur la page que l'ascii art du dessus
            UtilsView.style_print(content="Menu :\n\n")
            options = "\n".join(f"{spc*21}{option}" for option in menu_options)
            UtilsView.style_print(content=options, color=Fore.YELLOW)
            UtilsView.style_print(content="\n\nChoisissez une option: ")
        else:
            return

    @classmethod
    def clear_screen(cls):
        """vide l'écran avant affichage de menu ou d'informations"""
        os.system('cls' if os.name == 'nt' else 'clear')

    @classmethod
    def style_print(cls, content, color=Fore.GREEN):
        """styliser l'impression des contenus"""
        # WARNING = Fore.YELLOW
        BOLD = Style.BRIGHT
        CLReset = Style.RESET_ALL
        for letter in content:
            sys.stdout.flush()
            print(f"{color}{BOLD}{letter}{CLReset}", end='', flush=True)
            time.sleep(0.00000001)

    @classmethod
    def valid_input(cls, question, valid_format, *args):
        """valide le format de la réponse utilisateur pour assurer la qualité
           de la base de données et prévenir les erreurs de saisie

        Args:
            question (string): la question
            valid_format (string): le format attendu de la réponse utilisateur

        Returns:
            rep (various formats): la réponse au format valide
        """
        valid_ok = False
        while valid_ok is False:
            rep = input(f"{Fore.CYAN}{question}")
            match valid_format:
                case "string":
                    if rep is not rep or rep == "" \
                        or not rep.isalpha():
                        print(f"Veuillez inscrire une réponse valide")
                        continue
                    else:
                        return rep
                case "string_name":
                    if rep is not rep or rep == "" \
                        or re.match("^[-'a-zA-ZÀ-ÿ]+$", rep) is None:
                        print(f"Veuillez inscrire une réponse valide")
                        continue
                    else:
                        return rep
                case "integer":
                    if rep is not rep or rep == "" \
                        or not rep.isdigit():
                        print(f"Veuillez inscrire une réponse valide")
                        continue
                    else:
                        return rep
                case "date":
                    if rep is not rep or rep == "" \
                        or re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$',
                                        rep) is None:
                        print(f"Veuillez inscrire une date valide")
                        continue
                    else:
                        return rep
                case "id_chess":
                    if rep is not rep or rep == "" \
                            or re.match('^[A-Z]{2}[0-9]{5}$',
                                        rep) is None:
                        print(f"Veuillez rentrer une id valide, ex : AB12345")
                        continue
                    else:
                        return rep
                case "comma_integer_list":
                    if rep is not rep or rep == "" \
                        or re.match('^(\d+)(,\s*\d+)*', rep) is None:
                        print(f"Veuillez inscrire une réponse valide")
                        continue
                    #elif r for r in rep, r > int(args):
                    #    print("certains joueurs n'existent pas encore")
                    #    continue
                    else:
                        return rep
                case "anything":
                    if rep is not rep or rep == "" :
                        print(f"Veuillez inscrire une réponse valide")
                        continue
                    else:
                        return rep
                    """case "elo_rank":
                    if rep is not rep or rep == "" \
                            or re.match(r'^\d{3,4}$', rep) is None:
                        print(f"Veuillez inscrire une réponse valide")
                        continue
                    else:
                        return rep"""

    @classmethod
    def input_return_prints(cls, message, **kwargs):
        while True:
            match message:
                case "continue":
                    input(f"\n{Fore.YELLOW}{spc*26}appuyez sur une touche "
                          "pour continuer")
                    return
                case "choice_error":
                    input(f"\n\n{Fore.RED}{spc*12}Veuillez choisir une des "
                          f"options proposées.\n{spc*19}{Fore.GREEN}"
                          f"Appuyez sur la touche entrée")
                    return
                case "player_reg":
                    print(f"\n{Fore.YELLOW}{spc*19}le joueur a bien été "
                          "enregistré")
                    time.sleep(3)
                    return
                case "tournament_reg":
                    print(f"\n{Fore.YELLOW}{spc*18}le tournoi a bien été "
                          "enregistré")
                    time.sleep(3)
                    return
                case "tournament_select":
                    print(f"\n{Fore.YELLOW}{spc*26}le tournoi '{kwargs['name']}'"
                          " a bien été sélectionné")
                    time.sleep(1)
                    return
                case "bienvenue":
                    input(f"\n\n{Fore.YELLOW}{spc*10}Bienvenue dans le centre "
                          "névralgique de vos tournois échiquéens !"
                          f"\n\n{spc*24} Appuyez sur la touche entrée")
                    return
                case "quit":
                    print(f"{Fore.MAGENTA}\n\n\n######## Au "
                    "revoir les échecs !!! Belles réussites à vous\n"
                    f"\n{Fore.GREEN}")
                    break
                case "invalid_tournament":
                    print(f"{Fore.RED}Il semble que le fichier soit corrompu."
                          " Veuillez recréer un tournoi d'abord")
                    time.sleep(3)
                    return
                case "notournament":
                    print(f"{Fore.RED}Veuillez d'abord inscrire un premier "
                          "tournoi")
                    return
                case "noplayer":
                    print(f"{Fore.RED}Veuillez d'abord inscrire un "
                          "premier joueur")
                    return
