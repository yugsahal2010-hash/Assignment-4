from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import RRRInput, RRRResponse, ErrorResponse
from services import calculate_rrr

app = FastAPI(
    title="Khel AI Required Run Rate API",
    version="1.0.0",
    description="Calculates the chase equation: runs needed, balls remaining, and RRR."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "status": "Online",
        "api_name": "Required Run Rate API",
        "motto": "Explain the chase equation clearly.",
    }


@app.post(
    "/api/calculate-rrr/",
    response_model=RRRResponse,
    responses={400: {"model": ErrorResponse}}
)
def get_rrr(input_data: RRRInput):
    return calculate_rrr(input_data.model_dump())
