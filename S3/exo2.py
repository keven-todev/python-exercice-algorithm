import heapq


def astar_search(graph, start, goal):
    queue = [(0, start)]   #initialise une liste qui coutient le cout initial et le noeuf de départ et est ajouté à la file de priorité ( tas ) 
    visited = set() #sert à initialiser un noeud vide pour enregistrer les noeuds visités pendant la recherche

    while queue:
        cost, current_node = heapq.heappop(queue) #Retire le tuple avec le coût le plus bas de la file queue en utilisant heapq.heappop(). 
        #cost contient le coût actuel du nœud, et current_node contient le nœud actuel.
        if current_node == goal: 
            return cost
        if current_node not in visited: 
            visited.add(current_node) 
            for neighbor, neighbor_cost in graph[current_node]: # Itère à travers tous les voisins du current_node et leurs coûts dans le graphe.
                heapq.heappush(queue, (cost + neighbor_cost, neighbor)) #Ajoute chaque voisin et son coût actualisé à la file queue en utilisant heapq.heappush(). Le nouveau coût est la somme du coût actuel et du coût du voisin.

# Exemple d'utilisation
graph = {'A': [('B', 1), ('C', 3)],
         'B': [('A', 1), ('D', 5)],
         'C': [('A', 3), ('D', 1)],
         'D': [('B', 5), ('C', 1)]}

start_node = 'A'
goal_node = 'D'
print(astar_search(graph, start_node, goal_node))
