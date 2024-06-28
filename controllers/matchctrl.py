from views.utilsviews import UtilsView
from views.reportviews import ReportView
from models.entity.matchmodel import MatchModel
import random


class MatchController:
    '''Contrôleur pour gérer les matchs d'un round.'''

    @classmethod
    def make_round_one_matchs(cls, instantiated_players):
        '''permet de créer les matchs du premier round
        '''
        random.shuffle(instantiated_players)
        players = list(instantiated_players)
        pairs = []
        for i in range(0, len(players), 2):
            if i + 1 < len(players):
                pairs.append([players[i], players[i + 1]])
            else:
                # Si le nombre de joueurs est impair, on peut ajouter un joueur sans partenaire (faudra gérer ensuite...et +1point)
                pairs.append([players[i]])
        #on a nos paires (et, si nombre de joueurs impair, un joueur seul qui gagnera +1 point)
        #on va faire nos matchs
        round_matches = []    
        for pair in pairs :
            #player_id1 = f"{pair[0].firstname} {pair[0].lastname} (chessID {pair[0].chess_id})"
            #player_id2 = f"{pair[1].firstname} {pair[1].lastname} (chessID {pair[1].chess_id})"
            # à fourrer dans la vue
            #print(f"\nLes matchs de ce premier round :\n")
            #print(f"           {player_id1}     à     {player_id2}\n")
            match_instance = MatchModel(pair[0],pair[1],"None","None")
            round_matches.append(match_instance)
            #str(round for round in round_matches)
        matches_list_dict = MatchModel.to_dict(round_matches)
        header = matches_list_dict[0].keys()
        rows = [game.values() for game in matches_list_dict]
        ReportView.display_matches_list(rows, header)

    @classmethod
    def make_next_round_matchs(cls, instantiated_players):
        '''permet de créer les matchs des rounds n+1
        '''
