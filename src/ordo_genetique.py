from icecream import ic
from job import Job 
from ordonnancement import Ordo
from random import sample, shuffle



class Ordo_mutation(Ordo):

    def crossover(self, __value: object):
        p1 = self.sequence.copy()
        p2 = __value.sequence.copy()
        cross_point = sample(list(range(self.nb_job)), 1)[0]

        son = p1[:cross_point] + p2[cross_point:]
        self.__fix(son)
        
        return Ordo_mutation(son)
    

    def mutation(self):
        i, j  = sample(range(self.nb_job), 2)
        liste_job = self.sequence.copy()
        job = liste_job.pop(i)
        liste_job.insert(j, job)

        return Ordo_mutation(liste_job)
    

    def shuffle(self):
        liste_job = self.sequence
        shuffle(liste_job)
        return Ordo_mutation(liste_job)
    

    def __fix(self, son : list[Job]):
        
        ids = [job.id for job in son]

        missing_jobs = [job for job in self.sequence if not(job.id in ids)]

        for index, job in enumerate(son):
            if job in son[:index]:
                son[index] = missing_jobs.pop(0)

    def get_all_neighbors(self):
        return super().get_all_neighbors()
    
    def get_random_neighbor(self):
        return super().get_random_neighbor()
    
    def NEH(self):

        ordo_NEH = Ordo_mutation([self.sequence[0]])
        for job in self.sequence[1:]:
            cmin = 100_000
            for i in range(ordo_NEH.nb_job):
                
                seq = ordo_NEH.sequence.copy()
                seq.insert(i, job)
                ordo = Ordo_mutation(seq)
                cmax = ordo.valeur
                if cmax < cmin:
                    best_ordo = ordo
                    cmin = cmax
            ordo_NEH = best_ordo

        return ordo_NEH
        
