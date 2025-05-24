# websearch.py
# -- Questions handling powered by DuckDuckGo

from duckduckgo_search import ddg
from database import get_cached_answer, save_cached_answer

def search_web(query, lang="en", max_results=3):
    cached = get_cached_answer(query)
    if cached:
        return cached["answer"]

    try:
        results = ddg(query, max_results=max_results, region=lang)
        if not results:
            return "No relevant results found."

        answer = "\n\n".join(
            f"{res['title']}\n{res['body']}\n{res['href']}" for res in results
        )
        save_cached_answer(query, answer)
        return answer
    except Exception as e:
        return f"Search failed: {str(e)}"
