import os
import ast

def get_ast(tree):
    print(ast.dump(tree, indent=2))


class Finder(ast.NodeVisitor):
    """
    A Checker is a Visitor that defines a lint rule, and stores all the
    nodes that violate that lint rule.
    """

    def __init__(self, name):
        self.name = name
        self.findings = set()


class Serializer:
    """Holds all finders, and runs them against a source file."""

    def __init__(self):
        self.finders = set()

    @staticmethod
    def print_findings(finder):
        print(f"\nFinder -> {finder.name}")
        print("="*(len(finder.name)+10))
        for finding in finder.findings:
            print(finding)
            print("\n")
        print("\n\n")

    def run(self, source_path):
        """Runs all finders on a source file."""
        file_name = os.path.basename(source_path)

        with open(source_path) as source_file:
            source_code = source_file.read()

        tree = ast.parse(source_code)

        for finder in self.finders:
            finder.visit(tree)
            self.print_findings(finder)


class ImportFinder(Finder):
    """Find all import statements."""


    def __init__(self, name):
        super().__init__(name)

    def generic_visit(self,node):
        if(isinstance(node,ast.ImportFrom) or isinstance(node,ast.Import)):
            self.findings.add(ast.dump(node=node))
        super().generic_visit(node)

class VariableFinder(Finder):
    """Find all variables."""


    def __init__(self, name):
        super().__init__(name)

    def generic_visit(self,node):

        if(isinstance(node,ast.Assign) and isinstance(node.value, ast.Constant)):
            self.findings.add(ast.dump(node=node))
        super().generic_visit(node)

class FunctionFinder(Finder):
    """Find all variables."""


    def __init__(self, name):
        super().__init__(name)

    def generic_visit(self,node):

        if(isinstance(node,ast.FunctionDef)):
            self.findings.add(ast.dump(node=node))
        super().generic_visit(node)



source_path = "./dags/test.py"

serializer = Serializer()
serializer.finders.add(ImportFinder(name="import_finder"))
serializer.finders.add(VariableFinder(name="variable_finder"))
serializer.finders.add(FunctionFinder(name="function_finder"))
serializer.run(source_path)



#To convert ast to source code

# with open(source_path) as source_file:
#     source_code = source_file.read()

# tree = ast.parse(source_code)
# print(ast.unparse(tree))