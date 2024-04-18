# Exercice 2: Algorithmes de recherche avancés
# Implémentez l'algorithme de recherche A* pour trouver le chemin le plus court entre deux points dans une grille.

import heapq

def astar_search(graph, start, goal):
    queue = [(0, start)]
    visited = set()

    while queue:
        cost, current_node = heapq.heappop(queue)
        if current_node == goal:
            return cost
        if current_node not in visited:
            visited.add(current_node)
            for neighbor, neighbor_cost in graph[current_node]:
                heapq.heappush(queue, (cost + neighbor_cost, neighbor))

# Exemple d'utilisation
graph = {'A': [('B', 1), ('C', 3)],
         'B': [('A', 1), ('D', 5)],
         'C': [('A', 3), ('D', 1)],
         'D': [('B', 5), ('C', 1)]}

start_node = 'A'
goal_node = 'D'
print(astar_search(graph, start_node, goal_node))
