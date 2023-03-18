import json


from ast import *
from ast_to_json import ASTToJson

# tree = None

START_BRACKET = "("
END_BRACKET = ")"

APPEND_TYPES = (int,type(None))


def create_node(node,lst):
    for key in node.keys():
        if(key == "_type"):
            lst.append(node[key]+START_BRACKET)
        else:
            if(isinstance(node[key],APPEND_TYPES)):
                lst.append(f'{key}={node[key]}')
            elif(isinstance(node[key],str)):
                if("\n" in node[key]):
                    lst.append(f"{key}='''{node[key]}'''")
                else:
                    lst.append(f"{key}='{node[key]}'")
                # lst.append(f"{key}='{node[key]}'")
            elif(isinstance(node[key],list)):
                lst.append(f'{key}=[')
                [create_node(x,lst) for x in node[key]]
                lst.append(']')
            elif(isinstance(node[key],dict)):
                lst.append(f'{key}=')
                create_node(node[key],lst)
            else:
                print(f"Unidentified instance ==> {type(node[key])} key ==> {key} and node ==> {node[key]}")
                
    lst.append(END_BRACKET)


# with open("./ast.json", "r") as f:
#     data = json.load(f)


# data = ASTToJson(file_path="./dags/test.py").get()


# ast_lst = ["Module"+START_BRACKET,"body=["]
# for node in data["body"]:
#     create_node(node,ast_lst)
# ast_lst.append("]")
# ast_lst.append('type_ignores=[]')
# ast_lst.append(END_BRACKET)


# ast_str = "".join([f'{line}\n' if line[-1] in (START_BRACKET,"[", "=") else f'{line},\n' for line in ast_lst])

# print(ast_str)
# Convert ast to source code
# print(unparse(eval(ast_str)[0]))

# print(ast_str)
# with open('demofile2.py','w') as tfile:
#     # tfile.write("from ast import *\n")
#     [tfile.write(f'{line}\n' if line[-1] in (START_BRACKET,"[") else f'{line},\n') for line in lst]


