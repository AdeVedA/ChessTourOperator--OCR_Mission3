from controllers import mainctrl

if __name__ == '__main__':

    try:
        mainctrl.MainController.run()
    except KeyboardInterrupt:
        print("\nArrêt par service commandé d'interruption utilisateur...")
