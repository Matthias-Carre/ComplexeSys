
import networkx as nx
import matplotlib.pyplot as plt

def parseFile(file_path):
    print(f"fichier etudier: {file_path}")
    graph = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            (s1,s2) = (int(line.split(" ")[0]),int(line.split(" ")[1][0:-1]))
            graph.append((s1,s2))
    return graph

def indicesAA(G):
    scores = []
    edges = list(G.edges())
    res = {}
    
    for u, v in edges:
        G.remove_edge(u, v)
        
        #Adamic-Adar
        indexs = nx.adamic_adar_index(G, [(u, v)])
        for _, _, score in indexs:
            res[(u, v)] = score
        G.add_edge(u, v)
    valmax = max(res.values()) 
    val=[]
    for lien, score in res.items():
        val.append(score/valmax)

    return val


def plot_predictability_ranking(probas):
    filename = "predictability_ranking.png"
    tabX=[i/100 for i in range(len(probas))]
    tabY=probas
    plt.figure(figsize=(12, 8))
    plt.bar(tabX,tabY, color='skyblue', edgecolor='black', width=0.006)
    plt.title("Graphique de la probabilité de prédiction")
    plt.yscale("log")
    plt.xlabel("Probabilite")
    plt.ylabel("effectif")
    plt.legend("")
    plt.grid(True)
    plt.savefig("Graphes/linkPrediction.png")

    plt.show()


def effectifProba(tab):#en n il y a le nombre de valeur a n/100 de proba
    res=[0 for i in range(101)]
    for e in tab:
        res[int(e*100)]+=1
    return res

listLiens = parseFile("Data/dataReactomeSorted")
G=nx.Graph()
G.add_edges_from(listLiens)
ranked_links = indicesAA(G)
effectpro = effectifProba(ranked_links)

plot_predictability_ranking(effectpro)