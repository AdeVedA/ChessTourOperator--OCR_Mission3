import os
import json
from views.utilsviews import UtilsView
from models.entity.roundmodel import Round
tourdatas_path = os.path.join(os.getcwd(), "datas", "tournaments")

class TournamentCrud:
    #def __init__(self):
    #    os.makedirs(tourdatas_path, exist_ok=True)
    @classmethod
    def get_all_tournaments(cls):
        tournaments_files = []
        tournaments_infos = []
        if os.path.isfile(os.path.join(tourdatas_path, "tournament_1.json")):
            #files = os.listdir(tourdatas_path)
            tournaments_files = [f for f in os.listdir(tourdatas_path) 
                                 if f.startswith('tournament_')
                                 and f.endswith('.json')
                                 and any(char.isdigit() for char in f[11:-5])]
            for file in tournaments_files:
                with open(os.path.join(tourdatas_path,f"{file}"),
                          'r', encoding='utf-8') as file:
                    try:
                        tournaments_infos.append(json.load(file))
                    except json.JSONDecodeError:
                        pass
        else:
            UtilsView.input_return_prints("notournament")
        return tournaments_infos
    
    @classmethod
    def save_new_tournament(cls, tournament):
        """_summary_

        Args:
            tournament (objet instance de Tournament cls): _description_
        """
        i=1
        while os.path.exists(os.path.join(tourdatas_path, f"tournament_{i}.json")):
            i += 1
            tournament.tournament_id = i
        with open(os.path.join(tourdatas_path, f"tournament_{i}.json"), 'w', encoding='utf8') as file:
             json.dump(tournament.__dict__, file, ensure_ascii=False, indent=4)

    @classmethod
    def update_tournament_players(cls, my_tournament):
        """
        """
        i = my_tournament.tournament_id
        with open(os.path.join(tourdatas_path, f"tournament_{i}.json"), 'w', encoding='utf8') as file:
             json.dump(my_tournament.__dict__, file, ensure_ascii=False, indent=4)
        UtilsView.input_return_prints("tournament_save", my_tournament.name)
        pass

    @classmethod
    def update_tournament(cls, my_tournament, _round):
        """sérialise le tournoi sauvegarde le tournoi en l'état
        """
        if my_tournament.rounds_tour==[] or _round.name!=my_tournament.rounds_tour[-1]['name']:
            my_tournament.rounds_tour.append(Round.to_json(_round))
        elif my_tournament.rounds_tour!=[] and _round.name==my_tournament.rounds_tour[-1]['name']:
            del my_tournament.rounds_tour[-1]
            my_tournament.rounds_tour.append(Round.to_json(_round))
        my_tournament_dict = my_tournament.to_json()
        i = my_tournament_dict['tournament_id']
        with open(os.path.join(tourdatas_path, f"tournament_{i}.json"), 'w', encoding='utf8') as file:
             json_dumps_str = json.dumps(my_tournament_dict, ensure_ascii=False, indent=4)
             print(json_dumps_str, file=file)
        UtilsView.input_return_prints("tournament_save", my_tournament_dict['name'])
        return my_tournament