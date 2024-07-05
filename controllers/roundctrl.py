from views.utilsviews import UtilsView
from views.roundviews import RoundView
from .matchctrl import MatchController
#from models.entity.matchmodel import MatchModel
from models.entity.roundmodel import Round
from datetime import datetime

class RoundController:
    """Contrôleur pour gérer les rounds d'un tournoi"""

    @classmethod
    def round_one_matches(cls, my_tournament, instantiated_players):
        """permet de créer les matchs du 1er round du tournoi et les sauvegarder
        Args:
            my_tournament (Tournament): Instance du tournoi en cours.
            instantiated_players (list of Player): Liste des joueurs instanciés prêts à concourir.
        Returns:
            tuple: Un tuple contenant le tournoi mis à jour et le round créé.
        """
        RoundView.roundheader()
        if int(my_tournament.current_round) == 1 and my_tournament.rounds_tour == []:
            matches = MatchController.make_round_one_matchs(instantiated_players)
            round1 = Round("Round 1", my_tournament.start_date, None, matches)
            #on va printer le round
            RoundView.roundprint(my_tournament, round1.to_dict())
            RoundController.round_one_results(my_tournament, instantiated_players, round1)
        elif int(my_tournament.current_round) == 1 and my_tournament.rounds_tour != []:
            matches = MatchController.instantiate_round_matchs_from_json(my_tournament.rounds_tour[0]['matches'], instantiated_players)
            round1 = Round("Round 1", my_tournament.start_date, None, matches)
            RoundView.roundprint(my_tournament, round1.to_dict())
            my_tournament, round1 = RoundController.round_get_results(my_tournament, round1)
        else:    
            print("le tournoi est déjà démarré veuillez...")
            print("erruer à gérer")
        return my_tournament, round1

    @classmethod
    def round_get_results(cls, my_tournament, _round):
        """permet de l'inscrire les résultats du round et les sauvegarder
        Args:
            mytournament (Tournament): Instance du tournoi en cours.
            _round (Round): Instance du round actuel dont on souhaite récupérer les résultats.
        Returns:
            tuple: Un tuple contenant le tournoi et le round mis à jour avec les résultats.
        """
        return_results = (f"{RoundView.round_winners_input()}")
        if return_results!='None':
            RoundController.round_results(_round, return_results)
            my_tournament.next_round()
            return my_tournament, _round
        else:
            return my_tournament, _round

    @classmethod
    def make_next_round(cls, my_tournament, instantiated_players):
        """permet de créer les rounds (n+1) avec classement par points
        Args:
            mytournament (Tournament): Instance du tournoi en cours.
            instantiated_players (list of Player): Liste des joueurs instanciés prêts à concourir.
        Returns:
            tuple: Un tuple contenant le round suivant et le tournoi mis à jour.
        """
        if 1 < int(my_tournament.current_round) <= int(my_tournament.rounds_nbr):
            # mappage des points des rounds précédents
            points_mapping = RoundController.create_points_mapping(my_tournament)
            # calcul des points actuels des instances de joueurs
            for player in instantiated_players:
                player_id = player.chess_id
                total_points = sum(points for points in points_mapping[player_id])
                player.points = int(total_points)
            matches = MatchController.make_next_round_matchs(instantiated_players, my_tournament)
            name = f"Round {my_tournament.current_round}"
            start_date = datetime.today().strftime('%d/%m/%Y')
            end_date = None
            round_next = Round(name, start_date, end_date, matches)
            RoundView.roundprint(my_tournament, round_next.to_dict())
            my_tournament, round_next = RoundController.round_get_results(my_tournament, round_next)
            return round_next, my_tournament

    @classmethod
    def create_points_mapping(cls, my_tournament):
        """créer un dictionnaire mappant les chess_id des joueurs à leurs 
        points accumulés au fil des rounds
        Args:
            mytournament (Tournament): Instance du tournoi pour laquelle on souhaite créer le mapping de points.
        Returns: dict: Dictionnaire mappant les chess_id aux points accumulés.
        """
        points_mapping = {}
        for _round in my_tournament.rounds_tour:
            if _round['matches'] is not None:
                for _match in _round['matches']:
                    for player_inf in _match:
                        chess_id, points = player_inf[0], int(player_inf[1])
                        if chess_id not in points_mapping:
                            points_mapping[chess_id] = []
                        points_mapping[chess_id].append(points)
        return points_mapping

    @classmethod
    def round_results(cls, _round, return_results):
        """permet de recueillir et traduire les résultats des matchs en points
        pour finaliser les infos d'un round
        Args:
            _round (Round): Instance du round dont on souhaite enregistrer les résultats.
            return_results (str): Résultats des matchs séparés par des virgules.
        Returns: Round: Le round mis à jour avec les scores et la date de fin.
        """
        try:
            matches_list = []
            for _match in _round.matches:
                matches_list.append(_match)
            results_list = [int(x) for x in return_results.split(',')]
            for index, _match in enumerate(matches_list):
                if _match.player_id2 != None:
                    winner = results_list[index]
                    _match.score_p1, _match.score_p2 = _match.set_result(winner)
                else:
                    winner = 1
                    _match.score_p1, _match.score_p2 = _match.set_result(winner)
            _round.end_date = datetime.today().strftime('%d/%m/%Y')
        except (ValueError, TypeError) as e:
            UtilsView.input_return_prints("choice_error")
        return _round

