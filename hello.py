import json 

with open("names.json","r")as f:
    data = json.load(f)

new_string = json.dumps(data, indent=4)

with open("New.json","a") as f:
    f.write(new_string)