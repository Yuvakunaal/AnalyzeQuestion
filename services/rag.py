# services/rag.py
from database import fetch_similar_problems

def retrieve_context(problem_text: str, limit: int = 3) -> str:
    """
    Fetch similar past problems for RAG.
    Returns a string to prepend to AI prompt.
    """
    similar = fetch_similar_problems(problem_text, limit)
    context = ""
    for idx, (p_text, patterns, difficulty, approach) in enumerate(similar, start=1):
        context += f"Previous Problem {idx}:\n{p_text}\nPatterns: {patterns}\nDifficulty: {difficulty}\nApproach: {approach}\n\n"
    return context
