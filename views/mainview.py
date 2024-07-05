from views.utilsviews import UtilsView
from colorama import Fore


class MainMenuView:

    @classmethod
    def display(cls):
        header = "Logiciel de Gestion de Tournois d'Échecs"
        menu_options = [
            "1. Gérer les Joueurs",
            "", 
            "2. Gérer les Tournois",
            "",
            "3. Consulter les rapports",
            "",
            "",
            "",
            "0. Quitter"
            ]
        UtilsView.menu(header, menu_options)
        choice = input()
        return choice

    @classmethod
    def firstscreen(cls):
        UtilsView.clear_screen()
        Chesscreen =r"""                                          _/\_   
                         o   |\ _()_ /||\ \''/ /|    o     
 _   _   _   |\__      /\^/\ | '-::-' || :'--': |  /\^/\   |\__     _   _   _ 
| |_| |_| | /   o\__  | o/O ) \      /  \      /  | O/o ) /   o\__ | |_| |_| |
 \       / |    ___=' |  _ /   |    |    |    |   |  _ / |    ___=' \       / 
  |  |  |  |    \      \  /    |    |    |    |    \  /  |    \      |  |  |
  |  |  |   \    \     |  |    |    |    |    |    |  |   \    \     |  |  |  
  |  |  |    >    \    |  |    |    |    |    |    |  |    >    \    |  |  |  
 /  / \  \  /      \  /    \  /      \  /      \  /    \  /      \  /  / \  \ 
|_________||________||______||________||________||______||________||_________|
    __         __       __       __        __       __       __         __   
   (  )       (  )     (  )     (  )      (  )     (  )     (  )       (  )  
    ><         ><       ><       ><        ><       ><       ><         ><   
   |  |       |  |     |  |     |  |      |  |     |  |     |  |       |  |  
  /    \     /    \   /    \   /    \    /    \   /    \   /    \     /    \ 
 |______|   |______| |______| |______|  |______| |______| |______|   |______|
    
                                                _   _              
         _/_  /        /  / _       _        /.' ).' )             
      °  /      ,     /  / / )_/ / / )      /   /   /  _       _   
     /  /\     / )   (__/ (_/ (_/\/ (__    /   /   /  / )_/ /_/_)  
  __/\_/  \_  /_/    __/                  /   /   (__(_/ (_/ (__  () () ()
                    (_/"""
        #ce dessin a été copié du site asciiart (auteur anomnyme) puis légèrement modifié
        UtilsView.style_print(content=f"{Chesscreen}")
        UtilsView.input_return_prints("bienvenue")
