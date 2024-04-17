import networkx as nx
import multiprocessing
import time

def dfs(graph, start_node, end_node, visited, path):
    visited.add(start_node)
    path.append(start_node)

    if start_node == end_node:
        return True

    for neighbor in graph.neighbors(start_node):
        if neighbor not in visited:
            if dfs(graph, neighbor, end_node, visited, path):
                return True

    path.pop()
    return False

def dfs_subgraph(graph, start_node, end_node, result_queue):
    visited = set()
    path = []
    dfs(graph, start_node, end_node, visited, path)
    result_queue.put(path)

if __name__ == "__main__":
    # Crear un grafo de ejemplo
    grafo = nx.Graph()
    grafo.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (1, 5), (3, 5)])

    start_node = 1
    end_node = 4
    num_processes = multiprocessing.cpu_count()

    # DFS sin multiprocessing
    start_time = time.time()
    visited = set()
    path = []
    dfs(grafo, start_node, end_node, visited, path)
    end_time = time.time()
    print(f"Camino encontrado (sin multiprocessing): {path if path else 'No se encontró'}")
    print(f"Tiempo de ejecución (sin multiprocessing): {end_time - start_time} segundos")

    # DFS con multiprocessing
    start_time = time.time()
    result_queue = multiprocessing.Queue()
    processes = []
    for _ in range(num_processes):
        process = multiprocessing.Process(target=dfs_subgraph, args=(grafo, start_node, end_node, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    while not result_queue.empty():
        path = result_queue.get()
        if path:
            print(f"Camino encontrado (con multiprocessing): {path}")
            break
    else:
        print("No se encontró un camino (con multiprocessing)")
    end_time = time.time()
    print(f"Tiempo de ejecución (con multiprocessing): {end_time - start_time} segundos")
