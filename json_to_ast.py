import json

with open("./ast.json", "r") as f:
    data = json.load(f)

tree = None

START_BRACKET = "("
END_BRACKET = ")"

APPEND_TYPES = (int,type(None))

lst = ["Module"+START_BRACKET,"body=["]

def create_node(node):
    for key in node.keys():
        if(key == "_type"):
            lst.append(node[key]+START_BRACKET)
        else:
            if(isinstance(node[key],APPEND_TYPES)):
                lst.append(f'{key}={node[key]}')
            elif(isinstance(node[key],str)):
                lst.append(f"{key}='{node[key]}'")
            elif(isinstance(node[key],list)):
                lst.append(f'{key}=[')
                [create_node(x) for x in node[key]]
                lst.append(']')
            else:
                print(f"Unidentified key ==> {key} and node ==> {node[key]}")
                
    lst.append(END_BRACKET)

# f = open("demofile2.py", "a")
# f.write("from ast import *\n")


for node in data["body"]:
    create_node(node)
    lst.append("]")
    lst.append(END_BRACKET)
    break


ast_str = "from ast import *\n"

with open('demofile2.py','w') as tfile:
    tfile.write("from ast import *\n")
    ast_str += "".join([f'{line}\n' if line[-1] in (START_BRACKET,"[") else f'{line},\n' for line in lst])
    [tfile.write(f'{line}\n' if line[-1] in (START_BRACKET,"[") else f'{line},\n') for line in lst]
        # f.write(f'{data[item]}()')

print(ast_str)

# f.close()
