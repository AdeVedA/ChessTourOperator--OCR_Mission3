import datetime
import random
from .matchesmodel import MatchModel

class Round:

    def __init__(self, round_number, matches=[]):
        self.round_number = round_number
        self.matches = matches
        

    def make_round_one(self, my_tournament, instantiated_players):
        #
        # un pti roundmanager plutôt ?
        #
        '''permet de créer le premier round, en attendant de dispatcher la fonction en bonne place dans le MVC ;)
        et de faire le ménage aussi hihi
        '''
        if int(my_tournament.current_round) == 1:
            self.round_number = int(my_tournament.current_round)
            random.shuffle(instantiated_players)
            pairs = []
            players = list(instantiated_players)
            for i in range(0, len(players), 2):
                if i + 1 < len(players):
                    pairs.append([players[i], players[i + 1]])
                else:
                    # Si le nombre de joueurs est impair, on peut ajouter un joueur sans partenaire (faudra gérer ensuite...et +1point)
                    pairs.append([players[i]])
            tour_matches = []
            print(f"\nLes matchs de ce round {self.round_number} :\n")
            for pair in pairs :
                player_id1 = f"{pair[0].firstname} {pair[0].lastname} (chessID {pair[0].chess_id})"
                player_id2 = f"{pair[1].firstname} {pair[1].lastname} (chessID {pair[1].chess_id})"
                print(f"           {player_id1}     à     {player_id2}\n")
                match_instance = MatchModel(pair[0],pair[1])
                tour_matches.append(match_instance)
            round1 = Round(my_tournament.current_round, tour_matches)
            return round1
            #players = range(1,len(instantiated_players)+1)
            #pairs = [((i), (i + 1) % len(sorted_players_list)) for i in range(len(instantiated_players))]
            #if len(instantiated_players)%2
        else:
            round_next = self(my_tournament.current_round).make_next_round(my_tournament, instantiated_players)

        '''sauvegarde du round au propre dans le json avec résultat None = pas joué
        affichage des matchs au propre (UtilsView...)
        affichage menu d'input des résultats avec (1,2,0) (UtilsV)
        enregistrement résultats
        calcul des points
        nouveau round ?:
        appairement des joueurs selon points + requête "déjà joué"/sauvegarde
        affichage des matchs
        nouveau round ? ou fin :
        si fin de tournoi, affichage du classement/points des joueurs
        revoir les rapports
        flake8...
        readme...
        powerp
        '''
class Round_next(Round):

    def __init__(self, round_number, matches=[]):
        self.round_number = round_number
        self.matches = matches


    def make_next_round(self, my_tournament, instantiated_players):
        '''permet de créer les rounds (n+1) avec classement par points'''