from models.entity.matchmodel import MatchModel
import random


class MatchController:
    '''Contrôleur pour gérer les matchs d'un round.'''

    @classmethod
    def make_round_one_matchs(cls, my_players):
        '''permet de mélanger au hasard les joueurs,
        créer les matchs du premier round
        et les renvoyer au RoundCtrl
        '''
        # on mélange
        random.shuffle(my_players)
        players = list(my_players)
        # on prépare nos paires
        pairs = []
        # on prend les joueurs par 2, 1&2 3&4 etc 
        for i in range(0, len(players), 2):
            if i + 1 < len(players):
                pairs.append([players[i], players[i + 1]])
            # et le dernier joueur impair dont le joueur[i+1] n'existe pas
            else:
                pairs.append([players[i], None])
        # on a nos paires
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
                                           my_players):
        """Créer des instances de "MatchModel" à partir d'une liste de matches
        et de joueurs. Si aucun adversaire n'est trouvé, l'adversaire est None
        Args:
            round_matches : liste de matches pour un round particulier
            my_players : liste d'instances PlayerModel
        Returns:
            liste d'instances de "MatchModel"
        """
        instantiated_matchs_list = []
        for _match in round_matches:
            for player in my_players:
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
    def make_next_round_matchs(cls, my_players, my_tournament):
        """permet de retourner les matchs des rounds n+1 avec appairage
        selon les points (classement sorted_players), selon les joueurs
        précédemment rencontrés (à éviter au maximum), selon si joueur seul
        Args:
            my_tournament : Instance du tournoi en cours
            my_players : Liste des joueurs instanciés du tournoi
        Returns:
            next_round_matches : liste des matchs instanciés du prochain round
        """
        sorted_players = sorted(
            my_players, key=lambda d: d.points, reverse=True)
        # Initialisation de la liste à retourner
        next_round_matches = []
        # paired_players listera les joueurs déjà appairés.
        paired_players = []
        # played_against est le dictionnaire de joueurs déjà joués
        played_against = cls.get_played_against(my_tournament)
        for player in sorted_players:
            player_id = player.chess_id
            if player_id in paired_players:
                continue
            if player_id not in played_against:
                played_against[player_id] = set()
            # on enregistre le chess_id du joueur dans
            # paired_players pour l'exclure totalement
            paired_players.append(player_id)
            opponent = None
            potential_opponents = []
            # Trouver un adversaire potentiel, en excluant le joueur
            # et ceux déjà appairés pour ce round
            potential_opponents = [
                    available_player for available_player in sorted_players
                    if available_player.chess_id not in paired_players]
            if len(potential_opponents) >= 1:
                for potential_opponent in potential_opponents:
                    potential_opponent_id = potential_opponent.chess_id
                    # Trouver un opponent "non joué" pour le "player"
                    if potential_opponent_id not in played_against[player_id]:
                        opponent = potential_opponent
                        break
                    else:
                        continue
                # Si un adversaire est trouvé, on crée le match
                if opponent:
                    paired_players.append(opponent.chess_id)
                    next_round_matches.append(
                        MatchModel(player, None, opponent, None))
                    opponent = None
                # sinon rejouer un match existant
                else:
                    opponent = potential_opponents[0]
                    paired_players.append(opponent.chess_id)
                    next_round_matches.append(
                        MatchModel(player, None, opponent, None))
                    opponent = None
            # Si aucun nouvel adversaire valide n'est trouvé,
            # s'il est tout seul=>match factice
            elif len(sorted_players) % 2 != 0:
                next_round_matches.append(
                        MatchModel(player, None, None, 0))
        return next_round_matches

    @classmethod
    def get_played_against(cls, my_tournament):
        """à partir de l'instance tournoi my_tournament, retourne un
        dictionnaire "joueur:adversaires déjà joués" avec
        pour clé : chess_id des joueurs
        pour valeurs : liste des chess_ids que chaque clé-joueur a déjà joués
        pour appairage de match
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
