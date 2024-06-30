from views.utilsviews import UtilsView
from views.roundviews import RoundView
from .matchctrl import MatchController
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
        else:
            return round1
        
    @classmethod
    def make_round_one(cls, my_tournament, instantiated_players):
        '''permet de créer le premier round
        my_tournament = instance de tournoi
        instantiated_players = instances des joueurs du tournoi
        '''
        if int(my_tournament.current_round) == 1:
            #self.round_number = int(my_tournament.current_round)
            matches = MatchController.make_round_one_matchs(instantiated_players)
            name = "Round 1"
            start_date = my_tournament.start_date
            end_date = None
            round1 = Round("Round 1", my_tournament.start_date, None, matches)
            return round1

            #players = range(1,len(instantiated_players)+1)
            #pairs = [((i), (i + 1) % len(sorted_players_list)) for i in range(len(instantiated_players))]
            #if len(instantiated_players)%2
            #print(round_matches)
            #matches_list_dict = round_matches
            #header = matches_list_dict[0].keys()
            #rows = [game.values() for game in matches_list_dict]
            #ReportView.display_matches_list(rows, header)
        else:
            round_next = RoundController.make_next_round(my_tournament, instantiated_players)

    @classmethod
    def round_results(cls, round1, return_results):
        #en cours d'implémentation
        """permet de recueillir et traduire les résultats des matchs pour
        finaliser un round (avec calcul des points)
        """
        selected_winners = []
        while not selected_winners:
            try:
                numbers = [int(n) for n in return_results.split(',')]
                winners_sel = []
                for number in numbers:
                    #à préciser/indexer
                    player_chess_id = players_list[number]['chess_id']
                    winners_sel.append(player_chess_id)
                
                selected_winners = sdf
                print(selected_winners) 
            except (ValueError, TypeError):
                UtilsView.input_return_prints("choice_error")
        return round1

    @classmethod
    def make_next_round(cls, my_tournament, instantiated_players):
        '''permet de créer les rounds (n+1) avec classement par points'''
        matchs = MatchController.make_next_round_matchs(instantiated_players)


    @classmethod   
    def make_round_one_pairs(cls):
        """Permet d'appairer les joueurs au hasard lors du premier round
        """
        
        