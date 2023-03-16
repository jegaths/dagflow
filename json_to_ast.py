import json

from ast import *

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
            elif(isinstance(node[key],dict)):
                lst.append(f'value=')
                # create_node(node)
                #TODO cannot call create_node again, maximum recursion depth exceeded
            else:
                print(f"Unidentified instance ==> {type(node[key])} key ==> {key} and node ==> {node[key]}")
                
    lst.append(END_BRACKET)

# f = open("demofile2.py", "a")
# f.write("from ast import *\n")


for node in data["body"]:
    create_node(node)
    lst.append("]")
    lst.append('type_ignores=[]')
    lst.append(END_BRACKET)
    # break

# print(lst)

# ast_str = "from ast import *\n"
# ast_str = "".join([f'{line}\n' if line[-1] in (START_BRACKET,"[") else f'{line},\n' for line in lst])


# with open('demofile2.py','w') as tfile:
#     # tfile.write("from ast import *\n")
#     [tfile.write(f'{line}\n' if line[-1] in (START_BRACKET,"[") else f'{line},\n') for line in lst]

#Convert ast to source code
# print(unparse(eval(ast_str)[0]))
