from views.reportviews import ReportView
from views.utilsviews import UtilsView
from models.manager.playermanager import PlayerCrud
from models.manager.tournamentmanager import TournamentCrud


class ReportController:
    '''Contrôleur pour gérer les rapports accessibles à l'utilisateur.'''

    @classmethod
    def report_menu(cls):
        '''Permet à l'utilisateur d'afficher un des rapports sur joueurs et tournois'''
        while True:
            choice = ReportView.display()
            match choice:
                case "1":
                    ReportController.display_players()
                case "2":
                    ReportController.display_tour_players()
                case "3":
                    ReportController.display_alltournaments()
                case "4":
                    ReportController.display_tournament_name_dates()
                case "5":
                    ReportController.display_tournament_rounds_matches()
                case "0":
                    break
                case _:
                    UtilsView.input_return_prints("choice_error")

    @classmethod
    def display_players(cls):
        '''permet l'affichage de tous les joueurs inscrits dans le fichier json
        classés par nom de famille
        '''
        players_list = PlayerCrud.get_all_players()
        sorted_players_list = sorted(players_list,
                                         key=lambda d: d['lastname'])
        header = sorted_players_list[0].keys()
        rows = [infos.values() for infos in sorted_players_list]
        ReportView.display_players_list(rows, header)
        UtilsView.input_return_prints("continue")

    @classmethod
    def display_tour_players(cls, tournament):
        '''permet l'affichage des joueurs inscrits à un tournoi donné'''
        print("implémentation en cours")
        pass

    @classmethod
    def display_alltournaments(cls):
        '''permet l'affichage de tous les joueurs inscrits dans le fichier json'''
        tournaments_list_dict = TournamentCrud().get_all_tournaments()
        tournaments_list = []
        for tournament in tournaments_list_dict:
            tournament = {'tournament_id': tournament.pop('tournament_id'), **tournament}
            tournaments_list.append(tournament)
        sorted_tournaments_list = sorted(tournaments_list,
                                         key=lambda d: d['tournament_id'])
        header = sorted_tournaments_list[0].keys()
        rows = [infos.values() for infos in sorted_tournaments_list]
        ReportView.display_tournaments_list(rows, header)

    @classmethod
    def display_tournament_name_dates(cls):
        '''permet l'affichage du nom et des dates d'un tournoi donné'''
        print("implémentation en cours")
        pass

    @classmethod
    def display_tournament_rounds_matches(cls):
        '''permet l'affichage des rounds et matches d'un tournoi donné'''
        print("implémentation en cours")
        pass

