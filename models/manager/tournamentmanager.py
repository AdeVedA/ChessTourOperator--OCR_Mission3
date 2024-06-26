import os
import json
from views.utilsviews import UtilsView

tourdatas_path = os.path.join(os.getcwd(), "datas", "tournaments")

class TournamentCrud:
    #def __init__(self):
    #    os.makedirs(tourdatas_path, exist_ok=True)
    @classmethod
    def get_all_tournaments():
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
    
        """
        numbers = []
        for f in tournament_files:
            num_str = ''
            for char in f[11:-5]:
                if char.isdigit():
                    num_str += char
        numbers.append(int(num_str))
        max_nbr_tournament = max(numbers)
        return max_nbr_tournament
        """

    @classmethod
    def save_new_tournament(tournament):
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
    def update_tournament(my_tournament):
        """
        """
        i = my_tournament.tournament_id
        with open(os.path.join(tourdatas_path, f"tournament_{i}.json"), 'w', encoding='utf8') as file:
             json.dump(my_tournament.__dict__, file, ensure_ascii=False, indent=4)
        pass
        