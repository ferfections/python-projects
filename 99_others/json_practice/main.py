import json

with open("others/data.json", "r") as f:
    data = json.load(f)

print(data.items())