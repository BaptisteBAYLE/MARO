import sys
sys.path.append('./src')


from flowshop import Flowshop
from ordo_permutation import Ordo_permutation



fs = Flowshop('./Donnees/tai01.txt')

jobs = fs.liste_jobs

ordo = Ordo_permutation(jobs)
print(ordo.disponibilite)
print(ordo.valeur)


