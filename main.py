from controllers import mainctrl

if __name__ == '__main__':

    try:
        main_page = mainctrl.MainController()
        main_page.run()
    except KeyboardInterrupt:
        print("\nArrêt par service commandé d'interruption utilisateur...")