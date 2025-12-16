from duckduckgo_search import DDGS

def duckduckgo_search(query: str, max_results: int = 5) -> str:
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append(
                f"- {r['title']} ({r['href']})\n  {r['body']}"
            )
    return "\n".join(results) if results else "No results found."
