

from random import shuffle
from abc import ABC, abstractmethod
from job import Job
from icecream import ic

class Ordo(ABC):

    def __init__(self, list_job : list[Job]):
        self.sequence = list_job
        self.nb_job = len(list_job)
        self.nb_machine = list_job[0].nb_machine
        self.disponibilite = [0] * self.nb_machine
        
        if list_job:
            self.__ordonancer_liste(list_job)
        
        self.valeur = self.__get_valeur()
    
    
    def __hash__(self) -> int:
        return hash((hash(job) for job in self.sequence))
    

    def __eq__(self, other):
        return self.valeur == other.valeur
    

    def __lt__(self, other):
        return self.valeur < other.valeur
    

    def __le__(self, other):
        return self.valeur <= other.valeur


    def __ordonnancer(self, job : Job) -> None:
        '''
        Ordonnace le job a la suite de l'ordonancement
        '''
        
        for machine, dispo_machine in enumerate(self.disponibilite):
            dispo_job = 0

            if machine:
                dispo_job = self.disponibilite[machine - 1]
            
            job.set_debut(machine, max(dispo_job, dispo_machine))

            self.disponibilite[machine] = job.debut[machine] + job.duree[machine]
        
        pass

    
    def __ordonancer_liste(self, list_job : list[Job]) -> None:
        '''
        Ordonnance une liste de job
        '''

        for job in list_job:
            
            self.__ordonnancer(job)
        pass


    def __get_valeur(self) -> int:
        '''
        Renvoie la valeur de la solution de l'ordonnancement
        '''

        return self.disponibilite[-1]
    

    @abstractmethod
    def shuffle(self):
        '''
        Renvoie un ordonnancement aléatoire 'éloigné' de l'actuel
        '''


    @abstractmethod
    def NEH(self):
        '''
        Renvoie un ordonnancement rangé selon l'heuristique NEH
        '''
        pass        


    @abstractmethod
    def get_random_neighbor(self):
        '''
        Renvoie un voisin aléatoire de l'ordonnancement
        '''
        pass


    @abstractmethod
    def get_all_neighbors(self):
        '''
        Renvoie tous les voisins d'un ordonnancement
        '''
        pass

    @abstractmethod
    def crossover(self, __value : object):
        '''
        Renvoie un enfant de self et __value
        '''
        pass

    @abstractmethod
    def mutation(self):
        '''
        Renvoie un ordonnacement qui résulte d'une mutation de self
        '''
        pass

