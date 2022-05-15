import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../_data/3.csv')

data = df[df.puin.isin(['2713129639'])]
data = data.sort_values(axis=0, by='s_input_date', ascending=True)

print(data)
plt.plot(data['s_input_date'],  data['cnt'])
plt.xticks(rotation=60)
plt.ylabel('content count')
plt.xlabel('date')
plt.title('title')
plt.show()
