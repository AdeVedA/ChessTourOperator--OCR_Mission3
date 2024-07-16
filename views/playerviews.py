from views.utilsviews import UtilsView as UV


class PlayerView:

    @classmethod
    def display(cls):
        """affiche la vue du menu de gestion des joueurs
        """
        header = "Gestion de la liste de joueurs d'échecs"
        menu_options = [
            "1. Inscrire un nouveau joueur",
            "",
            "2. Liste des joueurs inscrits par ordre alphabétique",
            "",
            "",
            "0. Retour au menu principal"
            ]
        UV.menu(header, menu_options)
        choice = input()
        return choice

    @classmethod
    def player_infos(cls):
        """suite d'inputs-utilisateur fournissant les données d'un joueur
        que l'on valide à l'aide des match-case d'UtilsView
        """
        player_infos = {}
        header = "@  INSCRIPTION D'UN JOUEUR  @"
        menu_options = []
        UV.menu(header, menu_options)
        player_infos["lastname"] = UV.valid_input(
            "Veuillez rentrer le nom de famille du joueur : ",
            "string_name").upper()
        player_infos["firstname"] = UV.valid_input(
            "Veuillez rentrer le prénom du joueur : ",
            "string_name").capitalize()
        player_infos["birth_date"] = UV.valid_input(
            "Veuillez rentrer la date de naissance "
            "du joueur au format JJ/MM/AAAA : ",
            "birthdate")
        player_infos["chess_id"] = UV.valid_input(
            "Veuillez rentrer l'identité nationale d'échec du joueur : ",
            "id_chess")
        return player_infos
