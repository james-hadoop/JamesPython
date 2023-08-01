import json

from pyecharts import options as opts
from pyecharts.charts import Graph

json_file = "les-miserables.json"
json_file = "dataworks_1.json"

with open(json_file, "r", encoding="utf-8") as f:
    j = json.load(f)
    nodes = j["nodes"]
    links = j["links"]
    categories = j["categories"]

c = (
    Graph(init_opts=opts.InitOpts(width="1920px", height="1080px"))
    .add(
        "",
        nodes=nodes,
        links=links,
        categories=categories,
        type="graph",
        layout="none",
        is_rotate_label=True,
        linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3),
        label_opts=opts.LabelOpts(position="right"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Graph-Les Miserables"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_left="2%", pos_top="20%"),
    )
    .render("graph_les_miserables.html")
)
