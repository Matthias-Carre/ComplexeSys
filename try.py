import networkx as nx

def calculate_clustering_coefficients(edges):
    # Créer un graphe à partir des arêtes données
    G = nx.Graph()
    G.add_edges_from(edges)

    # Calculer le coefficient de clustering pour chaque nœud
    clustering_coeffs = nx.clustering(G)

    # Calculer le coefficient de clustering moyen pour le graphe
    average_clustering = nx.average_clustering(G)

    print("Coefficient de clustering pour chaque nœud:", clustering_coeffs)
    print("Coefficient de clustering moyen pour le graphe:", average_clustering)



graph = []
file_path = "./Data/dataReactomeSorted"
with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        (s1,s2) = (int(line.split(" ")[0]),int(line.split(" ")[1][0:-1]))
        graph.append((s1,s2))
        
calculate_clustering_coefficients(graph)

