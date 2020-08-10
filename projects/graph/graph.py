"""
Simple graph implementation
"""
import copy
from collections import deque

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return [edge for edge in self.vertices[vertex_id]]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        bft_deque = deque([starting_vertex])
        visited = set()
        while len(bft_deque) > 0:
            this_vert = bft_deque.popleft()
            if this_vert not in visited:
                visited.add(this_vert)
                for n in self.get_neighbors(this_vert):
                    if n not in visited:
                        bft_deque.append(n)
                print(this_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        dft_deque = deque([starting_vertex])
        visited = []
        visited_set = set()
        while len(dft_deque) > 0:
            this_vert = dft_deque.pop()
            if this_vert not in visited_set:
                visited.append(this_vert)
                visited_set.add(this_vert)
                for n in self.get_neighbors(this_vert):
                    if n not in visited_set:
                        dft_deque.append(n)
        for v in visited:
            print(v)

    def dft_recursive(self, starting_vertex, vis=False):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if not vis:
            vis = set()
        if starting_vertex not in vis:
            print(starting_vertex)
            vis.add(starting_vertex)
            for n in self.get_neighbors(starting_vertex):
                self.dft_recursive(n, vis)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        paths = []
        bfs_deque = deque([[set([starting_vertex]),[starting_vertex]]])
        while len(bfs_deque) > 0:
            this_state = bfs_deque.popleft()
            print(this_state)
            if this_state[1][-1] == destination_vertex:
                paths.append(this_state[1])
            else:
                for n in self.get_neighbors(this_state[1][-1]):
                    if n not in this_state[0]:
                        new_state = copy.deepcopy(this_state)
                        new_state[0].add(n)
                        new_state[1].append(n)
                        bfs_deque.append(new_state)
        if len(paths) > 0:
            paths.sort(key=len)
            return paths[0]

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        dfs_deque = deque([[set([starting_vertex]), [starting_vertex]]])
        while len(dfs_deque) > 0:
            this_state = dfs_deque.pop()
            if this_state[1][-1] == destination_vertex:
                return this_state[1]
            else:
                for n in self.get_neighbors(this_state[1][-1]):
                    if n not in this_state[0]:
                        new_state = copy.deepcopy(this_state)
                        new_state[0].add(n)
                        new_state[1].append(n)
                        dfs_deque.append(new_state)

    def dfs_recursive(self, starting_vertex, destination_vertex, vis=False):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if not vis:
            vis = set()
        if starting_vertex in vis:
            return None
        elif starting_vertex == destination_vertex:
            return [starting_vertex]
        else:
            vis.add(starting_vertex)
            for n in self.get_neighbors(starting_vertex):
                c = self.dfs_recursive(n, destination_vertex, vis)
                if c:
                    return [starting_vertex].extend(c)
                else:
                    return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
