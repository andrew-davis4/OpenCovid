from dataclasses import dataclass
from re import X
import requests, json
import pandas as pd
import matplotlib.pyplot as plt
from os import system


def thousands(x, pos):
    return "{:,.0f}".format(x/1000) 
def millions(x, pos):
    return "{:,.0f}".format(x/1000000)



def province():
    #system("cls")
    url = 'https://api.opencovid.ca/timeseries'
    response = requests.get(url)
    data = json.loads(response.text)
    # print(json_data)

    df = pd.read_json(json.dumps(data['active']))


    ##df['date_active'] = pd.to_datetime(df['date_active'], format='%d-%m-%Y')

    ax = df.query('province == "Alberta"').plot(
        x='date_active',
        y='active_cases',
        rot=20,
        legend=False
    )
    ax.set_title('Active Covid Cases Over Time : Alberta', fontsize=20)
    ax.set_xlabel('Date', fontsize=16)
    ax.set_ylabel('Active Cases (Thousands)', fontsize=16)
    ax.xaxis.set_tick_params(labelsize=10)
    ax.yaxis.set_major_formatter(thousands)
    plt.show() 

province()


def population():
    system("cls")
    url = 'https://api.opencovid.ca/other?stat=prov'
    data = requests.get(url).text
    json_data = json.loads(data)
    # print(json_data)

    json_data['prov'].pop() #Data Cleaning - to remove "Repatriated" from data['prov']

    df = pd.read_json(json.dumps(json_data['prov'])) # df : Data Frame
    print(df)

    ax = df.plot.bar(
        x='province_short',
        y='pop',
        rot=0,
        legend=False
    )
    ax.set_title('Population by province', fontsize=20)
    ax.set_xlabel('Province', fontsize=14)
    ax.set_ylabel('Population (millions)', fontsize=14)
    #ax.yaxis.set_major_formatter()
    ax.yaxis.set_major_formatter(millions)
    plt.show()



# in one line:
# print(json.loads(requests.get('https://api.opencovid.ca/other?stat=prov').text))

