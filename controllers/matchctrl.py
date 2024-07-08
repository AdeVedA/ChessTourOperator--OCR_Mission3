from models.entity.matchmodel import MatchModel
import random


class MatchController:
    '''Contrôleur pour gérer les matchs d'un round.'''

    @classmethod
    def make_round_one_matchs(cls, instantiated_players):
        '''permet de créer les matchs du premier round
        et les renvoyer au RoundCtrl
        '''
        random.shuffle(instantiated_players)
        players = list(instantiated_players)
        pairs = []
        for i in range(0, len(players), 2):
            if i + 1 < len(players):
                pairs.append([players[i], players[i + 1]])
            else:
                pairs.append([players[i], None])
        # on a nos paires (si nombre de joueurs impair,
        # un joueur seul qui gagnera +1 point)
        # on va faire nos matchs
        round_matches = []
        for pair in pairs:
            match_instance = MatchModel(
                pair[0].chess_id, "None",
                pair[1].chess_id if pair[1] else None, "None")
            round_matches.append(match_instance)
        return round_matches

    @classmethod
    def instantiate_round_matchs_from_json(cls, round_matches,
                                           instantiated_players):
        instantiated_matchs_list = []
        for _match in round_matches:
            for player in instantiated_players:
                if player.chess_id == _match[0][0]:
                    player1 = player
                if player.chess_id == _match[1][0]:
                    player2 = player
                if _match[1][0] == 'None':
                    player2 = None
            match_instance = MatchModel(
                player1, _match[0][1], player2, _match[1][1])
            instantiated_matchs_list.append(match_instance)
        return instantiated_matchs_list

    @classmethod
    def make_next_round_matchs(cls, instantiated_players, my_tournament):
        """permet de créer les matchs des rounds n+1 avec appairage
        selon les points (classement) et joueurs précédemment
        rencontrés (à éviter au maximum)
        """
        sorted_players = sorted(
            instantiated_players,
            key=lambda d: d.points, reverse=True)
        next_round_matches = []
        played_against = cls.get_played_against(my_tournament)
        for player in sorted_players:
            player_id = player.chess_id
            if player_id not in played_against:
                played_against[player_id] = set()
            opponent = None
            # Trouver un "opponent"
            if len(sorted_players) > 1:
                for potential_opponent in sorted_players:
                    potential_opponent_id = potential_opponent.chess_id
                    # Trouver un "opponent" non joué pour le joueur "player"
                    if potential_opponent_id != player_id and \
                            potential_opponent_id not in \
                            played_against[player_id]:
                        opponent = potential_opponent
                        break
                    # sinon rejouer un match existant.
                    elif potential_opponent_id in played_against[player_id]:
                        next_round_matches.append(
                            MatchModel(player, "None",
                                       sorted_players[1], "None"))
                        sorted_players.remove(player)
                        sorted_players.remove(sorted_players[0])
                        break
                # Si un adversaire est trouvé, on crée le match et
                # on enlève ces joueurs de la liste
            if opponent:
                next_round_matches.append(
                    MatchModel(player, None, opponent, None))
                sorted_players.remove(player)
                sorted_players.remove(opponent)
                opponent = None
            # Si aucun nouvel adversaire valide n'est trouvé,
            # s'il est tout seul=>match factice
        if len(sorted_players) == 1:
            next_round_matches.append(
                    MatchModel(sorted_players[0], "None", None, 0))
            sorted_players.remove(sorted_players[0])
        return next_round_matches

    @classmethod
    def get_played_against(cls, my_tournament):
        """crée un dictionnaire played_against avec
        pour clé : chess_id des joueurs
        pour valeurs : liste des chess_ids que chaque clé-joueur a déjà joués
        """
        played_against = {}
        # Parcourir tous les tours terminés pour remplir
        # le dictionnaire "played_against"
        for _round in my_tournament.rounds_tour:
            for match in _round['matches']:
                player1, player2 = match[0][0], match[1][0]
                if player1 not in played_against:
                    played_against[player1] = set()
                if player2 not in played_against:
                    played_against[player2] = set()
                played_against[player1].add(player2)
                played_against[player2].add(player1)
        return played_against
