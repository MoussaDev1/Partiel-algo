def djikstra(graph, start):
    # Initialisation
    # On initialise les distances à l'infini et previous à None
    distance_parcourus = {node: float('inf') for node in graph}
    previous_city = {node: None for node in graph}
    city_visited = set()
    distance_parcourus[start] = 0

    # Boucle principale pour visiter tous les noeuds
    while len(city_visited) < len(graph):
        current_city = None
        current_distance_parcourus = float('inf')

        # Recherche du noeud non visité avec la plus petite distance
        for city in graph:
            if city not in city_visited and distance_parcourus[city] < current_distance_parcourus:
                # Met à jour le noeud de l'itération en cours et sa distance
                current_city = city
                current_distance_parcourus = distance_parcourus[city]   
        if current_city is None:
            break
        else: 
            # Marque le noeud comme visité
            city_visited.add(current_city)

        # Met à jour les distances des voisins du noeud courant
        for neighbor, weight in graph[current_city]:
            new_distance_parcourus = distance_parcourus[current_city] + weight

            # Relaxation(Si la nouvelle distance est plus petite, on met à jour pour avoir le plus court chemin)
            if new_distance_parcourus < distance_parcourus[neighbor]:
                distance_parcourus[neighbor] = new_distance_parcourus
                previous_city[neighbor] = current_city
        
    paths = {}
    for city in graph:
        path = []
        current = city
        while current is not None:
            path.insert(0, current)
            # Remonte le chemin en utilisant previous_city
            current = previous_city[current]
        paths[city] = path
    return distance_parcourus, paths

#Utilisation
graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("C", 5), ("D", 10)],
    "C": [("E", 3)],
    "D": [("F", 11)],
    "E": [("D", 4)],
    "F": []
}
if __name__ == "__main__":
    start_city = "A"
    end_city = "F"
    
    distances, paths = djikstra(graph, start_city)
    print("Distances from start city to end city:", distances[end_city])
    print("Paths from start city to end city:", paths[end_city])

