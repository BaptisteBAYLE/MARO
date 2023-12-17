


from abc import ABC, abstractmethod

from matplotlib import pyplot as plt
from job import Job
from ordo_deplacement import Ordo_deplacement
from ordo_permutation import Ordo_permutation
from random import random
from icecream import ic

from population import Population





class Flowshop(ABC):
    

    def __init__(self, donnees : str, type_voisin : str, len_population: None | int = None) -> None:
        '''
        type_voisin : 'permutation' ou 'deplacement' 
        '''

        self.nb_machines = 0
        self.nb_jobs = 0
        self.liste_jobs = []
        self.historique_ordo = []
        self.historique_valeurs = []

        self.__lire_donnee(donnees)
        
        if type_voisin == 'permutation':
            self.ordo = Ordo_permutation(self.liste_jobs)
            self.meilleur_ordo = self.ordo
        
        if type_voisin == 'deplacement':
            self.ordo = Ordo_deplacement(self.liste_jobs)
            self.meilleur_ordo = self.ordo

        if type_voisin == 'mutation':
            self.population = Population(len_population, self.liste_jobs)
            self.meilleur_ordo = self.population.get_best()


    def __lire_donnee(self, donnees : str):
        data = open(donnees, 'r')
        entete = data.readline()
        entete = entete.split()
        self.nb_machines = int(entete[1])
        self.nb_jobs = int(entete[0])

        tableau = data.readlines()
        tableau = [[int(elt) for elt in ligne.split()] for ligne in tableau]

        self.liste_jobs = [Job(i, duree) for i, duree in enumerate(tableau)]


    def local_step_random(self, aplha : float, beta : float):
        '''
        Realise une etape de la recherche aleatoire
        '''

        voisin = self.ordo.get_random_neighbor()

        if voisin.valeur < self.ordo.valeur :
            self.ordo = voisin
            self.historique_valeurs.append(self.ordo.valeur)
            return 
        
        if voisin.valeur < self.ordo.valeur * beta:
            if random() <= aplha :
                self.ordo = voisin
                self.historique_valeurs.append(self.ordo.valeur)
                return 
    

    def local_step_meilleur(self, len_historique) -> bool:
        '''
        Réalise une étape de la recherche par meilleur voisin
        Renvoie True si la recherche s'est arreté car tous les voisins tabous
        '''

        voisins = self.ordo.get_all_neighbors()
        voisins.sort(key = lambda x : x.valeur)
        max_index = min(len(voisins), len_historique)
        
        index = 0
        voisin = voisins[index]

        while voisin in self.historique_ordo and index < max_index:
            index += 1
            
            voisin = voisins[index]
        
        
        self.ordo = voisin
        self.historique_valeurs.append(voisin.valeur)
        self.enregistrer_ordo(len_historique)
        
        if index == len_historique:
            return True
        else:
            return False


    def shuffle_ordo(self, len_historique):
        '''
        Melange l'ordonnancement
        '''

        self.ordo = self.ordo.shuffle()
        #self.ordo = self.ordo.NEH()
        self.historique_valeurs.append(self.ordo.valeur)
        self.enregistrer_ordo(len_historique)

    
    def genetic_step(self, mutation_rate : float):
        '''
        Réalise une étape de résolition par algo génétique
        '''

        self.population.next_generation(mutation_rate)

        self.ordo = self.population.get_best()
        
        self.historique_valeurs.append(self.ordo.valeur)
        self.save_if_better()

    
    def save_if_better(self):
        '''
        Savegarde l'ordo actuel comme le meilleur s'il est effectivement le meilleur
        '''

        if self.ordo.valeur < self.meilleur_ordo.valeur :
            self.meilleur_ordo = self.ordo
            ic(self.ordo.valeur)


    def enregistrer_ordo(self, len_historique):
        '''
        Enregistre un ordonnacement dans l'historique mais l'historique ne dois pas dépasser TAILLE_HISTORIQUE éléments
        '''

        self.historique_ordo.append(self.ordo)

        if len(self.historique_ordo) > len_historique:
            self.historique_ordo.remove(self.historique_ordo[0])
        

    def afficher_diagramme_gantt(self):
        self.nb_machines # Nombre de machines
        fig, ax = plt.subplots()
        colors = plt.cm.tab10.colors[:self.nb_jobs]
        
        # Nom des machines en ordonnée
        ax.set_yticks(range(self.nb_machines))
        ax.set_yticklabels([f"Machine {i+1}" for i in range(self.nb_machines)])
        ax.set_xlabel('Temps')

        for i, job in enumerate(self.ordo.sequence):
            debut = job.debut
            duree = job.duree
            for machine in range(self.nb_machines):
                
                ax.barh(machine, duree[machine], left=debut[machine], height=0.5, align='center', color=colors[i % len(colors)])

        ax.set_title('Diagramme de Gantt')
        ax.invert_yaxis()  # Inversion de l'axe y pour afficher les machines du haut en bas
        ax.legend()
        plt.show()


        