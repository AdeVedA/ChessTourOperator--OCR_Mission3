from controllers import mainctrl

if __name__ == '__main__':

    try:
        mainctrl.MainController.run()
    except KeyboardInterrupt:
        print("\nArrêt par service commandé d'interruption utilisateur...")

        '''TO_DO LIST
        si fin de tournoi, affichage du classement/points des joueurs
        revoir les rapports
        flake8...
        readme...
        powerp
        rdv
        '''
