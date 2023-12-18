import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(adjacency_matrix):
    G = nx.Graph()

    num_nodes = len(adjacency_matrix)
    G.add_nodes_from(range(num_nodes))

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if adjacency_matrix[i][j] == 1:
                G.add_edge(i, j)
            elif adjacency_matrix[i][j] == -1:
                G.add_edge(j, i)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10, edge_color='gray', linewidths=1, alpha=0.7)
    plt.show()

# Example usage
adj_matrix = [
    [0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0]
]

draw_graph(adj_matrix)
