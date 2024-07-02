from views.utilsviews import UtilsView
from views.roundviews import RoundView
from .matchctrl import MatchController
from models.entity.matchmodel import MatchModel
from models.entity.roundmodel import Round


class RoundController:
    '''Contrôleur pour gérer les rounds d'un tournoi.'''


    @classmethod
    def round_progress(cls, my_tournament, instantiated_players):
        """permet de faire avancer le 1er round du tournoi et de retourner
        soit uniquement ses matchs, soit ses résultats
        """
        RoundView.roundheader()
        round1 = RoundController.make_round_one(my_tournament, instantiated_players)
        round_dict = round1.to_dict()
        RoundView.roundprint(my_tournament,round_dict)
        return_results = (f"{RoundView.round_winners_input(round_dict)}")
        if return_results!=None:
            RoundController.round_results(round1, return_results)
            my_tournament.next_round()
            return round1, my_tournament
        else:
            return round1, my_tournament

    @classmethod
    def make_round_one(cls, my_tournament, instantiated_players):
        '''permet de créer le premier round
        my_tournament = instance de tournoi
        instantiated_players = instances des joueurs du tournoi
        '''
        if int(my_tournament.current_round) == 1:
            #self.round_number = int(my_tournament.current_round)
            matches = MatchController.make_round_one_matchs(instantiated_players)
            #name = "Round 1"
            #start_date = my_tournament.start_date
            #end_date = None
            round1 = Round("Round 1", my_tournament.start_date, None, matches)
            return round1

            #pairs = [((i), (i + 1) % len(sorted_players_list)) for i in range(len(instantiated_players))]
            #if len(instantiated_players)%2
            #print(round_matches)
            #matches_list_dict = round_matches
            #header = matches_list_dict[0].keys()
            #rows = [game.values() for game in matches_list_dict]
            #ReportView.display_matches_list(rows, header)
        else:
            round_next = RoundController.make_next_round(my_tournament, instantiated_players)
            return round_next

    @classmethod
    def make_next_round(cls, my_tournament, instantiated_players):
        '''permet de créer les rounds (n+1) avec classement par points'''
        if 1 < int(my_tournament.current_round) <= int(my_tournament.rounds_nbr):
            matches = MatchController.make_next_round_matchs(instantiated_players, my_tournament)
            name = f"Round {my_tournament.current_round}"
            start_date = datetime.today().strftime('%d-%m-%Y %H:%M')
            end_date = None
            round_next = Round(name, start_date, end_date, matches)
            return round_next

    @classmethod
    def round_results(cls, round1, return_results):
        """permet de recueillir et traduire les résultats des matchs pour
        finaliser un round (avec calcul des points)
        """
        try:
            matches_list = []
            for _match in round1.matches:
                matches_list.append(_match)
            results_list = [int(x) for x in return_results.split(',')]
            for index, _match in enumerate(matches_list):
                if _match.player_id2 != None:
                    winner = results_list[index]
                    _match.score_p1, _match.score_p2 = _match.set_result(winner)
                else:
                    winner = 1
                    _match.score_p1, _match.score_p2 = _match.set_result(winner)
        except (ValueError, TypeError) as e:
            UtilsView.input_return_prints("choice_error")
        return round1
        