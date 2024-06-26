from views.reportviews import ReportView
from views.utilsviews import UtilsView
from models.manager.playermanager import PlayerCrud
from models.manager.tournamentmanager import TournamentCrud


class RoundController:
    '''Contrôleur pour gérer les rounds d'un tournoi.'''

    @classmethod   
    def make_round_one_pairs():
        """Permet d'appairer les joueurs au hasard lors du premier round
        """
        
        