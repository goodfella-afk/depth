graph = {

    'S': {'D':10, 'A':3 },    # S vidi D i A
    'D': {'E':10,'S':2,'B':6,'A':5},    # etc
    'A': {'D':5, 'B':4,'S':3},      
    'E': {'F':4,'D':2},
    'B': {'C':2,'A':4,'D':6},
    'F': {'G':3,'E':4},
    'G': {'F':3},
    'C': {'B':2}
}


min = 1000
for neighbour in graph['D']:
    print ('JA SAM', neighbour, ', a moj value je: ', graph[neighbour]['D'])
    if graph[neighbour]['D'] < min:
        min = graph[neighbour]['D']
        min2 = neighbour
print ('ja sam cvor najmanjeg puta:', min2)