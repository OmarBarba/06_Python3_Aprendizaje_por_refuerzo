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

def explore_vs_exploit(graph, start, goal, exploration_prob):
    current_node = start
    path = [current_node]

    while current_node != goal:
        neighbors = graph.get(current_node, [])
        if random.random() < exploration_prob and neighbors:
            # Explorar aleatoriamente eligiendo un vecino al azar
            next_node = random.choice(neighbors)
        else:
            # Explotar eligiendo el vecino más corto
            neighbors.sort(key=lambda node: len(path + [node]))
            next_node = neighbors[0]

        path.append(next_node)
        current_node = next_node

    return path

start_node = 'A'
goal_node = 'L'
exploration_prob = 0.2  # Probabilidad de exploración (ajustable)

path = explore_vs_exploit(graph, start_node, goal_node, exploration_prob)

print("Camino encontrado con exploración vs. explotación:", path)
