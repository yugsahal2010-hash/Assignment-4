from pydantic import BaseModel, Field

class RRRResponse(BaseModel):
    target: int = Field(..., description="The score set by the first innings team")
    current_score: int = Field(..., description="The runs scored by the chasing team so far")
    runs_needed: int = Field(..., description="Difference between target and current score")
    balls_remaining: int = Field(..., description="Number of legal deliveries left in the match")
    required_run_rate: float = Field(..., description="Runs needed per 6 balls")

class ErrorResponse(BaseModel):
    detail: str = Field(..., description="Error message for non-chase or invalid scenarios")