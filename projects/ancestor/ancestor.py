
from collections import deque

def earliest_ancestor(ancestors, starting_node):
    # Connections will be *reversed*: each node links to its *parents*
    vertices = {}
    for parent, child in ancestors:
        if child in vertices:
            vertices[child].add(parent)
        else:
            vertices[child] = set([parent])
        if parent not in vertices:
            vertices[parent] = set()
    def get_parents(node):
        return [parent for parent in vertices[node]]
    if len(get_parents(starting_node)) == 0:
        return -1
    def trace_back(node, steps=0, candidates=[]):
        parents = get_parents(node)
        if len(parents) == 0:
            return candidates.append((node, steps))
        else:
            for parent in parents:
                trace_back(parent, steps+1, candidates)
            return candidates
    possibles = sorted(trace_back(starting_node), key=lambda tup: tup[1], reverse=True)
    farthest = sorted([poss[0] for poss in possibles if poss[1] == possibles[0][1]])[0]
    return farthest