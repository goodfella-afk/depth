
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


test = dict()
visited = [] # visited nodes, keep track 
neighborVisited = []
values = []


def df(visited, graph, node):  # definisemo funkciju a za argumente uzimamo promjenjivu visited(listu), sam graf i promjenivu node koju cemo kasnije rekurzivno prosledjivati sa stacka u vidu komsija.
                          
    if node not in visited:                                                         # ako cvor koji provjeravamo vec nije posjecen, onda ga stampamo i smjestamo u visited.
        print (f'{node} -> I SEE {graph.get(node)} -> putting {node} in visited')
        visited.append(node)                                                       # u visited dodajemo trenutni cvor
        print (f'VISITED:{visited}\n')          #vizualizacija liste.
        

        neighborVisited = []
        neigbours = dict(sorted(graph[node].items() , key=lambda item: item[1]))


        for neighbour in neigbours:                                                 # udji u prvog komsiju iz sortirane liste neighbours (prvi value u sortiranoj listi je uvijek najmanji)
                if neighbour not in neighborVisited and neighbour not in visited:   # ako taj komsija vec nije u posjecenim komsijama ili posjecenim cvorovima uopsteno --> dodaj ga u posjecene 
                    neighborVisited.append(neighbour)                               # + u listu test smjesti cijene puteva izabranih komsija sa najmanjom cijenom puta.
                    test[neighbour] =  graph[node][neighbour]                       # u test smjesti cvor u koji ulazis i njegovu cijenu puta kao value.
                    df(visited, graph, neighbour)                                   # rekurzivno pozovi funkciju, proslijedi visited graph i ODABRANOG komsiju.
           

# main

print ('Unesite startni cvor: S,D,A,E,B,F,G,C: ')                
x = input('')                                                          # u x smijestamo cvor iz kog zelimo da pocnemo pretragu grafa, takodje ovaj x proosledjujemo kao argument funkciji za pocetnu nodu.
print ('Unesite cvor do kod zelite da stignete: S,D,A,E,B,F,G,C: ')
y = input('')                                                          # y koristimo kao zeljeni krajnji cvor.
df(visited, graph, x)

print ('\n\n')
print ('  ||')
print ('  ||')
print ('  ||')
print ('  \/\n')

for node in visited:               # provjera liste da vidimo u kom pravcu je graf posjecen + "graficki" prikaz 
    if node != y:
        print ('  ', node)
    else:
        break
print ('  ', y, '    KRAJ\n')

# ---------------------------------------------||
#          DOBIJANJE UKUPNE CIJENE PUTA        ||
#                                              \/

suma = 0                           
keys = list(test.keys())       # u keys u vidu liste smijestamo kljuceve-cvorove iz gore prethodno kreiranog dictionarija. tj one cvorove koji su imali najmanju cijenu puta 

values=[]                      # values kao prazna lista u koju cemo da stavimo odabrane cvorove, osim poslednjeg.

for key in keys:                # za svaki cvor u predjenim cvorovima
    if key != y:                # ako taj cvor nije finalni tj. onaj do kog trazimo put.
        values.append(key)      # dodaj ga u values                                       OVO RADIMO DA BI korigovali stack od rekurzije jer ista pretrazi citav graf najmanjim putevima. 
    else:                       # ako jeste izadji iz petlje                              i na kraju u values imamo cvorove koji trebaju, tj. imamo puteve op1,op2,op3 ...
        break

# print('kljucevi',values)

for item in test:                          # za svaki cvor od prodjenih cvorova 
    if item in values or item == y:         # ako je taj cvor u listi values, (ako nisu prvi i poslednji onih koje smo odabrali za pretragu)
        suma = suma + test[item]            # njihove vrijednosti sumiraj.

print('UKUPNA CIJENA OVOG PUTA JE: ',suma)
