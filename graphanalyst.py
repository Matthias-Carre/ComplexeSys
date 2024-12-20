import argparse


def dijtra(liste_adjacence,depart):
    fait=[]
    aFaire=[]
    distances=[-1 for i in range(len(liste_adjacence))]
    distances[depart]=0
    aFaire.append(depart)
    while len(aFaire)>0:
        sommet=aFaire.pop(0)
        fait.append(sommet)
        for voisin in liste_adjacence[sommet]:
            if voisin not in fait:
                if voisin not in aFaire:
                    aFaire.append(voisin)
                if distances[voisin]==-1 or distances[voisin]>distances[sommet]+1:
                    distances[voisin]=distances[sommet]+1
    return distances
    

def liste_adjacence(graph):
    liste_adjacence=[]
    max=0
    for arrete in graph:
        if arrete[1]>max:
            max=arrete[1]

    for i in range(0,max):
        liste_adjacence.append([])
    print(len(liste_adjacence))
    for arrete in graph:
        #print (arrete[0]-1,arrete[1]-1)
        liste_adjacence[arrete[0]-1].append(arrete[1]-1)
        liste_adjacence[arrete[1]-1].append(arrete[0]-1)
    
    listeDegres=[]
    maxDegre=0
    for i in range(len(liste_adjacence)):
        if len(liste_adjacence[i])>maxDegre:
            maxDegre=len(liste_adjacence[i])
        listeDegres.append(len(liste_adjacence[i])) 
    print("degres moyen : ",sum(listeDegres)/len(listeDegres),"\ndegres max : ",maxDegre)
    return liste_adjacence

def moyennedijtra(liste_adjacence):

    moyennedijtra=[]
    for i in range(1,len(liste_adjacence)):

        dijtradei = dijtra(liste_adjacence,i)

        somme=0
        nombre=0
        for val in dijtradei:
            if val!=-1:
                somme+=val
                nombre+=1
        moyennedijtra.append(somme/nombre)
        print("moyenne dijtra de ",i," : ",(moyennedijtra[i-1]))
    
    distancemoyenne=sum(moyennedijtra)/len(moyennedijtra)
    print("distance moyenne1 : ",distancemoyenne)

    somme=0
    nombre=0
    for val in moyennedijtra:
        somme+=val
        nombre+=1
    print("distance moyenne2 : ",somme/nombre)

        #maxi=0
    #for dj in listofdijtra:
    #    if maxi<max(dj):
    #        maxi=max(dj)
    #print(maxi)

def nbrTriangles(liste_adjacence):
    nbr = 0

    # Parcourir chaque sommet
    for i in range(len(liste_adjacence)):
        # Parcourir chaque voisin du sommet
        for voisin1 in liste_adjacence[i]:
            for voisin2 in liste_adjacence[voisin1]:
                if i in liste_adjacence[voisin2]:
                    if i< voisin1 and voisin1<voisin2:
                        nbr += 1
                        print("triangle")
    return nbr




def main(file_path):
    print(f"fichier etudier: {file_path}")
    graph = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            (s1,s2) = (int(line.split(" ")[0]),int(line.split(" ")[1][0:-1]))
            graph.append((s1,s2))

    listeAdj = liste_adjacence(graph)

    #print(listeAdj)
    #print(nbrTriangles(listeAdj))

    
   
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Graph Analyst")
    parser.add_argument('file', type=str, help='Path to the input file')
    args = parser.parse_args()
    
    main(args.file)