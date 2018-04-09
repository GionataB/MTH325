def infty(graph):
    total = 0
    for key in graph:
        for element in graph[key]:
            total += element[1]
    return total

def initial(graph):
    coloring = {}
    infinity = infty(graph)
    first = true
    for key in graph:
        coloring[key] = []
        for element in graph[key]:
            if first:
                coloring[key] = 1
                first = false
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
    source = "A" #This is the source for any graph of the dijkstra algorithm.
    infinity = infty(graph)
    vertices_to_use = list(graph.keys()).order()
    shortest_distance = {}
    for vertex in vertices_to_use:
        shortest_distance[vertex] = infinity
    shortest_distance[source] = 0
    vertices_visited = [source]
    vertices_to_use.remove(source)
    for vertex in vertices_visited:
        for element in graph[vertex]:
            if element not in vertices_visited: #Check that the vertices being updated have not been visited
                if shortest_distance[vertex] + element[1] < shortest_distance[element[0]]: #Check if the vertex should be updated with a new value, if the new value is lower than the current one.
                    shortest_distance[element[0]] += shortest_distance[vertex] + element[1]
        if not vertices_visited: #If the queue is empty, exit the loop, because every vertex has been visited.
            break
        minimum = infinity #The initial minimum is always the highest value.
        for key in shortest_distance:
            if key not in vertices_visited: #The vertex has not been visited.
                if shortest_distance[key] < minimum:
                    minimum = shortest_distance[key]
                    new_vertex = key
        else:
            vertices_visited.append(new_vertex)
            vertices_to_use.remove(new_vertex)
    return shortest_distance






def is_connected(graph):
    keys = list(graph.keys())
    connections = [keys[0]]
    for vertex in connections: #Go through the current list of connected vertices. This list increases during the loop, but should stop once there are no more connected vertices. Assumption: the list won't change the order of elements in it during the loop.
        for element in graph[vertex]: #For each vertex in the list of connected vertices, check its edges
            if element[0] not in connections: #If the current edge is between a vertex connected to the graph and a unknown vertex (we do not know if it is connected), then the new vertex is connected to the rest as well.
                connections.append(element[0]) #Append the new vertex, previously unknown, to the list of connected vertices.
    for element in connections: #Comparing the size of the two lists would have been faster, but this is comparing each element for equality, which is safer. Assumption: there could be an undefined behavior and we could have two lists with the same size, but some elements repeated. This prevents such occurency, in exchange for a lot more comparisons.
        if element not in keys:
            return False
    else:
        return True
