# Python AST Analyzer & RAG System

A comprehensive tool for **Static Code Analysis** and **Retrieval-Augmented Generation (RAG)**.

This project analyzes Python source code using the `ast` module to extract structural metadata, generating interactive dependency graphs and providing context-aware prompts for AI assistants. It solves the "context gap" in LLMs by injecting precise function scopes and call hierarchies.

## 🚀 Key Features

### 1. Static Analysis & Visualization
- **Deep AST Parsing**: Scans source code without execution to extract classes, functions, and imports.
- **Dependency Mapping**: Automatically detects caller/callee relationships.
- **Interactive Graphs**: Generates Mermaid.js diagrams (`Final_Graph.md`) for visual architectural review.

### 2. RAG Context Generation (New)
- **Context Injection Pattern**: Replaces naive text chunking with structural context extraction.
- **Vocabulary Matching**: Ensures LLMs understand exact function names and scopes, reducing hallucinations.
- **Chat Interface**: Includes `chat_with_code.py` to allow natural language querying of the codebase.

### 3. Quality Assurance (QA)
- **Verified Accuracy**: The RAG system has been audited using the "Context Quality Experiment" protocol.
- **Results**: Achieved a **5/5 accuracy score** on technical queries compared to a 2/5 baseline.
- **Report**: View the full audit in [QA_REPORT.md](./QA_REPORT.md).

## 🛠️ Tech Stack

- **Core**: Python 3.x, `ast` module
- **Visualization**: Mermaid.js (Markdown)
- **Architecture**: RAG (Retrieval-Augmented Generation) - Context Injection Pattern
- **Roadmap**: Migrating to VS Code Extension (TypeScript/Webpack)

## 📂 Installation & Usage

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/parangat7/python-ast-analyzer.git](https://github.com/parangat7/python-ast-analyzer.git)
   cd python-ast-analyzer
