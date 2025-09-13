from ollama_model import ollama_call
from services.rag import retrieve_context
from database import save_problem
import json

def analyze_problem(problem_text: str):
    """
    Analyze a coding problem using Ollama + RAG.
    Returns a dict with patterns, difficulty, and approach.
    """

    # Get RAG context
    context = retrieve_context(problem_text)

    # Call Ollama with context
    ai_response = ollama_call(problem_text, context)

    # Parse AI response (assume JSON output from Ollama)
    try:
        result = json.loads(ai_response)
        patterns = result.get("patterns", [])
        difficulty = result.get("difficulty", "Unknown")
        approach = result.get("approach", [])
    except:
        # Fallback if AI does not return JSON
        patterns, difficulty, approach = [], "Unknown", [ai_response]

    # Save to DB for future RAG
    save_problem(
        problem_text=problem_text,
        patterns=patterns,
        difficulty=difficulty,
        approach=approach
    )
    
    # print({
    #     "patterns": patterns,
    #     "difficulty": difficulty,
    #     "approach": approach
    # })

    return {
        "patterns": patterns,
        "difficulty": difficulty,
        "approach": approach
    }
