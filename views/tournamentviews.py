from views.utilsviews import UtilsView


class TournamentView:
    @classmethod
    def display(cls):
        header = "Gestion des tournois d'échecs"
        menu_options = ["1. Créer la matrice d'un tournoi",
                        "",
                        "2. Démarrer un tournoi (avec inscription des joueurs)",
                        "",
                        "3. Reprendre un tournoi",
                        "",
                        "",
                        "0. Retour au menu principal"]
        UtilsView.menu(header, menu_options)
        choice = input()
        return choice

    @classmethod
    def tournament_infos(cls):
        '''suite d'inputs-utilisateur fournissant les données d'un tournoi'''
        tournament_infos = {}
        header = "@  Création d'un Tournoi d'Échecs @"
        menu_options = []
        tournament_infos["name"] = UtilsView.valid_input("Veuillez saisir "
                    "le nom du tournoi : ", "anything")
        tournament_infos["location"] = UtilsView.valid_input("Veuillez "
                    "saisir le lieu du tournoi : ", "string")
        tournament_infos["description"] = UtilsView.valid_input("Veuillez "
                    "saisir la description du tournoi : ", "anything")
        tournament_infos["start_date"] = UtilsView.valid_input("Veuillez "
                    "saisir la date de début du tournoi au format "
                    "JJ/MM/AAAA : ", "date")
        #tournament_infos["end_date"] = UtilsView.valid_input("Veuillez "
        #            "saisir la date de fin du tournoi au format "
        #            "JJ/MM/AAAA : ", "date")
        tournament_infos["rounds_nbr"] = UtilsView.valid_input("Veuillez "
                    "saisir le nombre de rounds du tournoi : ", "integer")
        return tournament_infos

    @classmethod
    def tournament_choice(cls):
        '''choix du tournoi que l'on souhaite démarrer
        '''
        tournoi = UtilsView.valid_input("inscrivez le numéro du tournoi que "
                        "vous souhaitez démarrer (et appuyez sur 'entrée'): ",
                        "integer")
        #input("inscrivez le numéro du tournoi que vous souhaitez démarrer (et appuyez sur 'entrée'): ")
        return tournoi

    @classmethod
    def players_choice(cls, max_player_id):
        '''choix des joueurs que l'on souhaite inscire à un tournoi
        '''
        while True:
            players_tourn = UtilsView.valid_input(
                "inscrivez les numéros des joueurs 'players_id' que vous "
                "souhaitez inscrire séparés par des virgules (ex : 1,3,8,10,"
                "13,15) et appuyez sur 'entrée'): ", 
                "comma_integer_list", max_player_id)
            return players_tourn
        
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
        UtilsView.menu(header, menu_options)
        choice = input()
        return choice