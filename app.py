from ast_to_json import ASTToJson

ast = ASTToJson("./dags/test.py")
ast.save("ast.json")