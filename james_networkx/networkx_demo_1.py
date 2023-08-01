import networkx as nx
import matplotlib.pyplot as plt
import graphviz

G = nx.DiGraph(
    [
        ("start_dm_qm_book_analyze_day_new", "dm_qm_book_analyze_day_new"),
        ("end_dwt_qm_statistics_book_duration", "start_dm_qm_book_analyze_day_new"),
        ("a", "e"),
        ("b", "c"),
        ("b", "d"),
        ("d", "e"),
        ("f", "c"),
        ("f", "g"),
        ("h", "f"),
    ]
)

for layer, nodes in enumerate(nx.topological_generations(G)):
    # `multipartite_layout` expects the layer as a node attribute, so add the
    # numeric layer value as a node attribute
    for node in nodes:
        G.nodes[node]["layer"] = layer

# Compute the multipartite_layout using the "layer" node attribute
pos = nx.multipartite_layout(G, subset_key="layer")

fig, ax = plt.subplots()
nx.draw_networkx(G, pos=pos, ax=ax)
ax.set_title("DAG layout in topological order")
fig.tight_layout()
plt.show()
