from graph import Graph

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

print(my_graph.bfs(1,6))