import math

def distance_euclidienne(a, b, coords):
    # Calcule la distance euclidienne entre deux points a et b qui ont des coordonnées dans coords
    x1, y1 = coords[a]
    x2, y2 = coords[b]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def astar(graph, start, goal, coords):
    distance_parcourus = {node: float('inf') for node in graph}
    previous_city = {node: None for node in graph}
    city_visited = set()
    distance_parcourus[start] = 0

    while len(city_visited) < len(graph):
        current_city = None
        current_f = float('inf')


        for city in graph:
            if city not in city_visited:
                g = distance_parcourus[city]
                h = distance_euclidienne(city, goal, coords)
                f = g + h
                if f < current_f:
                    current_city = city
                    current_f = f

        if current_city is None:
            break

        if current_city == goal:
            break

        city_visited.add(current_city)

        for neighbor, weight in graph[current_city]:
            new_distance = distance_parcourus[current_city] + weight
            if new_distance < distance_parcourus[neighbor]:
                distance_parcourus[neighbor] = new_distance
                previous_city[neighbor] = current_city

    path = []
    current = goal
    while current is not None:
        path.insert(0, current)
        current = previous_city[current]

    return distance_parcourus, path

#Utilisation :
if __name__ == "__main__":
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("C", 5), ("D", 10)],
        "C": [("E", 3)],
        "D": [("F", 11)],
        "E": [("D", 4)],
        "F": []
    }

    # emplacement des villes (fictifs)
    coords = {
        "A": (0, 0),
        "B": (2, 3),
        "C": (3, 1),
        "D": (6, 2),
        "E": (4, 3),
        "F": (8, 4)
    }

    start_city = "A"
    end_city = "F"

    distances, path = astar(graph, start_city, end_city, coords)

    print(f"Distance totale estimée de {start_city} à {end_city} : {distances[end_city]}")
    print(f"Chemin le plus court : {' -> '.join(path)}")
