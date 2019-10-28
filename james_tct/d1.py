import pandas as pd
import matplotlib.pyplot as plt

puins = ['2713129639',
         '1845502510',
         '3592397569',
         '3197518060',
         '2124602574',
         '3051912202',
         '1750813688']

for puin in puins:
    df = pd.read_csv('../_data/20191027/content_20191027_top200.csv')

    data = df[df.puin.isin([puin])]
    data = data.sort_values(axis=0, by='s_input_date', ascending=True)

    print(data)
    plt.plot(data['s_input_date'], data['cnt'])
    plt.xticks(rotation=60)
    plt.ylabel('content count')
    plt.xlabel('date')
    plt.title(puin)
    plt.show()
