import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
df = pd.read_csv("facebook.csv")
df.head()

fb_graph = nx.from_pandas_edgelist(df,source="age",target="tenure")
type(fb_graph)

fb_graph.nodes()

fb_graph.edges()

nx.degree(fb_graph)

nx.degree_centrality(fb_graph)
degree_centrality = nx.degree_centrality(fb_graph)
plt.figure(figsize=(10, 6))
plt.bar(degree_centrality.keys(), degree_centrality.values(), color='skyblue')
plt.xlabel('Node')
plt.ylabel('degree_centrality')
plt.title('degree_centrality of Nodes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

G= nx.Graph(fb_graph)
nx.draw(fb_graph,with_labels=True)

nx.eigenvector_centrality(G)
eigen_centrality = nx.eigenvector_centrality(G)
plt.figure(figsize=(10, 6))
plt.bar(eigen_centrality.keys(), eigen_centrality.values(), color='skyblue')
plt.xlabel('Node')
plt.ylabel('eigen_centrality')
plt.title('eigen_centrality of Nodes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

nx.betweenness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
plt.figure(figsize=(10, 6))
plt.bar(betweenness_centrality.keys(), betweenness_centrality.values(), color='skyblue')
plt.xlabel('Node')
plt.ylabel('Betweenness Centrality')
plt.title('Betweenness Centrality of Nodes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

nx.has_bridges(G)

bridges = list(nx.bridges(G))
len(bridges)

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Position nodes using the spring layout
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10)
nx.draw_networkx_edges(G, pos, edgelist=bridges, edge_color='red', width=2)