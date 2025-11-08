import time
from itertools import permutations


def tsp_bruteforce(dist: list[list[float]], timeout: float = 10):
    """
    dist: square matrix dist[i][j] with distance
    timeout: algorithm timeout in seconds
    return: (min_distance, best_route)
    """
    deadline = time.time() + max(timeout, 1)
    n = len(dist)
    best_cost = float("inf")
    best_route = None
    optimal = False

    for perm in permutations(range(n)):
        cost = 0
        if time.time() > deadline:
            return best_cost, best_route, optimal
        for i in range(n - 1):
            cost += dist[perm[i]][perm[i + 1]]
        cost += dist[perm[-1]][perm[0]]

        if cost < best_cost:
            best_cost = cost
            best_route = perm
    optimal = True

    return best_cost, best_route, optimal
