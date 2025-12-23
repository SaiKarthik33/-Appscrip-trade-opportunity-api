from duckduckgo_search import DDGS
import logging

logger = logging.getLogger(__name__)

def get_market_data(sector: str) -> str:
    query = f"{sector} industry market trends trade opportunities india 2025"
    results_text = ""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
            if not results:
                return "No recent market data found."
            for res in results:
                results_text += f"Title: {res['title']}\nSnippet: {res['body']}\nSource: {res['href']}\n\n"
    except Exception as e:
        logger.error(f"Error fetching data: {e}")
        return "Error fetching external market data."
    return results_text