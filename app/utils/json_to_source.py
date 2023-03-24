import json
from ast import *


class JsonToSource:

    """
    JsonToAST class is to convert to a json AST(Abstract Syntax Tree) to python source code.

    ...

    Attributes:
    ----------
    file_path: str
        Path of the JSON file to convert to python source code (default None)
    json_string: str
        JSON data in string format to convert to python source code (default None)

    Either file_path or json_string should be supplied. If both are provided json_string takes precedance.
    """
    
    __START_BRACKET = "("
    __END_BRACKET = ")"

    __APPEND_TYPES = (int,type(None))

    def __init__(self,json_string: str = None, file_path: str = None) -> None:
        if(file_path == None and json_string == None):
            print("Filepath or json string should be given!")
            return
        if(json_string == None):
            with open(file_path, "r") as f:
                json_data= json.load(f)
        else:
            json_data = json.loads(json_string)
        self.ast_lst = ["Module"+self.__START_BRACKET,"body=["]
        self.__create_ast(json_data)


    def __create_ast(self,data):
        for node in data["body"]:
            self.__create_node(node)
        self.ast_lst.append("]")
        self.ast_lst.append('type_ignores=[]')
        self.ast_lst.append(self.__END_BRACKET)


    def __create_node(self,node):
        for key in node.keys():
            if(key == "_type"):
                self.ast_lst.append(node[key]+self.__START_BRACKET)
            else:
                if(isinstance(node[key],self.__APPEND_TYPES)):
                    self.ast_lst.append(f'{key}={node[key]}')
                elif(isinstance(node[key],str)):
                    if("\n" in node[key]):
                        self.ast_lst.append(f"{key}='''{node[key]}'''")
                    else:
                        self.ast_lst.append(f"{key}='{node[key]}'")
                elif(isinstance(node[key],list)):
                    self.ast_lst.append(f'{key}=[')
                    [self.__create_node(x) for x in node[key]]
                    self.ast_lst.append(']')
                elif(isinstance(node[key],dict)):
                    self.ast_lst.append(f'{key}=')
                    self.__create_node(node[key])
                else:
                    print(f"Unidentified instance ==> {type(node[key])} key ==> {key} and node ==> {node[key]}")
                    
        self.ast_lst.append(self.__END_BRACKET)

    def get(self):
        """
        Return source code as string
        """
        
        ast_str = "".join([f'{line}' if line[-1] in (self.__START_BRACKET,"[",'=') else f'{line},' for line in self.ast_lst])
        return unparse(eval(ast_str)[0])

    def save(self,file_path) -> None:
        """
        Save the source code to the specified path.
        """

        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(self.get())


