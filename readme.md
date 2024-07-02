# <p style="text-align: center;">Chess Tour Operator - OCR_Mission[3]</p>
<p style="text-align: center;">=========================================================================</p>

### <p style="text-align: center;">- Logiciel de Gestion de Tournois d'Échecs -</p>

### <p style="text-align: center;">(readme en construction)</p>


------------------------------------------

## <p style="text-align: center;">I - Setup windows</p>

#### ( si [Git](https://github.com/git-for-windows/git/releases/download/v2.45.0.windows.1/Git-2.45.0-64-bit.exe) et [python 3.6+](https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe) ne sont pas installés, commencez par l'annexe 1 !)
------------------------------------------
  #### A - Créez un répertoire pour le programme
Lancez votre explorateur windows (WIN+E) 
Créez un répertoire (CTRL+MAJ+N) pour le programme où vous le souhaitez et **nommez-le**
ex. : vous pouvez l'appeler **ChessTourOP** dans d:\chemin\vers\mon\dossier\ChessTourOP
**double-cliquez** sur le répertoire créé pour aller dedans.

  #### B - lancez l'interpréteur de commande windows
Clic gauche dans la barre d'adresse de l'explorateur, écrivez **"cmd"** (à la place de l'adresse)
et appuyez sur **"entrée"** (comme à chaque instruction en ligne future):

	cmd
	
  #### C - clonez le repo Github du projet dans ce répertoire
dans le terminal (l'invite de commande) qui indique bien que vous êtes à l'adresse du dossier créé, écrivez tour à tour:

	git init

puis : 

	git pull https://github.com/AdeVedA/ChessTourOperator--OCR_Mission3 -t main

  #### D - installez un environnement virtuel dans un dossier 'env' du projet, toujours par l'invite de commande :
	
	python -m venv env
 
  #### E - activez l'environnement virtuel créé précédemment :
	
	env\Scripts\activate.bat
 
  #### F - installez les librairies requises :
	
	pip install -r requirements.txt

  #### G - Lancement du programme (l'environnement virtuel doit avoir été activé avant):

	python main.py

  #### H - Désactivez l'environnement virtuel

	deactivate
-------------------------
-------------------------

## <p style="text-align: center;">II - Setup Linux/Mac</p>

#### ( si **[Git](https://sourceforge.net/projects/git-osx-installer/files/git-2.23.0-intel-universal-mavericks.dmg/download?use_mirror=autoselect)** et **[python](https://www.python.org/ftp/python/3.12.3/python-3.12.3-macos11.pkg)** ne sont pas installés, commencez par l'annexe 1 !)

-------------------------
	
  #### A- lancez un terminal

clic sur loupe/recherche lancez

	terminal
	
  #### B - Créez un répertoire pour le programme et placez-vous dedans
  par exemple si vous souhaitez appeler ce dossier "ChessTourOP" :

	mkdir ChessTourOP

puis :

	cd ChessTourOP

  #### C - clonez le repo Github du projet dans ce répertoire
dans le terminal (l'invite de commande) qui indique bien que vous êtes à l'adresse du dossier créé, écrivez tour à tour:

	git init

puis : 

	git pull https://github.com/AdeVedA/ChessTourOperator--OCR_Mission3 -t main

  #### D - installez un environnement virtuel dans un dossier 'env' du projet, toujours par le terminal :
	
	python3 -m venv env

  #### E - activez l'environnement virtuel créé précédemment :
	
	source env/bin/activate
 
  #### F - installez les librairies requises :
	
	pip install -r requirements.txt

  #### G - Lancement du programme (l'environnement virtuel doit avoir été activé avant):

	python3 main.py

  #### H - Désactivez l'environnement virtuel

	deactivate
 

## <p style="text-align: center;">III - informations sur la structure de données</p>

les données de vos tournois et joueurs sont toutes sauvegardées en .json dans le répertoire "datas" et le sous-répertoire "tournaments"

	racine_projet/
				├──────datas/
				├	├────players_data.json
				├	└────tournaments/
				├			├─────tournament_1.json
				├			└─────tournament_2.json...
				└─────main.py
				etc...

# <p style="text-align: center;">Annexe 1 - installation de Python & Git</p>
=======================================================================

pour Windows 64bits :
--------------------

installez **[Git](https://github.com/git-for-windows/git/releases/download/v2.45.0.windows.1/Git-2.45.0-64-bit.exe)** 
verifiez en tapant "cmd" dans le menu démarrer puis "git version" dans le terminal

installez **[python](https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe)** en vous assurant que ***"Add to PATH"*** est coché (laissez les autres choix par défaut)
verifiez en tapant "cmd" dans le menu démarrer puis "python --version" dans le terminal

pour Mac/Linux :
--------------------
**Git**
cliquez sur l'icone de recherche (loupe), écrivez "terminal" (on vérifie si git est déjà présent)

	git version

si ok, passez à python. 
sinon, installez ce qu'il vous propose d'installer ("command line developer tools") puis recommencez "git version" en terminal,
sinon : installez **[Git](https://sourceforge.net/projects/git-osx-installer/files/git-2.23.0-intel-universal-mavericks.dmg/download?use_mirror=autoselect)**
puis revérifiez git version dans le terminal

**Python**
installez **[python](https://www.python.org/ftp/python/3.12.3/python-3.12.3-macos11.pkg)**
