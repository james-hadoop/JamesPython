import pandas as pd
from elasticsearch import Elasticsearch
import json

es = Elasticsearch()
# 假设你有一堆数据，通过df加载，并且进行可必要的处理
df = pd.read_csv("/Users/lex/Code/bitmex_arbitrage/data.csv")

#
# 数据处理
# 然后准备输入到elasticsearch当中

df_as_json = df.to_json(orient='records', lines=True)
bulk_data = []

for json_document in df_as_json.split('\n'):
    bulk_data.append({"index": {
        '_index': "btc_eth_data",
        '_type': "doc",
    }})
    bulk_data.append(json.loads(json_document))
    # 一次bulk request包含1000条数据
    if len(bulk_data) > 1000:
        es.bulk(bulk_data)
        bulk_data = []
es.bulk(bulk_data)
