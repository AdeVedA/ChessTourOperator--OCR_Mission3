import os
import re
import sys
import time
from colorama import Fore, Style

spc = ' '
cursor_up = '\x1b[1A'
erase_line = '\x1b[2K'


class UtilsView:
    """Vue utile à toutes les vues/contrôleurs pour les messages types de
    retours de choix utilisateurs et de notification d'étape (sauvegarde),
    les print stylisés/colorés, le header menu/titre (mon 1er ascii art),
    les validations des données issues des saisies de l'utilisateur
    """
    @classmethod
    def menu(cls, header, menu_options):
        """Affiche un menu type avec infos en paramètres"""
        cls.clear_screen()
        echec1 = "███   ███   ███   ███   ███"
        echec2 = "▀▀▀   ▀▀▀   ▀▀▀   ▀▀▀   ▀▀▀"
        echec3 = "▄▄▄   ▄▄▄   ▄▄▄   ▄▄▄   ▄▄▄"
        cls.style_print(
            content=f"{spc*9}######################"
            "###########################\n")
        cls.style_print(
            content=f"{spc*9}░▒░▒░▒░▒  {echec1[3:].center(30)}  ▒░▒░▒░▒\n",
            color=Fore.RED)
        cls.style_print(
            content=f"{spc*9}░▒▀▄░▒░▒  {echec1[:-3].center(30)}  ▒░▒▄▀░▒\n")
        cls.style_print(
            content=f"{spc*9}░▒░▒░▒░▒  {echec1[3:].center(30)}  ▒░▒░▒░▒\n",
            color=Fore.RED)
        cls.style_print(
            content=f"{spc*9}░▒░       {echec2[:-3].center(30)}      ▒░▒\n",
            color=Fore.YELLOW)
        cls.style_print(
            content=f"{spc*9}░▒░ {header.center(41)} ▒░▒\n", color=Fore.YELLOW)
        cls.style_print(
            content=f"{spc*9}░▒░       {echec3[3:].center(30)}      ▒░▒\n",
            color=Fore.YELLOW)
        cls.style_print(
            content=f"{spc*9}░▒░▒░▒░▒  {echec1[:-3].center(30)}  ▒░▒░▒░▒\n",
            color=Fore.RED)
        cls.style_print(
            content=f"{spc*9}░▒▄▀░▒░▒  {echec1[3:].center(30)}  ▒░▒▀▄░▒\n")
        cls.style_print(
            content=f"{spc*9}░▒░▒░▒░▒  {echec1[:-3].center(30)}  ▒░▒░▒░▒\n",
            color=Fore.RED)
        cls.style_print(
            content=f"{spc*9}######################"
            "###########################\n\n")
        if menu_options != []:
            # si menu_options=[], affiche l'AsciiArt du dessus sans options
            cls.style_print(content="Menu :\n\n")
            options = "\n".join(f"{spc*21}{option}" for option in menu_options)
            cls.style_print(content=options, color=Fore.YELLOW)
            cls.style_print(content="\n\nChoisissez une option : ")
        else:
            return

    @classmethod
    def clear_screen(cls):
        """vide l'écran avant affichage de pages de menu ou d'informations"""
        os.system('cls' if os.name == 'nt' else 'clear')

    @classmethod
    def style_print(cls, content, color=Fore.GREEN):
        """styliser l'impression des contenus"""
        BOLD = Style.BRIGHT  # between color & letter : {BOLD}
        CLReset = Style.RESET_ALL
        for letter in content:
            sys.stdout.flush()
            print(f"{color}{BOLD}{letter}{CLReset}", end='', flush=True)
            time.sleep(0.000001)

    @classmethod
    def valid_input(cls, question, valid_format, *args):
        """valide le format de la réponse utilisateur pour assurer la qualité
        de la base de données et prévenir des erreurs de saisie
        Args:
            question (string): la question
            valid_format (string): le format attendu de la réponse utilisateur
            *args : argument optionnel permettant de recueillir les valeurs
                    contextuelles autorisées ou d'ajouter des validations
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
                        print(f"{Fore.RED}Veuillez inscrire "
                              "une réponse valide")
                        continue
                    else:
                        return rep
                case "string_name":
                    if rep is not rep or rep == "" \
                            or re.match("^[-'a-zA-ZÀ-ÿ]+$", rep) is None:
                        print(f"{Fore.RED}Veuillez inscrire "
                              "une réponse valide")
                        continue
                    else:
                        return rep
                case "integer":
                    if args:
                        if int(rep) not in [ids for ids in args[0]]:
                            print(f"{Fore.RED}Veuillez rentrer un numéro de "
                                  "tournoi valide")
                            continue
                        else:
                            pass
                    if rep is not rep or rep == "" \
                            or not rep.isdigit():
                        print(f"{Fore.RED}Veuillez inscrire "
                              "une réponse valide")
                        continue
                    else:
                        return int(rep)
                case "date":
                    if rep is not rep or rep == "" \
                            or re.match(r"^(3[01]|[12][0-9]|0?[1-9])(\/|\-|\.)"
                                        r"(1[0-2]|0?[1-9])\2([12][0-9]{3})$",
                                        rep) is None:
                        print(f"{Fore.RED}Veuillez inscrire une date valide")
                        continue
                    else:
                        return rep
                case "id_chess":
                    if rep is not rep or rep == "" \
                            or re.match('^[A-Z]{2}[0-9]{5}$',
                                        rep) is None:
                        print(f"{Fore.RED}Veuillez rentrer une "
                              "id valide, ex : AB12345")
                        continue
                    else:
                        return rep
                case "comma_integer_list":
                    if args:
                        for r in list(map(int, rep.split(','))):
                            if r > int(args[0]):
                                print(f"{Fore.RED}Veuillez inscrire une "
                                      "réponse valide")
                                continue
                            else:
                                pass
                    if rep is not rep or rep == "" or \
                            re.match(r"^(\d+)(,\s*\d+)*", rep) is None:
                        print(f"{Fore.RED}Veuillez inscrire une "
                              "réponse valide")
                        continue
                    else:
                        return rep
                case "choice":
                    if rep is not rep or rep == "" \
                            or re.match('^[1,2]{1}$', rep) is None:
                        print(f"{Fore.RED}Veuillez inscrire une "
                              "réponse valide")
                        continue
                    else:
                        return int(rep)
                case "anything":
                    if rep is not rep or rep == "":
                        print(f"{Fore.RED}Veuillez inscrire une "
                              "réponse valide")
                        continue
                    else:
                        return rep
                case "integer_tour_choice":
                    if rep is not rep or rep == "" \
                            or not rep.isdigit():
                        print(f"{Fore.RED}Veuillez inscrire "
                              "une réponse valide")
                        continue
                    if args:
                        if int(rep) not in range(1, int(args[0]) + 1):
                            print(f"{Fore.RED}Veuillez rentrer un "
                                  "numéro de tournoi valide")
                            continue
                        else:
                            return int(rep)
                    else:
                        return int(rep)

    @classmethod
    def input_return_prints(cls, message, *args, **kwargs):
        """permet d'afficher des messages en retour des entrées
        ou pour notification des sauvegardes etc
        Args:
            message est le "case" pour référrencer le message
            *args & **kwargs : Arguments optionnels pour messages
                personnalisés
        """
        while True:
            match message:
                case "continue":
                    input(f"\n{Fore.YELLOW}{spc*26}Appuyez sur la touche "
                          "'entrée' pour continuer")
                    print(cursor_up + erase_line + cursor_up)
                    return
                case "choice_error":
                    input(f"\n\n{Fore.RED}{spc*12}Veuillez choisir une des "
                          f"options proposées.\n{spc*19}{Fore.GREEN}"
                          f"Appuyez sur la touche entrée")
                    print((cursor_up + erase_line)*2 + cursor_up)
                    return
                case "player_reg":
                    print(f"\n{Fore.YELLOW}{spc*19}{args[0]} "
                          f"{args[1]} a bien été enregistré")
                    time.sleep(3)
                    return
                case "tournament_reg":
                    print(f"\n{Fore.YELLOW}{spc*18}Le tournoi a bien été "
                          "enregistré")
                    time.sleep(3)
                    return
                case "tournament_save":
                    print(f"\n{Fore.YELLOW}{spc*18}Le tournoi '{args[0]}'"
                          " vient d'être sauvegardé")
                    time.sleep(3)
                    return
                case "tournament_select":
                    print(f"\n{Fore.YELLOW}{spc*26}Le tournoi "
                          f"'{kwargs['name']}' a bien été sélectionné")
                    time.sleep(2)
                    return
                case "bienvenue":
                    input(f"\n\n{Fore.YELLOW}{spc*10}Bienvenue dans le centre "
                          "névralgique de vos tournois échiquéens !"
                          f"\n\n{spc*24} Appuyez sur la touche entrée")
                    return
                case "quit":
                    print(f"{Fore.MAGENTA}\n\n\n######## Au revoir "
                          "les échecs !!! Belles réussites à vous\n"
                          f"\n{Fore.GREEN}")
                    break
                case "invalid_tournament":
                    print(f"{Fore.RED}Il semble que le fichier soit corrompu."
                          " Veuillez recréer un tournoi d'abord")
                    time.sleep(1)
                    return
                case "notournament":
                    input(f"{Fore.RED}Veuillez d'abord inscrire un premier "
                          "tournoi si vous tentez d'en démarrer un, ou "
                          "avancer un tournoi au prochain round sinon.\n"
                          "appuyez sur la touche 'entrée' pour continuer")
                    print((cursor_up + erase_line)*2 + cursor_up)
                    return
                case "noplayer":
                    input(f"{Fore.RED}Veuillez d'abord inscrire un "
                          "premier joueur pour ce tournoi. "
                          "Appuyez sur la touche 'entrée'")
                    print(cursor_up + erase_line + cursor_up)
                    return
                case "noround":
                    input(f"{Fore.RED}Veuillez d'abord avancer ce tournoi "
                          "au prochain round avant de demander ce rapport.\n"
                          "appuyez sur la touche 'entrée' pour continuer")
                    print((cursor_up + erase_line)*2 + cursor_up)
                    return
