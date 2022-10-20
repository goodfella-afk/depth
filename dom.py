# deklarisemo graf u vidu dictionarija
# tako da svakom kljucu(cvoru, tj. nodi) dodijelimo-pokazemo value-susjedne cvorove koje vidi.

graph = {
    'S': ['D','A'],    # S vidi A i D
    'D': ['E','B'],    # etc
    'A': ['B','D'],      
    'E': ['F'],
    'B': ['C'],
    'F': ['G'],
    'G': [],
    'C': []
}

print ('\n')

visited = set() # visited nodes, keep track 

def df(visited, graph, node):  # definisemo funkciju a za argumente uzimamo posjecene cvorove,
                               #graf, i cvor u kom se trenutno nalazimo
    if node not in visited:
        print (f'{node} -> I SEE {graph.get(node)} -> putting {node} in visited')
        visited.add(node)                                                           # u visited dodajemo trenutni cvor
        print (f'VISITED:{visited}\n')
        if node == 'G':                                                             # ovo je trenutno dok ne smislimo kako prekinuti loop kad nadje G
            print('G FOUNDED, RETURNING IN PARENT NODE\n')
        
        for neighbour in graph[node]:                                       # udji u prvi sledeci cvor koji trenutni cvor vidi:
            if neighbour not in visited:                                    # ako taj cvor nismo ranije posjetili rekurzivno pozovi df.
                df(visited, graph, neighbour)



# call
df(visited, graph, 'S')
