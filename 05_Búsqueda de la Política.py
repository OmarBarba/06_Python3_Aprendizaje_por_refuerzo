import random

# Definir el grafo como un diccionario de adyacencia
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': ['I'],
    'G': ['J'],
    'H': ['K'],
    'I': ['J'],
    'J': ['K'],
    'K': ['L'],
    'L': []
}

def policy_search(graph, start, goal):
    current_node = start
    path = [current_node]

    while current_node != goal:
        neighbors = graph.get(current_node, [])
        # En este ejemplo, la política es elegir un vecino al azar
        if neighbors:
            next_node = random.choice(neighbors)
        else:
            break  # No hay vecinos disponibles, detener la búsqueda

        path.append(next_node)
        current_node = next_node

    return path

start_node = 'A'
goal_node = 'L'

path = policy_search(graph, start_node, goal_node)

print("Camino encontrado con búsqueda de política:", path)
