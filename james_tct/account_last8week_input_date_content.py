import pandas as pd
import matplotlib.pyplot as plt

# puin=str(1750813688)

df = pd.read_csv('../_data/20191027/content_20191027_top200.csv')

data = df
# data = df[df.puin.isin([puin])]
data = data.sort_values(axis=0, by='s_input_date', ascending=True)

print(data)
plt.plot(data['s_input_date'], data['cnt'])
plt.xticks(rotation=60)
plt.ylabel('content count')
plt.xlabel('date')
# plt.title(puin)
plt.show()
