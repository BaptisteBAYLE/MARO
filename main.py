import sys
from genetique import genetique


from tabu_research import tabu_research
sys.path.append('src')
from recuit import recuit
import time
import math as mt
from icecream import ic
from random import shuffle

N = 3


max_research_time = 15 # Temps en seconde
max_local_search_time = 5 # Temps en seconde
max_ite_local = 60
types_voisin = ['deplacement', 'permutation'] # 'deplacement' ou 'permutation'
len_historique_max = 50 # Taille de la liste des solutions tabou
alpha = 0.01
beta_max = 2.2

for n in range(2, 6):
    for len_pop in range(10, 50, 10):
        for a in range(1, 5, 1):
            ic(len_pop, a)
            mutation_rate = 10**(-a/2)
            genetique(31, len_pop, mutation_rate, 15)
