import numpy as num

graph = {
'a' : ['b','c','d'],
'b' : ['d'],
'c' : ['a','d'],
'd' : ['a','c']
}

iterationNo = 7

print("Graph")
print(graph)

A = []

for i in graph.keys():
    a = []
    for j in graph.keys():
        if(graph[j].count(i)!=0):
            a.append(1/len(graph[j]))
        else:
            a.append(0)
    A.append(a)

print("Page rank Matrix")
for i in A:
    for j in i:
        print(j,' ',end=" "),
    print('')

B = []

for i in range(0,len(A)):
    B.append([1])

print("Iteration Table")
print("Iteration 1:\n")
print(B)

for i in range(0,iterationNo):
    B = num.matmul(A,B)
    print("\nIteration " + str(i+2) + ":\n")
    print(B)