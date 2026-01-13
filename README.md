# Python Code Structure Analyzer & Visualizer

A powerful static analysis tool built with Python's `ast` (Abstract Syntax Tree) module. This tool scans Python source code to extract structural data, dependencies, and call hierarchies, then generates visual and data-driven reports.

## 🚀 Features

- **AST-Based Parsing**: Deep-scans source code without execution, making it safe and fast.
- **Entity Extraction**: Automatically identifies Class definitions, Function definitions, and Import statements.
- **Call Graph Generation**: Maps relationships between functions to visualize how code flows.
- **Multi-Format Output**: 
  - `entities.json`: Structured data for programmatic use.
  - `summary.md`: A quick overview of the codebase complexity.
  - `Final_Graph.md`: An interactive visualization using Mermaid.js.

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Core Library**: `ast` (Abstract Syntax Tree)
- **Visualization**: Mermaid.js (Markdown based)

## 📂 Installation & Usage

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/parangat7/python-ast-analyzer.git](https://github.com/parangat7/python-ast-analyzer.git)
   cd python-ast-analyzer
