# deklarisemo graf u vidu dictionarija
# tako da svakom kljucu(cvoru, tj. nodi) dodijelimo-pokazemo SAMO value-susjedne cvorove koje vidi.

graph = {

    'S': {'D':10, 'A':3},    # S vidi D i A
    'D': {'E':2,'S':10,'B':6,'A':5},    # etc
    'A': {'D':5, 'B':4,'S':3},      
    'E': {'F':4,'D':2},
    'B': {'C':2,'A':4,'D':6},
    'F': {'G':3,'E':4},
    'G': {'F':3},
    'C': {'B':2}
}


print ('\n')

visited = [] # visited nodes, keep track 

def df(visited, graph, node):  # definisemo funkciju a za argumente uzimamo promjenjivu visited(listu), sam graf i promjenivu node koju cemo kasnije rekurzivno prosledjivati sa stacka u vidu komsija.
                               
    if node not in visited:     # ako cvor koji provjeravamo vec nije posjecen, onda ga stampamo i smjestamo u visited.
        print (f'{node} -> I SEE {graph.get(node)} -> putting {node} in visited')
        visited.append(node)                                                       # u visited dodajemo trenutni cvor
        print (f'VISITED:{visited}\n')          #vizualizacija liste.
        
        
                                # udji u prvi sledeci cvor koji trenutni cvor vidi (komsiju, a ostale koje vidis stavi na stack):
            # z = graph[node][neighbour] OVO MI POKAZUJE VRIJEDNOST SAMO PRVOG PUTA
        
        
        min = 1000
        for neighbour in graph[node]:
            for next in graph[node]:
                if graph[next][node] < min:
                    min = graph[next][node]
                    min2 = next
            if min2 not in visited:
                print ('sad cu da pozovem rekurz')                     # ako taj cvor nismo ranije posjetili rekurzivno pozovi df a ako jesmo vrati se na pocetak steka i nastavi dalje.
                df(visited, graph, min2)
        
            


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


#TEST

# z = graph[node][neighbour] OVO MI POKAZUJE VRIJEDNOST SAMO PRVOG PUTA
            # for next in graph[neighbour]:                     
            #     print ('ovo je', next, 'komsija i vrijednost mu je ', graph[next][neighbour])

            #OVIM PRIKAZUJEM VRIJEDNOST SVAKOG SLEDECEG KOMSIJE 

