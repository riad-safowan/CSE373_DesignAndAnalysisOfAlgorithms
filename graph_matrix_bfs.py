from collections import deque

from graph_drawer import draw_graph


def init_graph(num_of_nodes, value):
    return [[value] * num_of_nodes for _ in range(num_of_nodes)]


def print_graph(graph):
    print("The graph: ")
    for row in graph:
        for i in row:
            print(i, end=" ")
        print()


def bfs(graph, start_node):
    visited = [False] * len(graph)
    queue = deque([start_node])
    visited[start_node] = True

    print("BFS traversal:")
    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")

        for i, hasEdge in enumerate(graph[current_node]):
            if hasEdge and not visited[i]:
                queue.append(i)
                visited[i] = True
    print()


def bfs_shortest_path(graph, start_node, end_node):
    visited = [False] * len(graph)
    parents = [-1] * len(graph)  # Initialize an array to store parents, -1 indicates no parent
    queue = deque([start_node])
    visited[start_node] = True

    while queue:
        current_node = queue.popleft()

        for neighbor, has_edge in enumerate(graph[current_node]):
            if has_edge and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                parents[neighbor] = current_node

                if neighbor == end_node:
                    print_path(parents, end_node, end_node)
                    return


def print_path(parents, end_node, last):
    if end_node == -1:
        return
    print_path(parents, parents[end_node], last)
    if end_node != last:
        print(end_node, end=" -> ")
    else:
        print(end_node)
    return


# start point
num_of_nodes = int(input("Enter the number of nodes: "))
num_of_edges = int(input("Enter the number of edges: "))

graph = init_graph(num_of_nodes, 0)

# add edges
for i in range(num_of_edges):
    print(f'Enter edge {i + 1}:')
    edge_input = input().split()
    source_node, destination_node = map(int, edge_input)
    graph[source_node][destination_node] = 1

# print the graph
draw_graph(graph)

# perform BFS
start_node = int(input("Enter the starting node for BFS: "))
end_node = int(input("Enter the end node for finding the shortest path: "))
bfs(graph, start_node)
bfs_shortest_path(graph, start_node, end_node)


# input

# 5
# 5
# 0 1
# 0 2
# 1 3
# 3 4
# 2 4
# 0
# 4

# 5
# 7
# 0 1
# 0 2
# 1 2
# 1 3
# 2 3
# 3 4
# 4 0
# 0
# 4