import json

with open('server_path.json') as json_file:
    data = json.load(json_file)
    print data
for k,v in data.items():
    for i in v:
        print k,i
