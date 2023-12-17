

from icecream import ic
from job import Job
from ordo_genetique import Ordo_mutation
from random import random, sample


class Population:

    def __init__(self, len_population : int, list_job : list[Job]) -> None:
        self.list_job = list_job
        self.len_population = len_population
        ordo = Ordo_mutation(list_job)
        self.population = [ordo.shuffle() for _ in range(int(len_population / 5 * 4))] + [ordo.shuffle().NEH() for _ in range(int((len_population + 1) / 5))]
        self.population.sort(key = lambda x : x.valeur)
    

    def next_generation(self, mutation_rate):
        '''
        Renvoie une population qui correspond à la nouvelle génération
        '''
        couples = [(o1, o2) for index, o1 in enumerate(self.population) for o2 in self.population[:index]]

        sons = list(set([o1.crossover(o2) for o1, o2 in couples]))
        for index, ordo in enumerate(sons):
            if random() < mutation_rate:
                sons[index] = ordo.mutation()
                if random() < mutation_rate:
                    sons[index] = ordo.shuffle()
        sons.sort(key = lambda x : x.valeur)

        size_of_best = int(self.len_population/4 * 3)
        size_of_random = self.len_population - size_of_best
        while (len(sons) < self.len_population):
            sons.append(sons[0].shuffle())

        self.population = sons[:size_of_best] + sample(sons[size_of_best:], size_of_random)
        
    

    def get_best(self):
        '''
        Renvoie le meilleur individu de la population
        '''

        return self.population[0]
    

    

 