import numpy as np

# Definir el grafo como un diccionario de adyacencia con pesos
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'D': 3, 'E': 2},
    'C': {'F': 5},
    'D': {'G': 2},
    'E': {'H': 3},
    'F': {'I': 1},
    'G': {'J': 2},
    'H': {'K': 2},
    'I': {'J': 3},
    'J': {'K': 1},
    'K': {'L': 2},
    'L': {}
}

# Definir los parámetros de Q-Learning
learning_rate = 0.2
discount_factor = 0.9
num_episodes = 1000

# Inicializar la tabla Q con ceros
nodes = list(graph.keys())
num_nodes = len(nodes)
q_table = np.zeros((num_nodes, num_nodes))

# Mapear nodos a índices para facilitar el acceso a la tabla Q
node_to_index = {node: i for i, node in enumerate(nodes)}

# Función para seleccionar una acción epsilon-greedy
def choose_action(state, epsilon):
    if np.random.uniform(0, 1) < epsilon:
        return np.random.choice(range(num_nodes))
    else:
        return np.argmax(q_table[state, :])

# Entrenamiento con Q-Learning
for episode in range(num_episodes):
    current_node = 'A'
    current_state = node_to_index[current_node]
    epsilon = 1.0 / (episode + 1)

    while current_node != 'L':
        current_state = node_to_index[current_node]
        action = choose_action(current_state, epsilon)

        # Encontrar el siguiente nodo a partir de la acción
        next_node = nodes[action]

        # Calcular la recompensa (negativa del peso de la arista)
        if next_node in graph[current_node]:
            reward = -graph[current_node][next_node]
        else:
            reward = 0  # No hay conexión válida

        # Actualizar la tabla Q
        q_table[current_state, action] = (1 - learning_rate) * q_table[current_state, action] + \
            learning_rate * (reward + discount_factor * np.max(q_table[action, :]))

        current_node = next_node

# Encontrar el camino óptimo
current_node = 'A'
current_state = node_to_index[current_node]
optimal_path = [current_node]

while current_node != 'L':
    current_state = node_to_index[current_node]
    action = np.argmax(q_table[current_state, :])

    # Encontrar el siguiente nodo a partir de la acción
    current_node = nodes[action]
    optimal_path.append(current_node)

print("Camino más corto encontrado por Q-Learning:", optimal_path)
