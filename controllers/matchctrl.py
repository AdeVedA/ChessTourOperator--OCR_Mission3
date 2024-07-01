from views.utilsviews import UtilsView
from views.reportviews import ReportView
from models.entity.matchmodel import MatchModel
import random


class MatchController:
    '''Contrôleur pour gérer les matchs d'un round.'''

    @classmethod
    def make_round_one_matchs(cls, instantiated_players):
        '''permet de créer les matchs du premier round et les renvoyer au RoundCtrl
        '''
        random.shuffle(instantiated_players)
        players = list(instantiated_players)
        pairs = []
        for i in range(0, len(players), 2):
            if i + 1 < len(players):
                pairs.append([players[i], players[i + 1]])
            else:
                pairs.append([players[i]], None)
        #on a nos paires (si nombre de joueurs impair, un joueur seul qui gagnera +1 point)
        #on va faire nos matchs
        round_matches = []    
        for pair in pairs :
            match_instance = MatchModel(pair[0].chess_id,"None",pair[1].chess_id,"None")
            round_matches.append(match_instance)
            #str(round for round in round_matches)
        return round_matches

    @classmethod
    def make_next_round_matchs(cls, instantiated_players):
        '''permet de créer les matchs des rounds n+1
        '''
