# main.py
# python-mini-projects @Murilo Pagliuso

import json

try:
    with open('data.json','r') as jsonfile:
        data = json.loads(jsonfile.read())   # Grab the whole json file

    output = ','.join([*data[0]["friends"][0]])  # Grab the keys of friends
    for k in data[0]["friends"]:
        output += f"\n{k["id"]},{k["name"]},{k["email"]},{k["phone"]},{k["address"]}"

    with open("data.csv",'w') as csvfile:   
        csvfile.write(output)   # write data to csv
    
except Exception as e:
    print(f"[!] - Error Loading File") 