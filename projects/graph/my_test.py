from graph import Graph
from collections import deque

my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)
my_graph.add_vertex(5)
my_graph.add_vertex(6)
my_graph.add_vertex(7)

my_graph.add_edge(5, 3)
my_graph.add_edge(6, 3)
my_graph.add_edge(7, 1)
my_graph.add_edge(4, 7)
my_graph.add_edge(1, 2)
my_graph.add_edge(7, 6)
my_graph.add_edge(2, 4)
my_graph.add_edge(3, 5)
my_graph.add_edge(2, 3)
my_graph.add_edge(4, 6)

def dfs_recursive(starting_vertex, destination_vertex, path=[]):
    path.append(starting_vertex)
    if starting_vertex == destination_vertex:
        return path
    for n in my_graph.get_neighbors(starting_vertex):
        if n not in path:
            dfs_recursive(n, destination_vertex, path)
            if path[-1] == destination_vertex:
                return path
            else:
                path.pop()

c = dfs_recursive(1, 4)
print(c)