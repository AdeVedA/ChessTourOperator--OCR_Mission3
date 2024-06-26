from views.tournamentviews import TournamentView
from views.utilsviews import UtilsView
from models.entity.tournamentmodel import TournamentModel
from models.manager.tournamentmanager import TournamentCrud
from models.entity.playermodel import PlayerModel
from models.manager.playermanager import PlayerCrud
from models.entity.roundmodel import Round
from .reportsctrl import ReportController

class TournamentController:

    #def __init__(self):
    #    '''Contrôleur pour gérer les tournois.'''

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
        '''Permet de créer un tournoi'''
        tour_infos = TournamentView.tournament_infos()
        tournament = TournamentModel(**tour_infos)
        tournaments_list = TournamentCrud.get_all_tournaments()
        TournamentCrud().save_new_tournament(tournament)
        UtilsView.input_return_prints("tournament_reg")
        return

    @classmethod
    def start_tournament_menu(cls):
        #
        #BORDEL: scinder en fonctions réutilisables, déplacer vers tournamentviews ou  ce qui touche à la vue
        #
        '''Permet de démarrer un tournoi en choisissant le tournoi et en sélectionnant les joueurs'''
        header = "@  Démarrage d'un Tournoi  @"
        menu_options = []
        UtilsView.menu(header, menu_options)
        ReportController.display_alltournaments()
        tournaments_list = TournamentCrud.get_all_tournaments()
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
        
        if selected_tournament['players_tour'] == []:
            UtilsView.input_return_prints("tournament_select", 
                                          **selected_tournament)
            tournament_add_players(selected_tournament)
            my_tournament = TournamentModel(**selected_tournament)
            # maintenant il faut sauvegarder l'état du tournoi et passer à la suite (round.robin)etc
        else :
            my_tournament = TournamentModel(**selected_tournament)
            UtilsView.input_return_prints("tournament_select", 
                                          **selected_tournament)
        TournamentCrud.update_tournament(my_tournament)
        tour_players_list = my_tournament.players_tour
        instantiated_players = TournamentController.instantiate_tournament_players(tour_players_list)
        round1 = Round(my_tournament.current_round).make_round_one(my_tournament, instantiated_players)
        
        my_tournament.rounds_tour.append([round1.round_number, [round1.matches]]) #FOIREUX !!!! à revoir !!!
        TournamentCrud.update_tournament(my_tournament)
                
    @classmethod    
    def tournament_add_players(cls, selected_tournament):
        '''permet d'inscrire des joueurs (enregistrés dans le fichier 
        players.json) à un tournoi
        '''
        ReportController.display_players()
        selected_players = []
        while not selected_players:
            try:
                max_player_id = PlayerCrud().get_max_player_id()
                players_id_tour_inpt = (f"{TournamentView.players_choice(max_player_id)}")
                numbers = [int(n) - 1 for n in players_id_tour_inpt.split(',')]
                players_list = PlayerCrud().get_all_players()
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
        args : tour_players_list = la liste de joueurs de l'instance "my_tournament" (attribut .players_tour)
        '''
        instantiated_players = []
        players_list = PlayerCrud().get_all_players() 
        for chess_id in tour_players_list:
            player = next((player for player in players_list if player['chess_id'] == chess_id), None)
            if player:
                player_instance = PlayerModel(**player)  # Création de l'instance du joueur
                instantiated_players.append(player_instance)  # Ajout de l'instance dans la liste
        return instantiated_players
            
        
    def resume_tournament_menu():
        '''Permet de reprendre un tournoi inachevé'''
        print("implémentation en cours")
        pass
    
    def choose_tournament():
        '''permet de choisir un tournoi dans la liste des tournois
        et de l'instancier
        '''
        ReportController.display_alltournaments()
        chosen_tournament = TournamentView.tournament_choice

        