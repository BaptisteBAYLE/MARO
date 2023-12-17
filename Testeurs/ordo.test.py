import sys

sys.path.append('./src')
from ordo_permutation import Ordo_permutation

from job import Job
from ordonnancement import Ordo


tableau = [
    [54, 79, 16, 66, 58],
    [83, 3, 89, 58, 56],
    [15, 11, 49, 31, 20],
    [71, 99, 15, 68, 85],
    [77, 56, 89, 78, 53],
    [36, 70, 45, 91, 35],
    [53, 99, 60, 13, 53],
    [38, 60, 23, 59, 41],
    [27, 5, 57, 49, 69],
    [87, 56, 64, 85, 13],
    [76, 3, 7, 85, 86],
    [91, 61, 1, 9, 72],
    [14, 73, 63, 39, 8],
    [29, 75, 41, 41, 49],
    [12, 47, 63, 56, 47],
    [77, 14, 47, 40, 87],
    [32, 21, 26, 54, 58],
    [87, 86, 75, 77, 18],
    [68, 5, 77, 51, 68],
    [94, 77, 40, 31, 28]
]

liste_job = [Job(id, duree) for id, duree in enumerate(tableau)]

ordo = Ordo_permutation(liste_job)

## Test 1 ##
if ordo.disponibilite == [1121, 1198, 1292, 1336, 1448]:
    print('test ordo #1 passed')
else:
    print('test ordo #1 failed')
## Test 2 ##
if ordo.valeur == 1448:
    print('test ordo #2 passed')
else:
    print('test ordo #2 failed')
