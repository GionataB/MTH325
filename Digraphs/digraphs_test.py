import digraphs_relations

#testing is_reflex
print("------ REFLEXIVE RELATION ------")
ground = ["A","B","C","D","E"]
relation = [["A","A"],["A","D"],["B","C"],["B","D"],["C","E"],["D","A"],["E","E"]]
print(digraphs_relations.is_reflex(ground, relation)) # False
print("FALSE")
ground = ["A", "B", "C"]
relation = [["A", "A"], ["A", "B"], ["A", "C"], ["B", "B"], ["B", "A"], ["C", "C"], ["C", "A"]]
print(digraphs_relations.is_reflex(ground, relation)) # True
print("TRUE")

#test is_sym
print("------ SYMMETRIC RELATION ------")
ground = ["A","B","C","D","E"]
relation = [["A","A"],["A","D"],["B","C"],["B","D"],["C","E"],["D","A"],["E","E"]]
print(digraphs_relations.is_sym(ground, relation)) #False
print("FALSE")
ground = ["A", "B", "C"]
relation = [["A", "A"], ["A", "B"], ["A", "C"], ["B", "B"], ["B", "A"], ["C", "C"], ["C", "A"]]
print(digraphs_relations.is_sym(ground, relation)) #True
print("TRUE")

#test is_antisym
print("------ ANTI-SYMMETRIC RELATION ------")
ground = ["A","B","C","D","E"]
relation = [["A","A"],["A","D"],["B","C"],["B","D"],["C","E"],["D","A"],["E","E"]]
print(digraphs_relations.is_antisym(ground, relation)) #False
print("FALSE")
ground = ["A","B","C","D"]
relation = [["A","A"],["A","B"],["A","C"],["A","D"],["B","D"],["C","D"],["C","C"]]
print(digraphs_relations.is_antisym(ground, relation)) #True
print("TRUE")

#test is_trans
print("------ TRANSITIVE RELATION ------")
ground = ["A","B","C","D","E"]
relation = [["A","A"],["A","D"],["B","C"],["B","D"],["C","E"],["D","A"],["E","E"]]
print(digraphs_relations.is_trans(ground, relation)) #False
print("FALSE")
ground = ["A","B","C","D"]
relation = [["A","A"],["A","B"],["A","C"],["A","D"],["B","D"],["C","D"],["C","C"]]
print(digraphs_relations.is_trans(ground, relation)) #True
print("TRUE")


#test trans_clos
print("------ TRANSITIVE CLOSURE ------")
test = {"A" : ["B"],"B" : ["C"],"C" : ["B"],"D" : ["A","C"]}
correct = {"A" : ["B","C"],"B" : ["B", "C"], "C" : ["B", "C"], "D" : ["A", "B", "C"]}
print(digraphs_relations.trans_clos(test))
print(correct)
test = {"A" : ["B", "C"], "B" : ["A"], "C" : ["A"]}
correct =  {"A" : ["A", "B", "C"], "B" : ["A", "B", "C"], "C" : ["A", "B", "C"]}
print(digraphs_relations.trans_clos(test))
print(correct)
