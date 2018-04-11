def infty(graph):
    total = 0
    for key in graph:
        for element in graph[key]:
            total += element[1]
    if total % 2 == 0:
        total = total / 2 + 1
    else:
        total = total / 2 + 1.5
    return int(total)

def initial(graph):
    coloring = {}
    infinity = infty(graph)
    first = True
    for key in graph:
        if first:
            coloring[key] = 0
            first = False
        else:
            coloring[key] = infinity
    return coloring

def find_min(color, queue):
    vertex = queue[0]
    min = color[vertex]
    for element in queue:
        if color[element] < min:
            min = color[element]
            vertex = element
    return vertex

def dijkstra(graph):
    infinity = infty(graph)
    visited = []
    queue = list(graph.keys())
    queue.sort()
    output = {}
    output[queue[0]] = 0
    for i in range(1, len(queue)):
        output[queue[i]] = infinity
    while queue:
        current = queue[0]
        for element in queue:
            if output[element] < output[current]:
                current = element
        queue.remove(current)
        for element in queue:
            weight = infinity
            for vertex in graph[current]:
                if vertex[0] == element:
                    weight = vertex[1]
            if output[current] + weight < output[element]:
                    output[element] = weight
        visited.append(current)
    return output


def is_connected(graph):
    keys = list(graph.keys())
    connections = [keys[0]]
    for vertex in connections: #Go through the current list of connected vertices. This list increases during the loop, but should stop once there are no more connected vertices. Assumption: the list won't change the order of elements in it during the loop.
        for element in graph[vertex]: #For each vertex in the list of connected vertices, check its edges
            if element[0] not in connections: #If the current edge is between a vertex connected to the graph and a unknown vertex (we do not know if it is connected), then the new vertex is connected to the rest as well.
                connections.append(element[0]) #Append the new vertex, previously unknown, to the list of connected vertices.
    for element in keys: #Comparing the size of the two lists would have been faster, but this is comparing each element for equality, which is safer. Assumption: there could be an undefined behavior and we could have two lists with the same size, but some elements repeated. This prevents such occurency, in exchange for a lot more comparisons.
        if element not in connections:
            return False
    else:
        return True
