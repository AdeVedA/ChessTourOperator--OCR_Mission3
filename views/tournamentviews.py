from views.utilsviews import UtilsView as UV


class TournamentView:
    @classmethod
    def display(cls):
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
            "Veuillez saisir le lieu du tournoi : ", "string")
        tournament_infos["description"] = UV.valid_input(
            "Veuillez saisir la description du tournoi : ", "anything")
        tournament_infos["start_date"] = UV.valid_input(
            "Veuillez saisir la date de début du tournoi au format "
            "JJ/MM/AAAA : ", "date")
        # tournament_infos["end_date"] = UV.valid_input("Veuillez "
        #            "saisir la date de fin du tournoi au format "
        #            "JJ/MM/AAAA : ", "date")
        tournament_infos["rounds_nbr"] = UV.valid_input(
            "Veuillez saisir le nombre de rounds du tournoi : ", "integer")
        return tournament_infos

    @classmethod
    def tournament_choice(cls):
        '''choix du tournoi que l'on souhaite démarrer
        '''
        tournoi = UV.valid_input(
            "inscrivez le numéro du tournoi que "
            "vous souhaitez démarrer (et appuyez sur 'entrée'): ",
            "integer")
        return tournoi

    @classmethod
    def players_choice(cls, max_player_id):
        '''choix des joueurs que l'on souhaite inscire à un tournoi
        '''
        while True:
            players_tourn = UV.valid_input(
                "inscrivez les numéros des joueurs 'players_id' que vous "
                "souhaitez inscrire \nséparés par des virgules (ex : 1,3,8,10,"
                "13,15) et appuyez sur 'entrée'): ",
                "comma_integer_list", max_player_id)
            return players_tourn

    @classmethod
    def start_tournament_view(cls):
        """Permet de démarrer un tournoi en choisissant le tournoi et en
        sélectionnant les joueurs. Instancie et sauvegarde le tournoi.
        """
        header = "@ Sélection du Tournoi et des Joueurs @"
        menu_options = []
        UV.menu(header, menu_options)
        pass

    @classmethod
    def resume_tournament_view(cls):
        """Permet de reprendre un tournoi en choisissant le tournoi et en
        sélectionnant les joueurs. Instancie et sauvegarde le tournoi.
        """
        header = "@ Sélection du Tournoi pour reprise @"
        menu_options = []
        UV.menu(header, menu_options)
        pass

    @classmethod
    def continue_tour(cls):
        """permet de continuer à enchainer les fonctions
        d'avancement du tournoi
        """
        choice = UV.valid_input(
            "voulez-vous continuer à faire progresser les rounds"
            "de ce tournoi ? \n1 pour Oui, 2 pour Non : ",
            "choice")
        return choice

    '''
    @classmethod
    def display_round(cls, pairs):
        header = "Round actuel de votre tournoi d'échecs"
        menu_options = ["1.",
                        "",
                        "2.",
                        "",
                        "3.",
                        "",
                        "",
                        "0. Retour au menu principal"]
        UV.menu(header, menu_options)
        choice = input()
        return choice
    '''
