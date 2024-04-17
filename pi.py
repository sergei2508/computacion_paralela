import networkx as nx
import matplotlib.pyplot as plt

# Crea un grafo vacio
grafo = nx.Graph()

grafo.add_node(1)
grafo.add_nodes_from([2, 3])

grafo.add_edge(1, 2)
grafo.add_edges_from([(2, 3), (1, 3)])

print(grafo.nodes())
print(grafo.edges())
print(list(grafo.neighbors(1)))
      
      
nx.draw(grafo, with_labels=True,node_color='red',edge_color='blue', font_weight='bold')
plt.show()
