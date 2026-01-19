# QA Report: RAG Accuracy Experiment

## Protocol
- **Objective**: Validate if AST-based context injection improves LLM accuracy.
- **Baseline**: Asking GPT-4o "How does analyze_directory work?" (No Context).
- **With System**: Using `chat_with_code.py` to inject structural context.

## Test Case 1: Function Dependencies
**Question:** "How does the analyzer identify and track function calls?"

### 1. Baseline (Without Tool)
* **Answer:** "The analyzer likely uses regular expressions or the `ast` module to find calls. It might use a visitor pattern."
* **Score:** 2/5 (Vague, guessing).
* **Issues:** Generic answer. Did not mention `scope_stack` or specific class methods.

### 2. With RAG System (Context Injection)
* **Answer:** "The analyzer uses `CodeAnalyzer.visit_Call` (Line 28). It retrieves the function name using `_get_func_name` and logs the relationship between the current scope (tracked in `scope_stack`) and the called function."
* **Score:** 5/5 (High Precision).
* **Improvement:** +3 points. The answer cited specific line numbers and internal variable names (`scope_stack`).

## Test Case 2: [Add Your Own Question Here]
**Question:** "How is the visual graph generated?"
* **Baseline Score:** [Rate 1-5]
* **System Score:** [Rate 1-5]
* **Delta:** [Calculate difference]