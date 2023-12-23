import networkx as nx

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    unvisited_vertices = set(graph.keys())

    while unvisited_vertices:
        current_vertex = min(unvisited_vertices, key=lambda vertex: distances[vertex])
        unvisited_vertices.remove(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    # Verifica ciclos negativos corretamente
    for _ in range(len(graph)):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distances[vertex] + weight < distances[neighbor]:
                    raise ValueError("Graph contains negative cycles")

    return distances


def main():
    # Exemplo de uso do algoritmo
    graph = {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2, 'D': 5}, 'C': {'A': 4, 'B': 2, 'D': 1}, 'D': {'B': 5, 'C': 1}}
    start_vertex = 'A'
    result = dijkstra(graph, start_vertex)

    G = nx.Graph()

    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(vertex, neighbor, weight=weight)

    shortest_lengths = nx.shortest_path_length(G, source=start_vertex, weight='weight')

    #nx_func = nx.shortest_path_length()
    print("Resultado do algoritmo: ", result, "\nResultado pelo Networkx: ", shortest_lengths)


if __name__ == "__main__":
    main()