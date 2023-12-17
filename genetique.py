import sys
import time

from matplotlib import pyplot as plt
import numpy as np
from openpyxl import load_workbook
sys.path.append('src')

from icecream import ic

## Variables de résolution ##
PROBLEME = 31

LEN_POP = 15
MUTATION_RATE = 0.1

MAX_RESEARCH_TIME = 15



## Résolution ##
def genetique(probleme, len_population, mutation_rate, max_research_time):
    from flowshop import Flowshop
    
    ## Création du problème ##
    donnees = f'Donnees/tai{probleme}.txt'
    start = time.perf_counter()
    fs = Flowshop(donnees, 'mutation', len_population)
    print(f'preprocess : {time.perf_counter() - start} s')
    start = time.perf_counter()
    generation_number = 0
    while time.perf_counter() - start < max_research_time:
        fs.genetic_step(mutation_rate)
        generation_number += 1
    



    if __name__ == '__main__':
        ic(generation_number)
        plt.plot(fs.historique_valeurs)
        plt.show()

        # Affichange de la solution
        print(f'Séquence :  {[job.id for job in fs.meilleur_ordo.sequence]}')
        print(f'Temps de process de la solution :  {fs.meilleur_ordo.valeur}')

        fs.afficher_diagramme_gantt()
    
    nouvelle_ligne = ['génétique', '', max_research_time, '', '', '', '', '', probleme, fs.meilleur_ordo.valeur, len_population, mutation_rate]

    chemin_fichier_xlsx = 'Resultats.xlsx'
    classeur = load_workbook(chemin_fichier_xlsx)
    feuille = classeur.worksheets[0]
    feuille.append(nouvelle_ligne)
    classeur.save(chemin_fichier_xlsx)


if __name__ == '__main__':
    genetique(PROBLEME, LEN_POP, MUTATION_RATE, MAX_RESEARCH_TIME)
