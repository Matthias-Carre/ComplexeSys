import argparse

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
    

def main(file_path):
    print(f"fichier etudier: {file_path}")
    graph = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            (s1,s2) = (int(line.split(" ")[0]),int(line.split(" ")[1][0:-1]))
            graph.append((s1,s2))
    liste_adjacence(graph)

    


    # Ajoutez ici le code pour traiter le fichier

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Graph Analyst")
    parser.add_argument('file', type=str, help='Path to the input file')
    args = parser.parse_args()
    
    main(args.file)