from collections import deque

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

def bfs_active_reinforcement(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        visited.add(node)

        if node == goal:
            return path

        # Aquí, el agente puede tomar decisiones activas
        # En este ejemplo, se elige el siguiente nodo no visitado en orden alfabético.
        neighbors = sorted([n for n in graph.get(node, []) if n not in visited])

        for neighbor in neighbors:
            new_path = path + [neighbor]
            queue.append((neighbor, new_path))

    return None

start_node = 'A'
goal_node = 'L'

path = bfs_active_reinforcement(graph, start_node, goal_node)

if path:
    print("Camino encontrado:", path)
else:
    print("No se encontró un camino.")

# Puedes implementar estrategias de decisión más sofisticadas para el agente,
# como selección basada en información heurística, políticas epsilon-greedy, etc.
