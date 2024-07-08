from views.reportviews import ReportView
from views.utilsviews import UtilsView as UV
from models.manager.playermanager import PlayerCrud
from models.manager.tournamentmanager import TournamentCrud
from models.entity.roundmodel import Round
from models.entity.playermodel import PlayerModel
from models.entity.matchmodel import MatchModel


class ReportController:
    '''Contrôleur pour gérer les rapports accessibles à l'utilisateur.'''

    @classmethod
    def report_menu(cls):
        '''Permet à l'utilisateur d'afficher des rapports
        sur joueurs et tournois
        '''
        while True:
            try:
                choice = ReportView.display()
                match choice:
                    case "1":
                        cls.display_players()
                    case "2":
                        cls.display_tour_players()
                    case "3":
                        cls.display_alltournaments()
                    case "4":
                        cls.display_tournament_name_dates()
                    case "5":
                        cls.display_tournament_rounds_matches()
                    case "0":
                        break
                    case _:
                        UV.input_return_prints("choice_error")
            except (IndexError, ValueError, TypeError) as e:
                input(f"veuillez reprendre, erreur... {e} ")

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
        UV.input_return_prints("continue")

    @classmethod
    def display_tour_players(cls):
        '''permet l'affichage des joueurs inscrits à un tournoi donné
        par ordre alphabétique(nom de famille)
        '''
        cls.display_alltournaments()
        tournaments_list = TournamentCrud.get_all_tournaments()
        tournament_nbr = ReportView.tour_choice_input(len(tournaments_list))
        tournament = tournaments_list[tournament_nbr - 1]
        players = tournament['players_tour']
        if players == []:
            UV.input_return_prints("noplayer")
            pass
        else:
            header = ['lastname', 'firstname', 'birth_date', 'chess_id']
            rows = []
            for player in players:
                play_inf = PlayerCrud.get_player_inf_from__chess_id(player)
                rows.append(play_inf)
            sorted_rows = sorted(rows, key=lambda d: d[0])
            ReportView.display_players_list(sorted_rows, header)
            UV.input_return_prints("continue")

    @classmethod
    def display_alltournaments(cls, *args):
        '''permet l'affichage de tous les joueurs inscrits
        dans le fichier json
        '''
        tournaments_list_dict = TournamentCrud.get_all_tournaments()
        if len(args) != 0:
            if args[0] == "dummy switch rounds 2+":
                tournaments_list_dict = [
                    tour for tour in tournaments_list_dict
                    if int(tour['current_round']) >= 2]
            elif args[0] == "dummy switch rounds 1":
                tournaments_list_dict = [
                    tour for tour in tournaments_list_dict
                    if int(tour['current_round']) == 1]
        else:
            pass
        tournaments_list = []
        for tournament in tournaments_list_dict:
            tournament = {
                'tournament_id': tournament.pop('tournament_id'),
                **tournament}
            del tournament['rounds_tour']
            tournament['players_tour'] = len(tournament['players_tour'])
            tournaments_list.append(tournament)
        sorted_tournaments_list = sorted(tournaments_list,
                                         key=lambda d: d['tournament_id'])
        header = ['numéro du tournoi', 'nom', 'lieu', 'description',
                  'date de début', 'date de fin', 'round en cours',
                  'nombre de rounds', 'nombre de joueurs', 'tour fini ?']
        rows = [infos.values() for infos in sorted_tournaments_list]
        ReportView.display_tournaments_list(rows, header)

    @classmethod
    def display_tournament_name_dates(cls):
        '''permet l'affichage du nom et des dates d'un tournoi donné'''
        tournaments_list_dict = TournamentCrud.get_all_tournaments()
        tournaments_list = []
        for tournament in tournaments_list_dict:
            tournament = {'tournament_id': tournament.pop('tournament_id'),
                          'name': tournament['name'],
                          'start_date': tournament['start_date'],
                          'end_date': tournament['end_date']}
            tournaments_list.append(tournament)
        sorted_tournaments_list = sorted(tournaments_list,
                                         key=lambda d: d['tournament_id'])
        header = ['numéro du tournoi', 'nom', 'date de début', 'date de fin']
        rows = [infos.values() for infos in sorted_tournaments_list]
        ReportView.display_tournaments_list(rows, header)
        pass

    @classmethod
    def display_tournament_rounds_matches(cls):
        '''permet l'affichage des rounds et matches d'un tournoi donné'''
        cls.display_alltournaments()
        tournaments_list = TournamentCrud.get_all_tournaments()
        tournament_nbr = ReportView.tour_choice_input(len(tournaments_list))
        tournament = tournaments_list[tournament_nbr - 1]
        instantiated_players = []
        players_list = PlayerCrud.get_all_players()
        for chess_id in tournament['players_tour']:
            player = next((player for player in players_list
                           if player['chess_id'] == chess_id), None)
            if player:
                # Création de l'instance du joueur
                player_instance = PlayerModel(**player)
                # Ajout de l'instance dans la liste à renvoyer
                instantiated_players.append(player_instance)
        for index, _round in enumerate(tournament['rounds_tour']):
            matches = []
            for _match in _round['matches']:
                for player in instantiated_players:
                    if player.chess_id == _match[0][0]:
                        player1 = player
                    if player.chess_id == _match[1][0]:
                        player2 = player
                    if _match[1][0] == 'None':
                        player2 = None
                match_instance = MatchModel(
                    player1, _match[0][1], player2, _match[1][1])
                matches.append(match_instance)
            _round = Round(_round['name'], tournament['start_date'],
                           _round['end_date'], matches)
            round_dic = _round.to_dict()
            header = round_dic[0].keys()
            rows = [game.values() for game in round_dic]
            ReportView.display_matches_list(
               rows, header, _round.name,
               tournament['name'])
        pass

    @classmethod
    def display_finished_tournament(cls, my_tournament):
        """permet d'afficher les résultats d'un tournoi terminé
        """
        header = "tata"
        rows = "toto"
        # à revoir bien sûr
        ReportView.display_finished_tournament_players_list(
            rows, header, my_tournament.round_nbr, my_tournament.name,
            my_tournament.end_date, my_tournament.location)
