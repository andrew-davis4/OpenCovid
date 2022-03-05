import requests
import json
from os import system


# url = 'https://api.opencovid.ca/'
# data = requests.get(url).text

# json_data = json.loads(data)


# with open("opencovid.json", "w") as w_file:
#     json.dump(json_data, w_file)

with open("opencovid.json", "r") as r_file:
    opencovid = json.load(r_file)


# url2 = 'https://api.opencovid.ca/other?stat=prov'
# data2 = requests.get(url2).text

# json_data2 = json.loads(data2)


# with open("opencovid2.json", "w") as w_file:
#     json.dump(json_data2, w_file)

with open("opencovid2.json", "r") as r_file:
    opencovid2 = json.load(r_file)


system("cls")

# num = input("Statistics\n\nWant to see:\n(1)Covid Cases summary in Canada\n{: >17}\n(2)Populations of each province in Canada\n".format("or"))

# system("cls")

## not working
# print("Covid cases summary in Canada:")
# for key in opencovid['summary']:
#     for subkey in key:
#       print(key, ":", key[subkey])


print("Populations of each province in Canada:\n")


for province in opencovid2['prov']:
    if province['pop'] != 'NULL':
        print("{} : {:,.0f}".format(province['province_short'], province['pop']))