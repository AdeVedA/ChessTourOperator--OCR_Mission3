from views.tournamentviews import TournamentView
from views.utilsviews import UtilsView
from models.entity.tournamentmodel import TournamentModel
from models.manager.tournamentmanager import TournamentCrud
from models.entity.playermodel import PlayerModel
from models.manager.playermanager import PlayerCrud
from models.entity.roundmodel import Round
from .roundctrl import RoundController
from .reportsctrl import ReportController
from datetime import datetime

class TournamentController:
    '''Contrôleur pour gérer les tournois.'''

    @classmethod
    def tournament_menu(cls):
        '''Permet à l'utilisateur de lancer une des fonctions de gestion de tournois'''
        while True:
            choice = TournamentView.display()
            match choice:
                case "1":
                    TournamentController.create_tournament()
                case "2":
                    TournamentController.start_tournament_menu()
                case "3":
                    TournamentController.resume_tournament_menu()
                case "0":
                    break
                case _:
                    UtilsView.input_return_prints("choice_error")

    @classmethod
    def create_tournament(cls):
        """Permet de créer une matrice de tournoi (infos du tournoi sans joueurs)
        Collecte les informations du tournoi via TournamentView, 
        crée un objet TournamentModel avec ces infos et sauvegarde le nouveau tournoi.
        Args:
            cls (TournamentController): La classe elle-même appelée pour accéder aux méthodes de la classe.
        """
        tour_infos = TournamentView.tournament_infos()
        tournament = TournamentModel(**tour_infos)
        TournamentCrud.save_new_tournament(tournament)
        UtilsView.input_return_prints("tournament_reg")
        return

    @classmethod
    def start_tournament_menu(cls):
        '''Permet de démarrer un tournoi en choisissant le tournoi et en sélectionnant les joueurs
        instancie les joueurs sélectionnés, le tournoi, et sauvegarde le tournoi en l'état.
        '''
        # selection du tournoi
        TournamentView.start_tournament_view()
        selected_tournament = TournamentController.choose_tournament()
        UtilsView.input_return_prints("tournament_select", 
                                      **selected_tournament)
        # si aucun joueur enregistré, inscription des joueurs au tournoi,
        # on instancie et on sauve
        if selected_tournament['players_tour'] == []:
            TournamentController.tournament_add_players(selected_tournament)
            my_tournament = TournamentModel(**selected_tournament)
            TournamentCrud.update_tournament_players(my_tournament)
        # sinon si il y a déjà des joueurs on instancie le tournoi
        else :
            my_tournament = TournamentModel(**selected_tournament)
        # on instancie les joueurs du tournoi
        instantiated_players = TournamentController.instantiate_tournament_players(my_tournament.players_tour)
        # on va créer le round 1 de ce tournoi et inscrire les matchs ou les résultats aussi
        my_tournament, round1 = RoundController.round_one_matches(my_tournament, instantiated_players)
        # on sauvegarde
        my_tournament = TournamentCrud.update_tournament(my_tournament, round1)
        TournamentController.check_if_tourn_finished(my_tournament)

    @classmethod
    def resume_tournament_menu(cls):
        """Permet de reprendre un tournoi inachevé, instancie les joueurs
        et le prochain round et sauvegarde l'état actuel du tournoi.
        """
        # selection du tournoi
        TournamentView.resume_tournament_view()
        tourn_next = "dummy switch pour affichage des rounds >1"
        selected_tournament = TournamentController.choose_tournament(tourn_next)
        # instanciation du tournoi
        my_tournament = TournamentModel(**selected_tournament)
        UtilsView.input_return_prints("tournament_select", 
                                      **selected_tournament)
        # on instancie les joueurs du tournoi
        instantiated_players = TournamentController.instantiate_tournament_players(my_tournament.players_tour)
        round_next, my_tournament = RoundController.make_next_round(my_tournament, instantiated_players)
        my_tournament = TournamentCrud.update_tournament(my_tournament, round_next)
        TournamentController.check_if_tourn_finished(my_tournament)

    @classmethod
    def choose_tournament(cls, *args):
        """permet de demander l'affichage d'une liste de tournois
        Args:
            *args: Argument optionnel pour l'affichage des tournois où les rounds >1.
        Returns:
            dict: Le dictionnaire représentant le tournoi sélectionné
        """
        if args:
            ReportController.display_alltournaments(args)
        else :
            ReportController.display_alltournaments()
        tournaments_list = TournamentCrud.get_all_tournaments()
        selected_tournament = TournamentController.select_tournament(tournaments_list)
        return selected_tournament

    @classmethod
    def select_tournament(cls, tournaments_list):
        '''Permet de sélectionner un tournoi parmi une liste de tournois.
        Args:
            cls (TournamentController): La classe elle-même appelée pour accéder aux méthodes de la classe.
            tournaments_list (list): Liste des dictionnaires représentant les tournois disponibles.
        Returns:
            dict: Le dictionnaire représentant le tournoi sélectionné
        '''
        selected_tournament = None
        while not selected_tournament:
            try:
                tournament_id_inpt = int(TournamentView.tournament_choice()) - 1
                if 0 <= tournament_id_inpt < len(tournaments_list):
                    selected_tournament = tournaments_list[tournament_id_inpt]
                else:
                    raise ValueError("Invalid selection")
            except (ValueError, TypeError):
                UtilsView.input_return_prints("choice_error")
        return selected_tournament

    @classmethod    
    def tournament_add_players(cls, selected_tournament):
        """permet d'inscrire des joueurs (enregistrés dans players.json) à un tournoi
        Args: selected_tournament (dict): Dictionnaire représentant le tournoi sélectionné.
        """
        ReportController.display_players()
        selected_players = []
        while not selected_players:
            try:
                max_player_id = PlayerCrud.get_max_player_id()
                players_id_tour_inpt = (f"{TournamentView.players_choice(max_player_id)}")
                numbers = [int(n) - 1 for n in players_id_tour_inpt.split(',')]
                players_list = PlayerCrud.get_all_players()
                players_sel = []
                for number in numbers:
                    player_chess_id = players_list[number]['chess_id']
                    players_sel.append(player_chess_id)
                selected_tournament['players_tour'] = players_sel
                selected_players = selected_tournament['players_tour']
                print(selected_players) 
            except (ValueError, TypeError):
                UtilsView.input_return_prints("choice_error")

    @classmethod
    def instantiate_tournament_players(cls, tour_players_list):
        '''permet d'instancier tous les joueurs d'un tournoi
        Args : tour_players_list = la liste de joueurs de l'instance "my_tournament" (attribut .players_tour)
        Returns: Liste des instances PlayerModel des joueurs du tournoi.
        '''
        instantiated_players = []
        players_list = PlayerCrud.get_all_players() 
        for chess_id in tour_players_list:
            player = next((player for player in players_list if player['chess_id'] == chess_id), None)
            if player:
                player_instance = PlayerModel(**player)  # Création de l'instance du joueur
                instantiated_players.append(player_instance)  # Ajout de l'instance dans la liste
        return instantiated_players

    @classmethod
    def check_if_tourn_finished(cls, my_tournament):
        if my_tournament.finished_tour==True:
            my_tournament.end_date = datetime.today().strftime('%d/%m/%Y')
            ReportController.display_finished_tournament(my_tournament)
        else:
            pass
