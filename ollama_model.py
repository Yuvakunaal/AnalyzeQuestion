import ollama

def build_ollama_prompt(problem_text: str, rag_context: str = "") -> str:
    """
    Constructs a detailed prompt for Ollama based on problem text, 
    RAG context, and expected JSON output.
    """

    prompt = f"""
You are an expert AI coding assistant for students and competitive programmers.

### Task:
Analyze the following coding problem and provide a complete breakdown including:
1. **All applicable algorithmic and data-structure patterns** (from classic patterns to advanced techniques).
2. **Difficulty level** (Easy / Medium / Hard).
3. **Step-by-step solution approach** in clear, actionable steps.
4. Output in **valid JSON format only** like this:

{{
  "patterns": ["Pattern 1", "Pattern 2", "Pattern 3"],
  "difficulty": "Medium",
  "approach": [
    "Step 1: Analyze input and constraints",
    "Step 2: Identify overlapping subproblems",
    "Step 3: Determine optimal, super optimal algorithm",
    "Step 4: Outline step-by-step solution"
  ]
}}

### Supported Algorithmic Patterns:
- Sliding Window, Prefix Sum, Two Pointers, Hashing, Kadane’s Algorithm, Monotonic Stack,
Monotonic Queue, Sorting, Subarray Techniques, Subsequence Techniques
- Classic 1D DP, 2D DP, DP on Trees, Bitmask DP, Memoization, Tabulation, Longest Common
- Subsequence, Longest Increasing Subsequence, Knapsack, Matrix DP, DP + Sliding Window
- BFS, DFS, Topological Sorting, Dijkstra, Bellman-Ford, Floyd-Warshall, Kruskal, Prim, Union-Find,
Graph Coloring, Tarjan SCC, Network Flow
- Interval Scheduling, Minimum Coins, Fractional Knapsack, Huffman Coding, Greedy + Sorting
- Binary Search, Ternary Search, Sliding Window Search, Two Pointers Search, Meet-in-the-middle
- Recursion, Backtracking, Subsets, Permutations, Combinations, N-Queens, Sudoku Solver, Word
Search, Maze Solving, Recursive DP
- Prime Factorization, GCD, LCM, Modular Arithmetic, Combinatorics, Sieve of Eratosthenes,
Modular Exponentiation, Fibonacci, Tribonacci, Probability, Counting
- Stack, Queue, Heap, Segment Tree, Fenwick Tree, Trie, Balanced BST, Linked List, HashMap,
HashSet, Union-Find
- Sliding Window + Hashing, Mo’s Algorithm, Heavy-Light Decomposition, Sparse Table, Rolling
Hash, FFT, Meet-in-the-middle
-Bit Manipulation, XOR Tricks, Game Theory, KMP, Z-Algorithm, Convex Hull, Line Intersections,
Interval DP, Matrix Chain Multiplication, Randomized Methods


### RAG Context:
{rag_context if rag_context else "No previous problems available."}

### Problem:
{problem_text}

### Instructions:
- Only output valid JSON.
- Include all applicable patterns.
- Provide step-by-step approach for a student to implement.
- Be precise, concise, and structured.
"""

    return prompt


def ollama_call(problem_text: str, context: str = "") -> str:

    # Construct the prompt with RAG context if available
    prompt = build_ollama_prompt(problem_text, context)
    
    try:
        response = ollama.chat(
            model='mistral:instruct',
            messages=[{'role': 'user', 'content': prompt}]
        )

        # Ollama returns a dict; extract content
        return response['message']['content']

    except Exception as e:
        return f"Error: {str(e)}"
