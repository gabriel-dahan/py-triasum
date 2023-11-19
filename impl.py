
from typing import List
from itertools import permutations
import numpy as np

G = {
    0: (0, 2, 3),
    1: (0, 1, 3),
    2: (1, 3, 4),
    3: (2, 5, 6),
    4: (2, 3, 6),
    5: (3, 4, 6),
    6: (4, 6, 7),
    7: (5, 6, 8),
    8: (6, 7, 8)
}

LINKS = {
    0: (4, 6),
    1: (2, 6),
    2: (1, 4, 8),
    3: (5, 7),
    4: (0, 2, 8),
    5: (3, 7),
    6: (0, 1),
    7: (3, 5),
    8: (2, 4)
}

def repartitions() -> np.ndarray:
    p = permutations(range(1, 10), 9)

    res = np.zeros((362880, 9), dtype = int)
    # On aurait pu mettre sum(1 for _ in p) à la place de 362880 pour quelque chose de plus dynamique mais pas besoin ici.
    # Contre intuitivement, len(list(p)) serait plus couteux en mémoire que sum(1 for _ in p).

    for i, comb in enumerate(p):
        for j in range(9):
            res[i][j] = sum(comb[G[j][digit]] for digit in range(3))
        # Combinaison exemple : (8, 3, 4, 2, 9, 5, 7, 1, 6)
        # On prend les 3 termes correspondant dans le dictionnaire et on les additionne.
    return res

def error_finder(repartition: List[int]) -> List[int]:
    """ Renvoie un tuple avec l'erreur et sa position. """
    for i in range(9):
        ...

if __name__ == '__main__':
    from random import choice
    print(choice(repartitions())) # Renvoie un jeu au hasard.