from views.utilsviews import UtilsView
from .matchctrl import MatchController
from models.entity.roundmodel import Round

class RoundController:
    '''Contrôleur pour gérer les rounds d'un tournoi.'''


    @classmethod
    def round_progress(cls, my_tournament, instantiated_players):
        header = "@  Rounds de votre Tournoi  @"
        menu_options = []
        UtilsView.menu(header, menu_options)
        round1 = RoundController.make_round_one(my_tournament, instantiated_players)
        return round1
        
    @classmethod
    def make_round_one(cls, my_tournament, instantiated_players):
        '''permet de créer le premier round
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
        else:
            round_next = RoundController.make_next_round(my_tournament, instantiated_players)

    @classmethod
    def make_next_round(cls, my_tournament, instantiated_players):
        '''permet de créer les rounds (n+1) avec classement par points'''
        matchs = MatchController.make_next_round_matchs(instantiated_players)


    @classmethod   
    def make_round_one_pairs(cls):
        """Permet d'appairer les joueurs au hasard lors du premier round
        """
        
        