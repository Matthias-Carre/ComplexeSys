import argparse , networkx ,random, matplotlib.pyplot as plt
from collections import deque
import itertools


def parseFile(file_path):
    print(f"fichier etudier: {file_path}")
    graph = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            (s1,s2) = (int(line.split(" ")[0]),int(line.split(" ")[1][0:-1]))
            graph.append((s1,s2))
    return graph


def plusGrandCC(liste_adjacence,depart):#renvoie liste des sommets
    res=[]
    fait=[]
    aFaire=[depart]
    while(len(aFaire)>0):
        sommet=aFaire.pop(0)
        for voisin in liste_adjacence[sommet]:
            if voisin not in fait:
                res.append(liste_adjacence[sommet])
                fait.append(voisin)
                aFaire.append(voisin)
    return res

def distriDegres(liste_adjacence):
    res=[0 for _ in range(len(liste_adjacence))]
    for i in range(len(liste_adjacence)):
        res[len(liste_adjacence[i])]+=1
    return res

def bfs_distances(liste_adjacence, point_de_depart):
    dist = [-1 for _ in range(len(liste_adjacence))]
    dist[point_de_depart] = 0
    file = deque([point_de_depart])


    while file:
        sommet = file.popleft()
        for voisin in liste_adjacence[sommet]:
            if dist[voisin] == -1:
                dist[voisin] = dist[sommet] + 1
                file.append(voisin)

    return dist


def moyenneDistances(liste_adjacence):
    somme=0
    for i in range(len(liste_adjacence)):
        tab = bfs_distances(liste_adjacence,i)
        #on fait la moyenne sur les valeurs accesibles
        c=0
        v=0
        for j in range(len(tab)):
            if tab[j]!=-1:
                c+=1
                v+=tab[j]
        somme+=( v/c )
    print("distance moyenne : ",somme/len(liste_adjacence))

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

    for arrete in graph:
        #print (arrete[0]-1,arrete[1]-1)
        liste_adjacence[arrete[0]-1].append(arrete[1]-1)
        liste_adjacence[arrete[1]-1].append(arrete[0]-1)
    

    return liste_adjacence

def degreMoyen(liste_adjacence):
    listeDegres=[]

    for i in range(len(liste_adjacence)):
        listeDegres.append(len(liste_adjacence[i])) 

    print("degres moyen : ",sum(listeDegres)/len(listeDegres))
    

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
    for i in range(len(liste_adjacence)):
        for voisin1 in liste_adjacence[i]:
            for voisin2 in liste_adjacence[voisin1]:
                if i in liste_adjacence[voisin2]:
                    if i< voisin1 and voisin1<voisin2:
                        nbr += 1
                        
    return nbr

def cliques_taille_4(liste_adjacence):
    nbr = 0
    for noeud in range(len(liste_adjacence)):
        for voisin1 in liste_adjacence[noeud]:
            if voisin1 > noeud:
                for voisin2 in liste_adjacence[noeud]:
                    if voisin2 > voisin1:
                        for voisin3 in liste_adjacence[noeud]:
                            if voisin3 > voisin2:
                                # Vérifier que tous les sommets sont connectés entre eux
                                if (voisin3 in liste_adjacence[voisin1] and
                                    voisin3 in liste_adjacence[voisin2] and
                                    voisin2 in liste_adjacence[voisin1]):
                                    nbr += 1
    return nbr

def cliques_taille_5(liste_adjacence):
    nbr = 0
    for noeud in range(len(liste_adjacence)):
        for voisin1 in liste_adjacence[noeud]:
            if voisin1 > noeud:
                for voisin2 in liste_adjacence[noeud]:
                    if not(voisin2 in liste_adjacence[voisin1]):
                        continue
                    if voisin2 > voisin1:
                        for voisin3 in liste_adjacence[noeud]:
                            if voisin3 > voisin2:
                                if not(voisin3 in liste_adjacence[voisin1] and 
                                    voisin3 in liste_adjacence[voisin2]):
                                    continue
                                for voisin4 in liste_adjacence[noeud]:
                                    if voisin4 > voisin3:
                                        if (voisin4 in liste_adjacence[voisin1] and
                                            voisin4 in liste_adjacence[voisin2] and
                                            voisin4 in liste_adjacence[voisin3] and
                                            voisin3 in liste_adjacence[voisin1] and
                                            voisin3 in liste_adjacence[voisin2] and
                                            voisin2 in liste_adjacence[voisin1]):
                                            nbr += 1
    return nbr

def cliques_taille_6_echantillon(liste_adjacence, sous_ensemble_noeuds):
    nbr = 0
    c=0
    for noeud in sous_ensemble_noeuds:
        """
        c+=1
        if(c%100==0):
            print(c,"il y a ",nbr," clique de 6 soit porportion de : ",nbr/c)
        """
        if len(liste_adjacence[noeud])<6:
            continue
        for voisin1 in liste_adjacence[noeud]:
            if voisin1 > noeud:
                for voisin2 in liste_adjacence[noeud]:
                    if not(voisin2 in liste_adjacence[voisin1]):
                        continue
                    if voisin2 > voisin1:
                        for voisin3 in liste_adjacence[noeud]:
                            if voisin3 > voisin2:
                                if not(voisin3 in liste_adjacence[voisin1] and 
                                    voisin3 in liste_adjacence[voisin2]):
                                    continue
                                for voisin4 in liste_adjacence[noeud]:
                                    if voisin4 > voisin3:
                                        if not(voisin4 in liste_adjacence[voisin1] and
                                            voisin4 in liste_adjacence[voisin2] and
                                            voisin4 in liste_adjacence[voisin3]):
                                            continue
                                        for voisin5 in liste_adjacence[noeud]:
                                            if voisin5 > voisin4:
                                                if (voisin5 in liste_adjacence[voisin1] and
                                                    voisin5 in liste_adjacence[voisin2] and
                                                    voisin5 in liste_adjacence[voisin3] and
                                                    voisin5 in liste_adjacence[voisin4]) :
                                                    nbr += 1
                                                    #print(noeud, voisin1, voisin2, voisin3, voisin4, voisin5)
    return nbr

def cliques_taille_7_echantillon(liste_adjacence, sous_ensemble_noeuds):
    nbr = 0
    c=0
    for noeud in sous_ensemble_noeuds:
        """
        c+=1
        if(c%100==0):
            print(c,"il y a ",nbr," clique de 7 soit porportion de : ",nbr/c)
        """
        for voisin1 in liste_adjacence[noeud]:
            if voisin1 > noeud:
                for voisin2 in liste_adjacence[noeud]:
                    if not(voisin2 in liste_adjacence[voisin1]):
                        continue
                    if voisin2 > voisin1:
                        for voisin3 in liste_adjacence[noeud]:
                            if voisin3 > voisin2:
                                if not(voisin3 in liste_adjacence[voisin1] and 
                                    voisin3 in liste_adjacence[voisin2]):
                                    continue
                                for voisin4 in liste_adjacence[noeud]:
                                    if voisin4 > voisin3:
                                        if not(voisin4 in liste_adjacence[voisin1] and
                                            voisin4 in liste_adjacence[voisin2] and
                                            voisin4 in liste_adjacence[voisin3]):
                                            continue
                                        for voisin5 in liste_adjacence[noeud]:
                                            if voisin5 > voisin4:
                                                if not(voisin5 in liste_adjacence[voisin1] and
                                                    voisin5 in liste_adjacence[voisin2] and
                                                    voisin5 in liste_adjacence[voisin3] and
                                                    voisin5 in liste_adjacence[voisin4]):
                                                    continue
                                                for voisin6 in liste_adjacence[noeud]:
                                                    if voisin6 > voisin5:
                                                        if (voisin6 in liste_adjacence[voisin1] and
                                                            voisin6 in liste_adjacence[voisin2] and
                                                            voisin6 in liste_adjacence[voisin3] and
                                                            voisin6 in liste_adjacence[voisin4] and
                                                            voisin6 in liste_adjacence[voisin5]):
                                                            nbr += 1
                                                            #print(noeud, voisin1, voisin2, voisin3, voisin4, voisin5,voisin6)
    return nbr

def cliques_taille_8_echantillon(liste_adjacence, sous_ensemble_noeuds):
    nbr = 0
    
    c=0
    for noeud in sous_ensemble_noeuds:
        """
        c+=1
        if(c%100==0):
            print(c,"il y a ",nbr," clique de 8 soit porportion de : ",nbr/c)
        """
        for voisin1 in liste_adjacence[noeud]:
            if voisin1 > noeud:
                for voisin2 in liste_adjacence[noeud]:
                    if not(voisin2 in liste_adjacence[voisin1]):
                        continue
                    if voisin2 > voisin1:
                        for voisin3 in liste_adjacence[noeud]:
                            if voisin3 > voisin2:
                                if not(voisin3 in liste_adjacence[voisin1] and 
                                    voisin3 in liste_adjacence[voisin2]):
                                    continue
                                for voisin4 in liste_adjacence[noeud]:
                                    if voisin4 > voisin3:
                                        if not(voisin4 in liste_adjacence[voisin1] and
                                            voisin4 in liste_adjacence[voisin2] and
                                            voisin4 in liste_adjacence[voisin3]):
                                            continue
                                        for voisin5 in liste_adjacence[noeud]:
                                            if voisin5 > voisin4:
                                                if not(voisin5 in liste_adjacence[voisin1] and
                                                    voisin5 in liste_adjacence[voisin2] and
                                                    voisin5 in liste_adjacence[voisin3] and
                                                    voisin5 in liste_adjacence[voisin4]):
                                                    continue
                                                for voisin6 in liste_adjacence[noeud]:
                                                    if voisin6 > voisin5:
                                                        if not(voisin6 in liste_adjacence[voisin1] and
                                                            voisin6 in liste_adjacence[voisin2] and
                                                            voisin6 in liste_adjacence[voisin3] and
                                                            voisin6 in liste_adjacence[voisin4] and
                                                            voisin6 in liste_adjacence[voisin5]):
                                                            continue
                                                        for voisin7 in liste_adjacence[noeud]:
                                                            if voisin7 > voisin6:
                                                                if (voisin7 in liste_adjacence[voisin1] and
                                                                    voisin7 in liste_adjacence[voisin2] and
                                                                    voisin7 in liste_adjacence[voisin3] and
                                                                    voisin7 in liste_adjacence[voisin4] and
                                                                    voisin7 in liste_adjacence[voisin5] and
                                                                    voisin7 in liste_adjacence[voisin6]):
                                                                    nbr += 1
                                                                    #print(noeud, voisin1, voisin2, voisin3, voisin4, voisin5,voisin6)
    return nbr


def grapheDegreDist(filename,liste_adjacence,taille):
    valdeg=distriDegres(liste_adjacence)
    valdeg = valdeg[:taille]
    deg = [i for i in range(len(valdeg))]

    plt.figure(figsize=(8, 6))
    plt.bar(deg, valdeg, color='skyblue', edgecolor='black', width=0.6)


    plt.title("Tracé de la distribution des degrés du graphe")
    plt.xlabel("Indices")
    plt.ylabel("Valeurs")
    plt.legend("Distributions des Degres entre 0 et "+str(taille)+" voisins")
    plt.grid(True)
    plt.savefig("Graphes/"+filename)

def coefClusterDeS(liste_adjacence,sommet):
    if len(liste_adjacence[sommet])<2:
        return 0
    nbr=0
    for voisin1 in liste_adjacence[sommet]:
        for voisin2 in liste_adjacence[sommet]:
            if voisin2 in liste_adjacence[voisin1]:
                nbr+=1
    return nbr/(len(liste_adjacence[sommet])*(len(liste_adjacence[sommet])-1))

def coefClusterMoyen(liste_adjacence):
    somme=0
    for i in range(len(liste_adjacence)):
        somme+=coefClusterDeS(liste_adjacence,i)
    print("coefficient de clustering moyen : ",somme/len(liste_adjacence))
    return somme/len(liste_adjacence)

def quatreProp(liste_adjacence,nomDuGraphe):
    degreMoyen(liste_adjacence)
    moyenneDistances(liste_adjacence)
    coefClusterMoyen(liste_adjacence)
    grapheDegreDist(nomDuGraphe+".png",liste_adjacence,40)

def grapheCliquesDistribution(filename,tabEffectif):
    plt.figure(figsize=(6, 7))
    plt.bar(tabEffectif.keys(), tabEffectif.values(), color='skyblue', edgecolor='black', width=0.6)
    plt.title("Tracé de la distribution des cliques")
    plt.yscale("log")
    plt.xlabel("Taille de la clique")
    plt.ylabel("Nombre de clique")
    plt.legend("Distributions des cliques")
    plt.grid(True)
    plt.savefig("Graphes/"+filename)

def cliques(listeAdj):

    t=[i for i in range(len(listeAdj))]
    tb=melangeTab(t)
    res={3:0,4:0,5:0,6:0,7:0,8:0}
    #res[3]=nbrTriangles(listeAdj)
    print("nombre de triangles : ",res[3])
    #res[4]=cliques_taille_4(listeAdj)
    print("cliques de taille 4 : ",res[4])
    #res[5]=cliques_taille_5(listeAdj)
    print("cliques de taille 5 : ",res[5])
    res[6]=cliques_taille_6_echantillon(listeAdj,tb)
    print("cliques de taille 6 : ",res[6])
    res[7]=cliques_taille_7_echantillon(listeAdj,t)
    print("cliques de taille 7 : ",res[7])
    res[8]=cliques_taille_8_echantillon(listeAdj,t)
    print("cliques de taille 8 : ",res[8])
    grapheCliquesDistribution("cliquesReactome.png",res)


def melangeTab(tab):
    res=tab.copy()
    for i in range(len(tab)*10):
        v1=random.randint(0,len(res)-1)
        v2=random.randint(0,len(res)-1)
        res[v1],res[v2]=res[v2],res[v1]
    return res

def main(file_path):
    graph = parseFile(file_path)
    listeAdj = liste_adjacence(graph)


    cliques(listeAdj)


    """
    #nomDuGraphe="Twitter"
    nomDuGraphe="Reactome"
    quatreProp(listeAdj,nomDuGraphe)
    """

    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Graph Analyst")
    parser.add_argument('file', type=str, help='chemin vers le fihier')
    args = parser.parse_args()
    
    main(args.file)