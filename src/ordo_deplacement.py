


from icecream import ic 
from ordonnancement import Ordo
from random import sample, shuffle



NB_VOISIN_PAR_ORDO = 25

class Ordo_deplacement(Ordo):

    def get_all_neighbors(self):
        neighbors = [self.change(i, sample(range(self.nb_job), 1)[0])
                      for i in range(self.nb_job)
                        for _ in range(NB_VOISIN_PAR_ORDO)]
        
        return neighbors

    
    def get_random_neighbor(self):
        i, j  = sample(range(self.nb_job), 2)
        return self.change(i, j)
    

    def shuffle(self):
        liste_job = self.sequence
        shuffle(liste_job)
        return Ordo_deplacement(liste_job)
    

    def change(self, i, j):
        '''
        Déplace l'objet à la position i vers la position j
        '''

        liste_job = self.sequence.copy()
        job = liste_job.pop(i)
        liste_job.insert(j, job)

        return Ordo_deplacement(liste_job)
    
    def NEH(self):

        ordo_NEH = Ordo_deplacement([self.sequence[0]])
        for job in self.sequence[1:]:
            cmin = 100_000
            for i in range(ordo_NEH.nb_job):
                
                seq = ordo_NEH.sequence.copy()
                seq.insert(i, job)
                ordo = Ordo_deplacement(seq)
                cmax = ordo.valeur
                if cmax < cmin:
                    best_ordo = ordo
                    cmin = cmax
            ordo_NEH = best_ordo

        return ordo_NEH
    
