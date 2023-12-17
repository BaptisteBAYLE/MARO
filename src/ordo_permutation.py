


from icecream import ic 
from ordonnancement import Ordo
from random import sample, shuffle

class Ordo_permutation(Ordo):

    
    def get_all_neighbors(self):
        neighbors = [self.permute(i, j) for i in range(self.nb_job) for j in range(i)]
        
        return neighbors

    
    def get_random_neighbor(self):
        i, j  = sample(range(self.nb_job), 2)
        liste_job = self.sequence.copy()
        liste_job[i], liste_job[j] = liste_job[j], liste_job[i]

        return Ordo_permutation(liste_job)
    

    def shuffle(self):
        liste_job = self.sequence
        shuffle(liste_job)
        return Ordo_permutation(liste_job)
    

    def permute(self, i, j):
        liste_job = self.sequence.copy()
        liste_job[i], liste_job[j] = liste_job[j], liste_job[i]
        return Ordo_permutation(liste_job)
    

    def NEH(self):

        ordo_NEH = Ordo_permutation([self.sequence[0]])
        for job in self.sequence[1:]:
            cmin = 100_000
            for i in range(ordo_NEH.nb_job):
                
                seq = ordo_NEH.sequence.copy()
                seq.insert(i, job)
                ordo = Ordo_permutation(seq)
                cmax = ordo.valeur
                if cmax < cmin:
                    best_ordo = ordo
                    cmin = cmax
            ordo_NEH = best_ordo

        return ordo_NEH
    

    def mutation(self):
        return super().mutation()
    

    def crossover(self, __value: object):
        return super().crossover(__value)
  