import json

with open('./attractions.json', 'r') as f:
    data_attractions = json.load(f)

print('Number: ', data_attractions["number"])

for k,v in data_attractions["attractions"].items():
    print(k)
    print('value: ', v["value"])
    print('latency: ', len(v["latency"]))
    print('fastpass: ', len(v["fastpass"]))
