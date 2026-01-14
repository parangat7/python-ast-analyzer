import os
import sys
from analyze import analyze_directory  # We reuse your existing work

def chat_interface():
    print("🚀 RAG System Initialized...")
    print("📡 Retrieving Structural Context from AST...")
    
    # 1. RETRIEVAL (Using your AST tool as the retriever)
    # This replaces "Naive RAG" with "AST-Based Chunking"
    code_data = analyze_directory(".") 

    # 2. CONTEXT ASSEMBLY
    # We format the extracted entities into a prompt
    context_str = "CODEBASE STRUCTURE:\n"
    
    # Add Functions context
    for func in code_data['functions']:
        context_str += f"- Function: {func['name']} (Line {func['line']})\n"
        context_str += f"  - Scope: {func['scope']}\n"
        
    # Add Dependency context (Calls)
    context_str += "\nDEPENDENCIES:\n"
    for call in code_data['calls']:
        context_str += f"- {call['caller']} calls {call['callee']}\n"

    print(f"✅ Context Loaded! ({len(code_data['functions'])} functions, {len(code_data['calls'])} calls)")
    print("-" * 50)

    # 3. INTERACTION LOOP
    while True:
        user_question = input("\n🤖 Ask a question (or 'exit'): ")
        if user_question.lower() in ['exit', 'quit']:
            break

        # 4. PROMPT ENGINEERING
        # We inject the context directly into the prompt template
        prompt = f"""
You are an expert AI code assistant. Use the following Structural Context to answer the user's question.

## CONTEXT (AST Analysis)
{context_str}

## QUESTION
{user_question}

## INSTRUCTIONS
- Use the provided function names and call graphs to explain the answer.
- If the logic isn't visible in the context, admit what you don't know.
"""
        print("\n" + "="*20 + " GENERATED PROMPT " + "="*20)
        print("Copy the text below into ChatGPT, Claude, or Gemini:\n")
        print(prompt)
        print("="*58)

if __name__ == "__main__":
    chat_interface()