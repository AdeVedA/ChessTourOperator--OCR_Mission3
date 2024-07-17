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
                input(f"Veuillez reprendre, erreur... {e} ")

    @classmethod
    def display_players(cls):
        '''permet l'affichage de tous les joueurs inscrits dans le fichier JSON
        classés par nom de famille
        '''
        players_list = PlayerCrud.get_all_players()
        for pl_dict in players_list:
            pl_dict.pop('points', None)
        # on classe la liste de dictionnaires de joueurs par Nom de famille
        sorted_players_list = sorted(players_list,
                                     key=lambda d: d['lastname'])
        header = sorted_players_list[0].keys()
        rows = [player.values() for player in sorted_players_list]
        ReportView.display_players_list(rows, header)
        UV.input_return_prints("continue")

    @classmethod
    def display_tour_players(cls):
        '''permet l'affichage des joueurs (par ordre alphabétique - nom de
        famille) inscrits à un tournoi particulier choisi par l'utilisateur
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
    def display_alltournaments(cls, firstrounds=False):
        '''permet l'affichage de tous les tournois inscrits
        dans les fichiers JSON de tournois
        '''
        tournaments_list_dict = TournamentCrud.get_all_tournaments()
        # c'est sale, mais le "château de cartes" est devenu fragile...
        tours_to_display = [dict(tour) for tour in tournaments_list_dict]
        tournaments_list = []
        for tournament in tours_to_display:
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
        return tournaments_list_dict

    @classmethod
    def display_tournaments_if(cls, firstrounds=False):
        '''permet l'affichage de tous les tournois qui en sont au
        1er round ou aux suivants (parmi les fichiers JSON de tournois)
        '''
        tournaments_list_dict = TournamentCrud.get_all_tournaments()
        if firstrounds is False:
            tournaments_list_dict = [
                tour for tour in tournaments_list_dict
                if int(tour['current_round']) >= 2
                and tour['finished_tour'] is False]
        elif firstrounds is True:
            tournaments_list_dict = [
                tour for tour in tournaments_list_dict
                if int(tour['current_round']) == 1]
        if len(tournaments_list_dict) == 0:
            UV.input_return_prints("notournament")
        # c'est sale, mais le "château de cartes" est devenu fragile...
        tours_to_display = [dict(tour) for tour in tournaments_list_dict]
        tournaments_list = []
        for tournament in tours_to_display:
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
        return tournaments_list_dict

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

    @classmethod
    def display_tournament_rounds_matches(cls):
        '''permet l'affichage des rounds et matches d'un tournoi donné,
        s'il est terminé cela affiche aussi les résultats (classement) des
        joueurs.
        rem: ce n'est pas la plus propre des méthodes, bloqué par la rencontre
        entre mon ignorance du MVC et l'impossibilité des imports circulaires
        '''
        cls.display_alltournaments()
        tournaments_list = TournamentCrud.get_all_tournaments()
        tournament_nbr = ReportView.tour_choice_input(len(tournaments_list))
        tournament = tournaments_list[tournament_nbr - 1]
        if tournament['rounds_tour'] != []:
            pass
        else:
            return UV.input_return_prints("noround")
        my_players = []
        players_list = PlayerCrud.get_all_players()
        for chess_id in tournament['players_tour']:
            player = next((player for player in players_list
                           if player['chess_id'] == chess_id), None)
            if player:
                # Création de l'instance du joueur
                player_instance = PlayerModel(**player)
                # Ajout de l'instance dans la liste à renvoyer
                my_players.append(player_instance)
        points_mapping = {}
        for index, _round in enumerate(tournament['rounds_tour']):
            matches = []
            for _match in _round['matches']:
                for player in my_players:
                    if player.chess_id == _match[0][0]:
                        player1 = player
                    if player.chess_id == _match[1][0]:
                        player2 = player
                    if _match[1][0] == 'None':
                        player2 = None
                match_instance = MatchModel(
                    player1, _match[0][1], player2, _match[1][1])
                matches.append(match_instance)
                # calcul des points au passage
                # de la boucle des matchs des rounds
                for player_inf in _match:
                    chess_id, points = player_inf[0], player_inf[1]
                    if chess_id not in points_mapping:
                        points_mapping[chess_id] = []
                    points_mapping[chess_id].append(points)
            round_obj = Round(_round['name'], tournament['start_date'],
                              _round['end_date'], matches)
            round_dic = round_obj.to_dict_results()
            header = round_dic[0].keys()
            rows = [game.values() for game in round_dic]
            # print du tableau du round
            ReportView.display_matches_list(
               rows, header, round_obj.name[6],
               tournament['name'])
        # calcul des points
        for player in my_players:
            total_points = sum(points for
                               points in points_mapping[player.chess_id])
            player.points = total_points
        # Affichage du tableau de classement des joueurs pour le tournoi
        if tournament['finished_tour'] is not False:
            ReportController.display_finished_tournament(tournament,
                                                         my_players,
                                                         report_menu=True)
        UV.input_return_prints("continue")

    @classmethod
    def display_finished_tournament(cls, my_tournament, my_players,
                                    report_menu=False):
        """permet d'afficher les résultats d'un tournoi terminé
        """
        sorted_players = sorted(
            my_players,
            key=lambda d: d.points, reverse=True)
        rows = []
        for player in sorted_players:
            player_inf = [player.lastname, player.firstname,
                          player.chess_id, player.points]
            rows.append(player_inf)
        header = ['lastname', 'firstname', 'chess_id', 'points']
        if report_menu is False:
            ReportView.display_finished_tournament_players_list(
                rows, header, my_tournament.rounds_nbr, my_tournament.name,
                my_tournament.end_date, my_tournament.location)
        else:
            ReportView.display_finished_tournament_players_list(
                rows, header, my_tournament['rounds_nbr'],
                my_tournament['name'],
                my_tournament['end_date'], my_tournament['location'])
