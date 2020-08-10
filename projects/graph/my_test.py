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

dfs_deque = deque()
dfs_deque.append([1])
while dfs_deque[0] is not [None]:
    print("Deque: ", dfs_deque)
    this_path = dfs_deque.pop()
    print("Popped: ", this_path)
    print("New deque: ", dfs_deque)
    if this_path[-1] == 6:
        print("Done")
        break
    else:
        for n in my_graph.get_neighbors(this_path[-1]):
            print("Neighbor: ", n)
            if n not in this_path:
                dfs_deque.append(this_path[:].extend([n]))
                print("New: ", dfs_deque)