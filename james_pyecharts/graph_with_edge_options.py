import os

from pyecharts import options as opts
from pyecharts.charts import Graph

os.remove("graph_with_edge_options.html")

nodes_data = [
    opts.GraphNode(name="结点1", symbol_size=30, is_fixed=True, x=100),
    opts.GraphNode(name="结点2", symbol_size=30, is_fixed=True, x=200),
    opts.GraphNode(name="结点3", symbol_size=30),
    opts.GraphNode(name="结点4", symbol_size=30),
    opts.GraphNode(name="结点5", symbol_size=30),
    opts.GraphNode(name="结点6", symbol_size=30),
]
# links_data = [
#     opts.GraphLink(source="结点1", target="结点2", value=30),
#     opts.GraphLink(source="结点2", target="结点3", value=300),
#     opts.GraphLink(source="结点3", target="结点4", value=3),
#     opts.GraphLink(source="结点4", target="结点5", value=3),
#     opts.GraphLink(source="结点5", target="结点6", value=3),
# ]
links_data = [
    opts.GraphLink(source="结点1", target="结点2", value=2),
    opts.GraphLink(source="结点2", target="结点3", value=3),
    opts.GraphLink(source="结点3", target="结点4", value=4),
    opts.GraphLink(source="结点4", target="结点5", value=5),
    opts.GraphLink(source="结点5", target="结点6", value=6),
]
c = (
    Graph(init_opts=opts.InitOpts(width="1800px", height="1600px"))
        .add(
        "",
        nodes_data,
        links_data,
        repulsion=8000,
        edge_label=opts.LabelOpts(
            is_show=True, position="middle", formatter="{b} -> {c}"
        )
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(title="Graph-GraphNode-GraphLink-WithEdgeLabel")
    )
        .render("graph_with_edge_options.html")
)
