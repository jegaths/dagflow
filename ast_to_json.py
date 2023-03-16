from _ast import AST
from ast import parse,dump
import codecs
import json

class ASTToJson:

    __BUILTIN_PURE = (int, float, bool)
    __BUILTIN_BYTES = (bytearray, bytes)
    __BUILTIN_STR = (str)

    def __init__(self,file_path: str) -> None:
        with open(file_path, "r") as f:
            tree = parse(f.read())
        # with open("sample_ast.py", 'w', encoding='utf-8') as f:
        #     f.write(dump(tree, include_attributes=True,indent=4))
        self.__ast_dict = self.__to_json(tree)

    def __to_json(self,node):
        node_details = dict()
        node_details['_type'] = node.__class__.__name__
        for attr in dir(node):
            if attr.startswith("_"):
                continue
            node_details[attr] = self.__get_value(getattr(node, attr))
        return node_details

    def __get_value(self,val):
        if val is None:
            return val
        if isinstance(val, self.__BUILTIN_PURE):
            return val
        if isinstance(val, self.__BUILTIN_BYTES):
            return self.__decode_bytes(val)
        if isinstance(val, self.__BUILTIN_STR):
            return self.__decode_str(val)
        if isinstance(val, complex):
            return str(val)
        if isinstance(val, list):
            return [self.__get_value(x) for x in val]
        if isinstance(val, AST):
            return self.__to_json(val)
        if isinstance(val, type(Ellipsis)):
            return '...'
        else:
            raise Exception(f"Unknown case for {val} of type {type(val)}")

    def __decode_str(self,value):
        return value

    def __decode_bytes(self,value):
        try:
            return value.decode('utf-8')
        except:
            return codecs.getencoder('hex_codec')(value)[0].decode('utf-8')  

    def json(self):
        return json.dumps(self.__ast_dict,indent=4)

    def save(self,file_path: str):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.__ast_dict, f, ensure_ascii=False, indent=4)