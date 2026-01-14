# Python AST Analyzer & RAG Context Generator

A powerful static analysis tool and **RAG (Retrieval-Augmented Generation) System** built with Python's `ast` module. 

This tool goes beyond simple text search by extracting **Structural Context** (classes, functions, and call dependencies) to power accurate LLM responses, solving the "vocabulary mismatch" problem found in naive RAG approaches.

## 🚀 Key Features

### 1. Static Code Analysis
- **AST-Based Parsing**: Deep-scans source code to understand structure without execution.
- **Dependency Mapping**: Automatically identifies relationships between functions and classes.
- **Visual Call Graphs**: Generates interactive Mermaid.js diagrams to visualize execution flow.

### 2. RAG Context Generation (New)
- **Structural Retrieval**: Uses AST metadata instead of vector similarity to find relevant code context.
- **Context Injection**: Implements **Pattern 2 (Context Injection)** to format code structure into optimized prompts for LLMs.
- **Scope Awareness**: Preserves function scope and class hierarchy in the generated context.

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Core Library**: `ast` (Abstract Syntax Tree)
- **Visualization**: Mermaid.js (Markdown based)
- **RAG Pattern**: Structural Context Injection

## 📂 Installation & Usage

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/parangat7/python-ast-analyzer.git](https://github.com/parangat7/python-ast-analyzer.git)
   cd python-ast-analyzer
