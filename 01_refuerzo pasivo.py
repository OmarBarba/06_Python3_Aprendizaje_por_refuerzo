from collections import deque

def bfs_with_positive_reinforcement(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        visited.add(node)

        if node == goal:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    return None

def apply_positive_reinforcement(graph, path, reward):
    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]
        if current_node in graph and next_node in graph[current_node]:
            # Incrementa la recompensa positiva en el enlace entre nodos
            graph[current_node][next_node] += reward
        else:
            # Inicializa la recompensa positiva en el enlace entre nodos
            graph[current_node][next_node] = reward

# Ejemplo de grafo (diccionario de adyacencia con recompensas)
graph = {
    'A': {'B': 0},
    'B': {'D': 0, 'E': 0},
    'C': {'F': 0},
    'D': {'G': 0},
    'E': {'H': 0},
    'F': {'I': 0},
    'G': {'J': 0},
    'H': {'K': 0},
    'I': {'J': 0},
    'J': {'K': 0},
    'K': {'L': 0},
    'L': {}
}

start_node = 'A'
goal_node = 'L'

# Realizar la búsqueda en el grafo
path = bfs_with_positive_reinforcement(graph, start_node, goal_node)

if path:
    print("Camino encontrado:", path)
    # Aplicar recompensas positivas al camino encontrado
    apply_positive_reinforcement(graph, path, reward=1)
else:
    print("No se encontró un camino.")

# Mostrar el grafo actualizado con las recompensas positivas
print("Grafo con recompensas positivas:")
for node, neighbors in graph.items():
    print(f"{node}: {neighbors}")
