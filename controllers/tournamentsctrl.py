from views.tournamentviews import TournamentView
from views.utilsviews import UtilsView as UV
from models.entity.tournamentmodel import TournamentModel
from models.manager.tournamentmanager import TournamentCrud
from models.entity.playermodel import PlayerModel
from models.manager.playermanager import PlayerCrud
from .roundctrl import RoundController
from .reportsctrl import ReportController
from datetime import datetime


class TournamentController:
    """Contrôleur pour gérer les tournois"""

    @classmethod
    def tournament_menu(cls):
        """Permet à l'utilisateur de lancer une des fonctions
        de gestion de tournois"""
        while True:
            try:
                choice = TournamentView.display()
                match choice:
                    case "1":
                        cls.create_tournament()
                    case "2":
                        cls.start_tournament_menu()
                    case "3":
                        cls.resume_tournament_menu()
                    case "0":
                        break
                    case _:
                        UV.input_return_prints("choice_error")
            except (IndexError):
                input("Veuillez reprendre, vous avez probablement demandé"
                      " à commencer un tournoi alors qu'aucun de vos "
                      "tournois n'en est au round 1...")
            except (ValueError, TypeError) as e:
                input(f"Veuillez reprendre, erreur... {e}")

    @classmethod
    def create_tournament(cls):
        """Permet de créer une matrice de tournoi (sans joueurs)
        Collecte les informations du tournoi via TournamentView,
        crée un objet TournamentModel avec ces infos
        et sauvegarde le nouveau tournoi.
        """
        tour_infos = TournamentView.tournament_infos()
        tournament = TournamentModel(**tour_infos)
        TournamentCrud.save_new_tournament(tournament)
        UV.input_return_prints("tournament_reg")

    @classmethod
    def start_tournament_menu(cls):
        """Permet de démarrer un tournoi en choisissant le tournoi
        et en sélectionnant les joueurs qui y joueront.
        instancie les joueurs sélectionnés, le tournoi, crée le 1er round,
        vérifie si le tournoi est terminé (tournoi avec un seul round)
        et sauvegarde le tournoi en l'état.
        """
        # selection du tournoi
        TournamentView.start_tournament_header()
        selected_tournament = cls.choose_tournament(firstrounds=True)
        UV.input_return_prints("tournament_select",
                               **selected_tournament)
        # si aucun joueur enregistré, inscription des joueurs au tournoi,
        # on instancie et on sauve
        if selected_tournament['players_tour'] == []:
            cls.tournament_add_players(selected_tournament)
            my_tournament = TournamentModel(**selected_tournament)
            TournamentCrud.update_tournament_players(my_tournament)
        # sinon si il y a déjà des joueurs on instancie le tournoi
        else:
            my_tournament = TournamentModel(**selected_tournament)
        # on instancie les joueurs du tournoi
        my_players = cls.instantiate_tournament_players(
                                my_tournament.players_tour)
        # on va créer le round 1 de ce tournoi et
        # inscrire les matchs ou les résultats aussi
        my_tournament, round1 = RoundController.round_one_matches(
                                my_tournament, my_players)
        # on sauvegarde
        cls.check_if_tourn_finished(my_tournament, my_players)
        my_tournament = TournamentCrud.update_tournament(my_tournament, round1)

    @classmethod
    def resume_tournament_menu(cls):
        """Procédure permettant de reprendre un tournoi inachevé (sélection/
        instanciation) et d'instancier les joueurs et envoie ceux-ci
        à une méthode qui propose de faire avancer le tournoi
        """
        # selection du tournoi
        TournamentView.resume_tournament_header()
        selected_tournament = cls.choose_tournament()
        # instanciation du tournoi
        my_tournament = TournamentModel(**selected_tournament)
        UV.input_return_prints("tournament_select",
                               **selected_tournament)
        # on instancie les joueurs du tournoi
        my_players = cls.instantiate_tournament_players(
                                my_tournament.players_tour)
        cls.progress_tournament(my_tournament, my_players)

    @classmethod
    def progress_tournament(cls, my_tournament, my_players):
        """méthode qui lance la création du prochain round, vérifie si le
        tournoi est terminé, sauvegarde l'état actuel du tournoi et propose
        de continuer les rounds immédiatement, ou pas
        """
        while True:

            round_next, my_tournament = RoundController.make_next_round(
                                my_tournament, my_players)
            my_tournament = TournamentCrud.update_tournament(
                                my_tournament, round_next)
            my_tournament = cls.check_if_tourn_finished(
                my_tournament, my_players)
            if my_tournament.finished_tour is not True:
                choice = TournamentView.continue_tour()
                if choice == 2:
                    break
            else:
                TournamentCrud.update_tournament(my_tournament, round_next)
                break

    @classmethod
    def choose_tournament(cls, firstrounds=False):
        """permet de demander l'affichage d'une liste des tournois
        Args:
            *args: Argument optionnel pour l'affichage des tournois
                où les rounds >1.
        Returns:
            dict: Le dictionnaire représentant le tournoi sélectionné
        """
        tournaments_list = TournamentCrud.get_all_tournaments()
        ReportController.display_tournaments_if(firstrounds)
        selected_tournament = cls.select_tournament(tournaments_list,
                                                    firstrounds)
        return selected_tournament

    @classmethod
    def select_tournament(cls, tournaments_list, firstrounds):
        """Permet de sélectionner un tournoi parmi une liste de tournois.
        Args:
            tournaments_list : Liste des dictionnaires représentant
                les tournois disponibles.
        Returns:
            dict: Le dictionnaire représentant le tournoi sélectionné
        """
        selected_tournament = None
        tourn_ids_list = [tour['tournament_id'] for tour in tournaments_list]
        while not selected_tournament:
            tournament_id_inpt = int(
                TournamentView.tournament_choice(tourn_ids_list,
                                                 firstrounds)) - 1
            selected_tournament = tournaments_list[tournament_id_inpt]
        return selected_tournament

    @classmethod
    def tournament_add_players(cls, selected_tournament):
        """permet d'inscrire des joueurs (de players.json) à un tournoi
        Args: selected_tournament (dict): Dictionnaire représentant
            le tournoi sélectionné.
        """
        ReportController.display_players()
        selected_players = []
        while not selected_players:
            try:
                max_player_id = PlayerCrud.get_max_player_id()
                players_id_tour_inpt = (
                        f"{TournamentView.players_choice(max_player_id)}")
                numbers = [int(n) - 1 for n in players_id_tour_inpt.split(',')]
                players_list = PlayerCrud.get_all_players()
                players_sel = []
                for number in numbers:
                    player_chess_id = players_list[number]['chess_id']
                    players_sel.append(player_chess_id)
                selected_tournament['players_tour'] = players_sel
                selected_players = selected_tournament['players_tour']
                for player in selected_players:
                    UV.style_print(
                        " - " + PlayerCrud.get_player_name(player))
                UV.input_return_prints("continue")
            except (ValueError, TypeError):
                UV.input_return_prints("choice_error")

    @classmethod
    def instantiate_tournament_players(cls, tour_players_list):
        """permet d'instancier tous les joueurs d'un tournoi
        Args : tour_players_list = liste des joueurs de l'instance
            "my_tournament" (attribut .players_tour)
        Returns: Liste des instances PlayerModel des joueurs du tournoi.
        """
        my_players = []
        players_list = PlayerCrud.get_all_players()
        for chess_id in tour_players_list:
            player = next((player for player in players_list
                           if player['chess_id'] == chess_id), None)
            if player:
                # Création de l'instance du joueur
                player_instance = PlayerModel(**player)
                # Ajout de l'instance dans la liste à renvoyer
                my_players.append(player_instance)
        return my_players

    @classmethod
    def check_if_tourn_finished(cls, my_tournament, my_players):
        """
        Vérifie si le tournoi est terminé et met à jour l'état final (end_date,
        finished_tour), calcule et affiche les résultats finaux (classement des
        joueurs par points descendants)

        Args :
         my_tournament (Tournament) : une instance d'une classe Tournament.
         my_players (list[Player]) : une liste des instances de
         Player participant au tournoi.
        Returns :
         my_tournament (Tournament) : updaté de la date de fin si terminé
        """
        end_round = int(my_tournament.rounds_nbr)
        if my_tournament.current_round == end_round and \
                len(my_tournament.rounds_tour) == end_round and \
                my_tournament.rounds_tour[-1]['end_date'] is not None:
            my_tournament.finished_tour = True
            my_tournament.end_date = datetime.today().strftime(
                '%d/%m/%Y %H:%M:%S')
            points_mapping = RoundController.create_points_mapping(
                    my_tournament)
            # calcul des points finaux des instances de joueurs
            for player in my_players:
                total_points = sum(
                        points for points in points_mapping[player.chess_id])
                player.points = total_points
            ReportController.display_finished_tournament(my_tournament,
                                                         my_players)
            UV.input_return_prints("continue")
            return my_tournament
        else:
            return my_tournament
