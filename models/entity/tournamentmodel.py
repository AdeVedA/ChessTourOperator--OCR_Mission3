class TournamentModel:
    """représente un tournoi avec ses attributs
    précisions:
    current_round = soit le numéro du futur round à créer,
                    soit le numéro du round déjà crée
                    mais dont les résultats n'ont pas été renseignés
    rounds_nbr = le nombre de rounds du tournoi
    tournament_id = l'identifiant numérique unique d'un tournoi
    players_tour = liste des chess_id des joueurs inscrits au tournoi
    rounds_tour = liste de dictionnaire des rounds déjà enregistrés
                  avec pour clés (nom, dates de début, de fin, liste de matchs)
    finished_tour (bool) = état "fini ou non" du tournoi
    """
    def __init__(
        self, name, location, description, start_date, end_date="",
        current_round=1, rounds_nbr=4, tournament_id=1,
        players_tour=[], rounds_tour=[], finished_tour=False
                ):
        self.name = name
        self.location = location
        self.description = description
        self.start_date = start_date
        self.end_date = end_date if end_date else "à terminer"
        self.current_round = current_round
        self.rounds_nbr = rounds_nbr
        self.tournament_id = tournament_id
        self.players_tour = players_tour
        self.rounds_tour = rounds_tour
        self.finished_tour = finished_tour

    def to_json(self):
        """convertit un objet tournament en dictionnaire serialisable
        """
        my_tournament = {
            "name": self.name,
            "location": self.location,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "current_round": self.current_round,
            "rounds_nbr": self.rounds_nbr,
            "tournament_id": self.tournament_id,
            "players_tour": self.players_tour,
            "rounds_tour": self.rounds_tour,
            "finished_tour": self.finished_tour
        }
        return my_tournament

    def __repr__(self):
        return f"Tournament{self.tournament_id} : {self.name}"

    def add_player(self, player):
        """
        """
        self.players_tour.append(player)

    def next_round(self):
        """ méthode pour incrémenter le numéro du round en cours du tournoi
        """
        if self.current_round < self.rounds_nbr:
            self.current_round += 1
        else:
            self.finished_tour = True

    def tour_players(self):
        """récupère les joueurs inscrits à ce tournoi
        """
        return self.players_tour
