import dijkstra

#test infty
print("------ INFINITY ------")
test = {"A":[["B",10],["D",5]],"B":[["A",10],["C",5]],"C":[["B",5],["D",15]],"D":[["C",15],["A",5]]}
print(dijkstra.infty(test)) #36
print("36")

#test initial
print("------ INITIAL ------")
test = {"A":[["B",10],["D",5]],"B":[["A",10],["C",5]],"C":[["B",5],["D",15]],"D":[["C",15],["A",5]]}
correct = {"A" : 0, "B" : 36, "C" : 36, "D" : 36}
print(dijkstra.initial(test))
print(correct)

#test find_min
print("------ FIND MINIMUM ------")
color = {"A" : 0, "B" : 10, "C" : 10, "D" : 15}
queue = ["A", "D"]
print(dijkstra.find_min(color, queue)) #"A"
print("A")
color = {"A" : 0, "B" : 10, "C" : 10, "D" : 15}
queue = ["B", "C", "D"]
print(dijkstra.find_min(color, queue))
print("B or C")


#test dijkstra
print("------ DIJKSTRA ------")
test = {"A":[["B",10],["D",5]],"B":[["A",10],["C",5]],"C":[["B",5],["D",15]],"D":[["C",15],["A",5]]}
correct = {"A" : 0,"B" : 10,"C" : 15,"D" : 5}
print(dijkstra.dijkstra(test))
print(correct)
test = {"A": [["B",10],["D",5]], "B": [["A",10], ["C",5]], "C": [["B",5],["D",15]],"D":[["C",15],["A",5]],
    "E": [["F",5]], "F": [["E",5]]}
correct = {"A" : 0,"B" : 10,"C" : 15,"D" : 5,"E" : 41,"F" : 41}
print(dijkstra.dijkstra(test))
print(correct)
test = {'A':[['B',35], ['C', 10]], 'B':[['A', 35], ['D', 10]], 'C':[['A',10], ['D',5]], 'D':[['B',10], ['C',5],
 ['E', 5]], 'E':[['D',5]]}
correct = {'A':[['B',5], ['C', 20]], 'B':[['A', 5], ['C', 5]], 'C':[['A',20], ['B',5]], 'D':[['E',5], ['F',5]],
'E':[['D',5], ['F',5]], 'F':[['E',5], ['F',5]]}
print(dijkstra.dijkstra(test), dijkstra.dijkstra(correct))
print(correct)

#test is_connected
print("------ CONNECTED GRAPHS ------")
test = {"A" : [["B", 10], ["D", 5]], "B" : [["A", 10], ["C", 5]], "C" : [["B", 5], ["D", 15]],
"D" : [["C", 15], ["A", 5]]}
print(dijkstra.is_connected(test)) #True
print("TRUE")
test = {"A" : [["B", 5], ["C", 5]], "B" : [["A", 5], ["C", 5]], "C" : [["B", 5], ["A", 15]], "D" :
[["E", 5]], "E" : [["D",5]]}
print(dijkstra.is_connected(test)) #False
print("FALSE")
