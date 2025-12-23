from google import genai
from app.core.config import settings

def generate_market_report(sector: str, market_data: str) -> str:
    """
    Sends the collected data to Gemini using the new SDK.
    """
    # Initialize the client
    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    
    prompt = f"""
    You are an expert financial analyst. Analyze the following raw market data for the '{sector}' sector in India.
    
    RAW DATA:
    {market_data}
    
    TASK:
    Generate a structured 'Trade Opportunities Report' in Markdown format.
    
    REQUIREMENTS:
    1. Title: Market Analysis for {sector}
    2. Section 1: Key Trends (Bulleted list)
    3. Section 2: Trade Opportunities (Highlight specific areas for investment/growth)
    4. Section 3: Risks & Challenges
    5. Section 4: Conclusion
    
    Make the output professional and ready to be saved as a .md file.
    """
    
    try:
        # We use the specific model you found in your list
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error generating report: {e}"