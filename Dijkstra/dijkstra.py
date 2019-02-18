#!/usr/bin/env python3

import copy

def infty(graph):
    total = 0
    for key in graph:
        for element in graph[key]: #element is a list where the first index is a string, and the second index is a number.
            total += element[1]
    #Divide the total by two because the program counted every edge two times. Add one because of the specifications given.
    if total % 2 == 0: #Assumption: the total is an integer. The result from the operation is either a number in the format X, or format X.5, where X is the integer part.
        total = total / 2 + 1 #If the result is in the format X
    else:
        total = total / 2 + 1.5 #If the result is in the format X.5
    return int(total) #Becuase in Python the result of a division is a floating point, transform the float number in the format X.0, to an integer equal to X

def initial(graph):
    graph_copy = copy.deepcopy(graph)
    coloring = {}
    infinity = infty(graph)
    coloring["A"] = 0 #The specifications define "A" as the first vertex.
    del graph_copy["A"] #Remove "A"
    for key in graph_copy:
        coloring[key] = infinity #Everything else to infinity
    return coloring

def find_min(color, queue):
    vertex = queue[0]
    min = color[vertex]
    for element in queue:
        if color[element] < min:
            min = color[element] #Retrieve the element's value.
            vertex = element #Assign the corresponding vertex.
    return vertex

def dijkstra(graph):
    infinity = infty(graph) #Define what our "infinity" is in this instance.
    visited = [] #This contains all vertices already visited by the algorithm. It is used only as a record of all vertices.
    queue = list(graph.keys()) #Each key is a vertex to be visited.
    queue.sort() #Sort the list of vertices, which is our queue for the Dijkstra algorithm.
    output = initial(graph)
    while queue: #Run as long as the queue is not empty
        current = find_min(output, queue) #Get the next vertex in the queue with lowest value.
        queue.remove(current) #Get it out of the queue.
        for element in queue: #Update the rest of the queue
            weight = infinity #If a vertex in the queue does not have an edge between itself and the current vertex, do not update it.
            for vertex in graph[current]:
                if vertex[0] == element: #Get all elements left in the queue that are linked to the current vertex through an edge.
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
