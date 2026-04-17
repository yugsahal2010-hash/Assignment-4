from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import RRRResponse, ErrorResponse
from services import calculate_rrr

app = FastAPI(
    title="Khel AI Required Run Rate API",
    version="1.0.0",
    description="Calculates the chase equation: runs needed, balls remaining, and RRR."
)

# Standard Middleware for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    """Root route to verify API status."""
    return {
        "status": "Online",
        "api_name": "Required Run Rate API",
        "motto": "Explain the chase equation clearly.",
        "usage": "/api/calculate-rrr/?target=160&current_score=140&balls_remaining=12"
    }

@app.get(
    "/api/calculate-rrr/", 
    response_model=RRRResponse, 
    responses={400: {"model": ErrorResponse}}
)
def get_rrr(target: int, current_score: int, balls_remaining: int):
    """
    Endpoint to calculate chase requirements.
    Fails if target is not provided (not a chase situation).
    """
    return calculate_rrr(target, current_score, balls_remaining)