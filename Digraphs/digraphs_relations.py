import copy

def is_reflex(ground, relation):
    for element in ground:
        compare_list = [element, element]
        if compare_list not in relation:
            return False
    else:
        return True

def is_sym(ground, relation):
    relation_copy = copy.deepcopy(relation)  #A copy is made to avoid changing the original relation. Technically python passes parameters by value, making a local copy of them. This is only a safe guard for some unexpected, or impossible even, behavior.
    for element in relation_copy:
        compare_list = [element[1], element[0]]
        if compare_list not in relation_copy:
            return False
        else:
            relation_copy.remove(compare_list) #If (a,b) and (b,a) are part of the list, remove (b,a) so that it won't be used in the future iterations. This should optimize the method, making it slightly faster. I am not removing (a,b) because I don't want any unexpected behavior. One such example is the pointer now pointing to the element next the one deleted, resulting in the loop 'skipping' over an element.
    else:
        return True

def is_antisym(ground, relation):
    relation_copy = copy.deepcopy(relation)
    for element in relation_copy:
        compare_list = [element[1], element[0]]
        if compare_list in relation_copy:
            if element[1] != element[0]:
                return False
            else:
                relation_copy.remove(compare_list)
    else:
        return True

#The method takes the ground set and relation set of a digraph, and returns wether these relations are transitive.
def is_trans(ground, relation):
    for element in relation: #takes the (a,b) relation
        for second_element in relation: #takes the (d,c) relation
            if element[1] == second_element[0]: #checks that b = d in the previous relations.
                compare_list = [element[0], second_element[1]] #creates a 'fake' (a,c) relation
                if compare_list not in relation: #checks if (a,c) actually exists in the set. if not, we already know the digraph's relation is not transitive.
                    return False
    else:
        return True

def trans_clos(digraph):
    transitive_closure = copy.deepcopy(digraph)
    for key in transitive_closure: #Takes a vertex 'key'.
        for element in transitive_closure[key]: #Takes all the vertices with an arc between them and 'key'
            for vertex in transitive_closure[element]: #Takes all the vertices with an arc between them and 'element'.
                if vertex not in transitive_closure[key]: #If 'key' does not have yet an arc between 'key' and 'vertex', make one.
                    transitive_closure[key].append(vertex) #If 'key' is connected to 'element', and 'element' is connected to 'vertex', then 'key' is connected to 'vertex'. in short, if (a,b) in digraph, and (b,c) in digraph, then (a,c) exists in the transitive closure.
    for key in transitive_closure: #Sort all the lists of vertices for each dict entry, because why not.
        transitive_closure[key].sort()
    return transitive_closure

"""

+++++++++++++++++ The following are prototypes of a Floyd-Warshall algorithm, and a transitive closure retrieved by the Floyd-Warshall output.


#The method takes a digraph as input, and returns a transitive closure of the digraph.
#The algorithm makes use of the Floyd-Warshall algorithm to produce a matrix used to create the transitive closure.
#Assumption: any negative entry in the matrix stands for "infinity".
#Assumption: an entry in the matrix can be zero, and it is considered a valid weight.

def trans_clos(digraph): #FIXME: Floyd_Warshall not needed.
    matrix = Floyd_Warshall(digraph)
    vertices = list(digraph.keys())
    vertices.sort()
    trans_closure = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            arcs = []
            if matrix[i][j] >= 0: #It should never be zero, either negative or positive, but I assume that, if it could be zero, then there is an arc.
                arcs.append(vertices[j])
        else:
            trans_closure[vertices[i]] = arcs
    return trans_closure

#The Floyd-Warshall algorithm takes a digraph as input, and returns the shortest weighted distance between any pair of vertices.
#This will NOT produce a transitive closure.
#Assumption: if the digraph does not have any weighted arc, then the weight for each arc is one.
#Assumption: because the algorithm sums values in various cells, the total could be any positive integer. Thus, "infinity" is represented by '-1' or, in general, any negative number.

def Floyd_Warshall(digraph):
    vertices = list(digraph.keys())
    vertices.sort()
    matrix = []
    for i in range(len(vertices)):
        key = vertices[i]
        matrix.append([])
        for j in range(len(vertices)):
            matrix[i].append(-1) #if the element in digraph has an empty list, this will prevent the matrix[i][j] to be zero.
            if vertices[j] in digraph[key]:
                matrix[i][j] = 1
    for k in range(len(vertices)):
        for i in range(len(matrix)):
            if i == k: #If the selected cell is part of the row "k", skip this iteration.
                continue
            for j in range(len(matrix[i])):
                if j == k: #If the selected cell is part of the column "k", skip this iteration.
                    continue
                if matrix[i][k] < 0 or matrix[k][j] < 0: #If the value in those two cells is "infinity", then skip this iteration.
                    continue
                elif matrix[i][k] + matrix[k][j] < matrix [i][j]: #If the sum is lower than the current value, update the cell.
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    print(matrix) #FIXME
    return matrix
"""
