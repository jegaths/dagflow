import json
from ast import *

with open("./ast.json", "r") as f:
    data = json.load(f)

tree = None

for item in data:
    if(item == "_type"):
        print(item)