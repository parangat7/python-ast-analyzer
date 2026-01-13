import ast
import os
import sys
from collections import defaultdict

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = {"classes": [], "functions": [], "imports": [], "calls": []}
        self.scope_stack = []
        self.current_function = None

    def visit_ClassDef(self, node):
        self.scope_stack.append(node.name)
        self.stats["classes"].append({"name": node.name, "line": node.lineno})
        self.generic_visit(node)
        self.scope_stack.pop()

    def visit_FunctionDef(self, node):
        func_name = node.name
        full_scope = ".".join(self.scope_stack + [func_name])
        self.current_function = full_scope
        self.scope_stack.append(func_name)
        self.stats["functions"].append({"name": func_name, "scope": full_scope, "line": node.lineno})
        self.generic_visit(node)
        self.scope_stack.pop()
        self.current_function = None

    def visit_Call(self, node):
        if self.current_function:
            callee = self._get_func_name(node.func)
            if callee:
                self.stats["calls"].append({"caller": self.current_function, "callee": callee})
        self.generic_visit(node)

    def visit_Import(self, node):
        for alias in node.names: self.stats["imports"].append(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        module = node.module if node.module else ""
        for alias in node.names: self.stats["imports"].append(f"{module}.{alias.name}")
        self.generic_visit(node)

    def _get_func_name(self, node):
        if isinstance(node, ast.Name): return node.id
        elif isinstance(node, ast.Attribute): return f"{self._get_func_name(node.value)}.{node.attr}"
        return None

def analyze_directory(path):
    aggregated = {"classes": [], "functions": [], "imports": [], "calls": []}
    print(f"🚀 Scanning directory: {path}")
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        tree = ast.parse(f.read())
                        analyzer = CodeAnalyzer()
                        analyzer.visit(tree)
                        for k in aggregated: aggregated[k].extend(analyzer.stats[k])
                except Exception as e: print(f"⚠️ Error: {e}")
    return aggregated

def generate_outputs(data, output_dir="output"):
    if not os.path.exists(output_dir): os.makedirs(output_dir)

    # 1. Write Summary
    with open(f"{output_dir}/summary.md", "w") as f:
        f.write(f"# Report\n- Classes: {len(data['classes'])}\n- Functions: {len(data['functions'])}")

    # 2. Write Graph (LINE BY LINE to prevent errors)
    counts = defaultdict(int)
    for c in data["calls"]: counts[(c['caller'], c['callee'])] += 1
    
    with open(f"{output_dir}/Final_Graph.md", "w") as f:
        f.write("# Visualization\n\n")
        f.write("```mermaid\n")
        f.write("graph TD\n") # <--- Forced Newline Here
        
        for (caller, callee), count in sorted(counts.items(), key=lambda x: x[1], reverse=True)[:50]:
            # Write each arrow on its own line
            f.write(f'    "{caller}" -->|{count}| "{callee}"\n')
            
        f.write("```\n")

    print(f"✅ Fixed! Open 'output/Final_Graph.md' and press Cmd+Shift+V")

if __name__ == "__main__":
    analyze_directory(".")
    generate_outputs(analyze_directory("."))