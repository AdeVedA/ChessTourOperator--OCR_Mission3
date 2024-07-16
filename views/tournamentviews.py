from views.utilsviews import UtilsView as UV


class TournamentView:

    @classmethod
    def display(cls):
        """affichage du menu et récupération du choix utilisateur
        returns : choix
        """
        header = "Gestion des tournois d'échecs"
        menu_options = ["1. Créer la matrice d'un tournoi",
                        "",
                        "2. Démarrer un tournoi (inscription des joueurs)",
                        "",
                        "3. Reprendre un tournoi",
                        "",
                        "",
                        "0. Retour au menu principal"]
        UV.menu(header, menu_options)
        choice = input()
        return choice

    @classmethod
    def tournament_infos(cls):
        '''suite d'inputs-utilisateur fournissant les données d'un tournoi'''
        tournament_infos = {}
        header = "@ Création d'un Tournoi d'Échecs @"
        menu_options = []
        UV.menu(header, menu_options)
        tournament_infos["name"] = UV.valid_input(
            "Veuillez saisir le nom du tournoi : ", "anything")
        tournament_infos["location"] = UV.valid_input(
            "Veuillez saisir le lieu du tournoi : ", "string_name")
        tournament_infos["description"] = UV.valid_input(
            "Veuillez saisir la description du tournoi : ", "anything")
        tournament_infos["start_date"] = UV.valid_input(
            "Veuillez saisir la date et l'heure de début du tournoi"
            " au format 'JJ/MM/AAAA HH:MM:SS' ou appuyez juste sur 'entrée' "
            " pour inscrire la date et l'heure actuelle : ", "date")
        tournament_infos["rounds_nbr"] = UV.valid_input(
            "Veuillez saisir le nombre de rounds du tournoi : ", "integer")
        return tournament_infos

    @classmethod
    def tournament_choice(cls, tourn_ids_list, firstrounds):
        '''choix du tournoi que l'on souhaite démarrer
        '''
        num = "Inscrivez le numéro du tournoi que vous souhaitez"
        instruc = "(et appuyez sur 'entrée') : "
        if firstrounds is False:
            tournoi = UV.valid_input(f"{num} reprendre {instruc}",
                                     "integer", tourn_ids_list)
        else:
            tournoi = UV.valid_input(f"{num} démarrer {instruc}",
                                     "integer", tourn_ids_list)
        return tournoi

    @classmethod
    def start_tournament_header(cls):
        """Affiche le logo de démarrage d'un tournoi et de
        sélection des joueurs.
        """
        header = "@ Sélection du Tournoi et des Joueurs @"
        menu_options = []
        UV.menu(header, menu_options)

    @classmethod
    def players_choice(cls, max_player_id):
        '''choix des joueurs que l'on souhaite inscire à un tournoi
        '''
        cursor_up = '\x1b[1A'
        erase_line = '\x1b[2K'
        while True:
            players_tourn = UV.valid_input(
                "Inscrivez les numéros des joueurs 'players_id' que vous "
                "souhaitez inscrire \nséparés par des virgules (ex : 1,3,8,10,"
                "13,15) et appuyez sur 'entrée'): ",
                "comma_integer_list", max_player_id)
            print((cursor_up + erase_line)*2 + cursor_up)
            return players_tourn

    @classmethod
    def resume_tournament_header(cls):
        """Affiche le logo de reprise d'un tournoi.
        """
        header = "@ Sélection du Tournoi pour reprise @"
        menu_options = []
        UV.menu(header, menu_options)

    @classmethod
    def continue_tour(cls):
        """permet de choisir de continuer à enchainer les fonctions
        d'avancement du tournoi.
        """
        choice = UV.valid_input(
            "\nVoulez-vous continuer à faire progresser les rounds"
            " de ce tournoi ? \n1 pour Oui, 2 pour Non : ",
            "choice")
        return choice
