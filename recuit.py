import sys
import time

from matplotlib import pyplot as plt
from openpyxl import load_workbook
sys.path.append('src')

from icecream import ic 


## Variables de resolution ##
probleme = 31

max_research_time = 10 # Temps en seconde
max_local_search_time = 5 # Temps en seconde
alpha = 0.01
beta = 1.5
type_voisin = 'deplacement' # 'deplacement' ou 'permutation' ou 'genetique'
len_historique = 1

def recuit(probleme, max_research_time, max_local_search_time, alpha, beta, type_voisin, len_historique):

    from flowshop import Flowshop

    ## Création du problème ##
    donnees = f'Donnees/tai{probleme}.txt'
    fs = Flowshop(donnees, type_voisin)


    ## Boucle pour la recherche générale ##
    start = time.perf_counter()
    nb_genral_research = 0
    while time.perf_counter() - start < max_research_time:
        
        fs.shuffle_ordo(len_historique)
        
        nb_genral_research += 1
        local_start = time.perf_counter()
        while time.perf_counter() - local_start < max_local_search_time:
            fs.local_step_random(alpha, beta)
            fs.save_if_better()

    end = time.perf_counter()
    total_time = end - start 

    ## Affichage des resultats ##

    # Indicateurs de resolution
    if __name__ == 'main':

        ic(total_time)
        ic(nb_genral_research)

        plt.plot(fs.historique_valeurs)
        plt.show()

        # Affichange de la solution
        print(f'Séquence :  {[job.id for job in fs.meilleur_ordo.sequence]}')
        print(f'Temps de process de la solution :  {fs.meilleur_ordo.valeur}')

        fs.afficher_diagramme_gantt()

    nouvelle_ligne = ['recuit', type_voisin, max_research_time, max_local_search_time, '', alpha, beta, '', probleme, fs.meilleur_ordo.valeur]

    chemin_fichier_xlsx = 'Resultats.xlsx'
    classeur = load_workbook(chemin_fichier_xlsx)
    feuille = classeur.worksheets[0]
    feuille.append(nouvelle_ligne)
    classeur.save(chemin_fichier_xlsx)

if __name__ == 'main':
    recuit(probleme, max_research_time, max_local_search_time, alpha, beta, type_voisin, len_historique)