# deklarisemo graf u vidu dictionarija
# tako da svakom kljucu(cvoru, tj. nodi) dodijelimo-pokazemo SAMO value-susjedne cvorove koje vidi.

graph = {

    'S': ['A','D'],    # S vidi A i D
    'D': ['E','S','B','A'],    # etc
    'A': ['B','S','D'],      
    'E': ['F','D'],
    'B': ['C','A','D'],
    'F': ['G','E'],
    'G': ['F'],
    'C': ['B']
}


print ('\n')

visited = [] # visited nodes, keep track 

def df(visited, graph, node):  # definisemo funkciju a za argumente uzimamo promjenjivu visited(listu), sam graf i promjenivu node koju cemo kasnije rekurzivno prosledjivati sa stacka u vidu komsija.
                               
    if node not in visited:     # ako cvor koji provjeravamo vec nije posjecen, onda ga stampamo i smjestamo u visited.
        print (f'{node} -> I SEE {graph.get(node)} -> putting {node} in visited')
        visited.append(node)                                                       # u visited dodajemo trenutni cvor
        print (f'VISITED:{visited}\n')          #vizualizacija liste.
        
        for neighbour in graph[node]:                        # udji u prvi sledeci cvor koji trenutni cvor vidi (komsiju, a ostale koje vidis stavi na stack):
            if neighbour not in visited:                     # ako taj cvor nismo ranije posjetili rekurzivno pozovi df a ako jesmo vrati se na pocetak steka i nastavi dalje.
                df(visited, graph, neighbour)


# main

print ('Unesite startni cvor: S,D,A,E,B,F,G,C: ')                
x = input('')                                                          # u x smijestamo cvor iz kog zelimo da pocnemo pretragu grafa, takodje ovaj x proosledjujemo kao argument funkciji za pocetnu nodu.
print ('Unesite cvor do kod zelite da stignete: S,D,A,E,B,F,G,C: ')
y = input('')                                                          # y koristimo kao zeljeni krajnji cvor.
df(visited, graph, x)

print ('  ||')
print ('  ||')
print ('  ||')
print ('  \/\n')

for node in visited:                                # provjera liste da vidimo u kom pravcu je graf posjecen + "graficki" prikaz 
    if node != y:
        print ('  ', node)
    else:
        break
print ('  ', y, '    KRAJ')               
