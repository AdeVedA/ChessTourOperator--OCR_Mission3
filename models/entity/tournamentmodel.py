class TournamentModel:

    def __init__(
        self, name, location, description, start_date, end_date="", 
        current_round=1, rounds_nbr=4, tournament_id=1,  
        players_tour=[], rounds_tour=[] ,finished_tour=False
                 ):
        self.name = name
        self.location = location
        self.description = description
        self.start_date = start_date
        self.end_date = end_date if end_date else "à terminer"
        self.current_round = current_round
        self.rounds_nbr = rounds_nbr  # nbr de round d'un tournoi(def = 4)
        self.tournament_id = tournament_id
        self.players_tour = players_tour if players_tour else []
        self.rounds_tour = rounds_tour if rounds_tour else []
        #for round in range(1,len(self.rounds_nbr)):
        #    self.rounds_tour.append
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
        """_summary_

        Args:
            player (_type_): _description_
        """
        self.players_tour.append(player)
        
 
    def next_round(self, current_round, rounds_nbr):
        """_summary_

        Args:
            current_round (_type_): _description_
            rounds_nbr (_type_): _description_
        """
        if self.current_round < self.rounds_nbr:
            self.current_round += 1
        else:
            self.finished_tour = True
