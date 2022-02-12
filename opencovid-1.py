from re import X
import requests, json
import pandas as pd
import matplotlib.pyplot as plt
from os import system

def population():
    system("cls")
    url = 'https://api.opencovid.ca/other?stat=prov'
    data = requests.get(url).text
    json_data = json.loads(data)
    # print(json_data)

    json_data['prov'].pop() #Data Cleaning - to remove "Repatriated" from data['prov']

    df = pd.read_json(json.dumps(json_data['prov'])) # df : Data Frame
    print(df)

    df.plot.bar(
        x='province_short',
        y='pop',
    )
    plt.show()

population()

# in one line:
# print(json.loads(requests.get('https://api.opencovid.ca/other?stat=prov').text))

