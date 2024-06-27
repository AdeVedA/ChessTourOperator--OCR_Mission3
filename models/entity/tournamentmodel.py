class TournamentModel:

    def __init__(
        self, name, location, description, start_date, end_date=None, 
        current_round=1, rounds_nbr=4, tournament_id=1,  
        players_tour=[], rounds_tour=[] ,finished_tour=False
                 ):
        self.name = name
        self.location = location
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.current_round = current_round
        self.rounds_nbr = rounds_nbr  # nbr de round d'un tournoi(def = 4)
        self.tournament_id = tournament_id
        self.players_tour = players_tour if players_tour else []
        self.rounds_tour = rounds_tour if rounds_tour else []
        #for round in range(1,len(self.rounds_nbr)):
        #    self.rounds_tour.append
        self.finished_tour = finished_tour

    def make_round_one(self, my_tournament, instantiated_players):
        #
        # un pti TournamentCtrl plutôt ?
        #
        '''permet de créer le premier round, en attendant de dispatcher la fonction en bonne place dans le MVC ;)
        et de faire le ménage aussi hihi
        '''
        if int(my_tournament.current_round) == 1:
            #self.round_number = int(my_tournament.current_round)
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
            
            for pair in pairs :
                player_id1 = f"{pair[0].firstname} {pair[0].lastname} (chessID {pair[0].chess_id})"
                player_id2 = f"{pair[1].firstname} {pair[1].lastname} (chessID {pair[1].chess_id})"
                # à fourrer dans la vue
                print(f"\nLes matchs de ce round {self.round_number} :\n")
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

    def make_next_round(self, my_tournament, instantiated_players):
        '''permet de créer les rounds (n+1) avec classement par points'''



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
