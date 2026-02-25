import networkx as nx
import matplotlib.pyplot as plt

n = int(input("Enter number of vertices (>3): "))

if n <= 3:
    raise ValueError("Number of vertices must be greater than 3.")

G = nx.complete_graph(n)

nx.draw(G, with_labels=True)
plt.show()
