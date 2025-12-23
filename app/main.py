from fastapi import FastAPI, Depends, Request
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse
from app.core.security import limiter, verify_token
from app.services.market_data import get_market_data
from app.services.ai_analysis import generate_market_report

app = FastAPI(title="Trade Opportunities API")

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(request: Request, sector: str, token: str = Depends(verify_token)):
    raw_data = get_market_data(sector)
    report_content = generate_market_report(sector, raw_data)
    return {"sector": sector, "report": report_content, "format": "markdown"}