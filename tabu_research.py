import sys
import time

from matplotlib import pyplot as plt
import numpy as np
from openpyxl import load_workbook
sys.path.append('src')

from icecream import ic


## Variables de resolution ##
probleme = 31

max_research_time = 10 # Temps en seconde
max_ite_local = 60
type_voisin = 'deplacement' # 'deplacement' ou 'permutation'
len_historique = 30 # Taille de la liste des solutions tabou

def tabu_research(probleme, max_research_time, max_ite_local, type_voisin, len_historique):

    ## Création du problème ##
    from flowshop import Flowshop
    donnees = f'Donnees/tai{probleme}.txt'
    fs = Flowshop(donnees, type_voisin)


    ## Variables d'observation du problème ##
    index = []
    

    ## Boucle pour la recherche générale ##
    start = time.perf_counter()
    while time.perf_counter() - start < max_research_time:
        t1 = time.perf_counter()
        fs.shuffle_ordo(len_historique)
        
        for local_index in range(max_ite_local):
            
            if fs.local_step_meilleur(len_historique):
                
                break
            
            fs.save_if_better()

        index += [local_index]

        end_local = time.perf_counter()
        local_time = end_local - t1

    end = time.perf_counter()
    total_time = end - start  
    mean_index = np.mean(index)
    nb_local_bound_reached = len([0 for i in index if i == max_ite_local])
    nb_genral_research = len(index)

    if __name__ == '__main__':
        ## Affichage des resultats ##

        # Indicateurs de resolution #
        ic(total_time)
        ic(nb_genral_research)
        ic(mean_index)
        ic(nb_local_bound_reached)
        plt.plot(fs.historique_valeurs)
        plt.show()

        # Affichange de la solution
        print(f'Séquence :  {[job.id for job in fs.meilleur_ordo.sequence]}')
        print(f'Valeur de la solution :  {fs.meilleur_ordo.valeur}')

        fs.afficher_diagramme_gantt()

    # Enregistrement des solutions dans le excel
    nouvelle_ligne = ['tabu', type_voisin, max_research_time, '', max_ite_local, '', '', len_historique, probleme, fs.meilleur_ordo.valeur]
    
    chemin_fichier_xlsx = 'Resultats.xlsx'
    classeur = load_workbook(chemin_fichier_xlsx)
    feuille = classeur.worksheets[0]
    feuille.append(nouvelle_ligne)
    classeur.save(chemin_fichier_xlsx)

if __name__ == '__main__':
    tabu_research(probleme, max_research_time, max_ite_local, type_voisin, len_historique)