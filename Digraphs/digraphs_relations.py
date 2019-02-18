#!/usr/bin/env python3

import copy

def is_reflex(ground, relation):
    for element in ground:
        compare_list = [element, element]
        if compare_list not in relation:
            return False
    else: #If the for loop ends succesfully, then the relation is reflexive.
        return True

def is_sym(ground, relation):
    relation_copy = copy.deepcopy(relation)  #A copy is made to avoid changing the original relation. Technically python passes parameters by value, making a local copy of them. This is only a safe guard for some unexpected, or impossible even, behavior.
    for element in relation_copy: #Get pair (a,b)
        compare_list = [element[1], element[0]] #Make a fake pair with (b,a)
        if compare_list not in relation_copy: #Check that the fake pair is in the relation.
            return False
        else:
            relation_copy.remove(compare_list) #If (a,b) and (b,a) are part of the list, remove (b,a) so that it won't be used in the future iterations. This should optimize the method, making it slightly faster. I am not removing (a,b) because I don't want any unexpected behavior. One such example is the pointer now pointing to the element next the one deleted, resulting in the loop 'skipping' over an element.
    else:
        return True

def is_antisym(ground, relation):
    relation_copy = copy.deepcopy(relation)
    for element in relation_copy: #Get pair (a,b)
        compare_list = [element[1], element[0]] #Make a fake pair with (b,a).
        if compare_list in relation_copy: #Check that the fake pair is in the relation.
            if element[1] != element[0]: #If b is not equal to a, then the relation is not antisymmetric
                return False
            else:
                relation_copy.remove(compare_list) #Take the fake pair out of the list to not use it in the loop, since we already checked it.
    else:
        return True

def is_trans(ground, relation):
    for element in relation: #Get pair (a,b)
        for second_element in relation: #Get pair (d,c)
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
