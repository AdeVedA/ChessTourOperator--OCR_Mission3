from views.utilsviews import UtilsView
from colorama import Fore
import re


class PlayerView:
    
    @classmethod
    def display():
        header = "Gestion de la liste de joueurs d'échecs"
        menu_options = [
            "1. Inscrire un nouveau joueur",
            "",
            "2. Liste des joueurs inscrits par ordre alphabétique",
            "",
            "",
            "0. Retour au menu principal"
            ]
        UtilsView.menu(header, menu_options)
        choice = input()
        return choice

    @classmethod
    def player_infos():
        """suite d'inputs-utilisateur fournissant les données d'un joueur"""
        player_infos = {}
        header = "@  INSCRIPTION D'UN JOUEUR  @"
        menu_options = []
        UtilsView.menu(header, menu_options)
        player_infos["lastname"] = UtilsView.valid_input("Veuillez rentrer "
                    "le nom de famille du joueur : ", "string_name").upper()
        player_infos["firstname"] = UtilsView.valid_input("Veuillez rentrer "
                    "le prénom du joueur : ", "string_name").capitalize()
        player_infos["birth_date"] = UtilsView.valid_input("Veuillez rentrer"
                    " la date de naissance du joueur au format JJ/MM/AAAA : ",
                     "date")
        player_infos["chess_id"] = UtilsView.valid_input("Veuillez rentrer "
                    "l'identité nationale d'échec du joueur : ", "id_chess")
        '''player_infos["elo_rank"] = UtilsView.valid_input("Veuillez rentrer "
                    "le classement Elo du joueur : ", "elo_rank")'''
        player_infos["points"] = UtilsView.valid_input("Veuillez rentrer "
                    "le score du joueur : ", "integer")
        return player_infos
