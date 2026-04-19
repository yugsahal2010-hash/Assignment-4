from fastapi import HTTPException


def calculate_rrr(data: dict) -> dict:
    target = data["target"]
    current_score = data["current_score"]
    balls_remaining = data["balls_remaining"]

    if target <= 0:
        raise HTTPException(
            status_code=400,
            detail="Required Run Rate is only applicable in a chase (2nd innings). Target must be > 0."
        )

    runs_needed = max(0, target - current_score)

    if balls_remaining > 0:
        rrr = round((runs_needed / (balls_remaining / 6)), 2)
    else:
        rrr = 0.0 if runs_needed == 0 else 99.99

    return {
        "target": target,
        "current_score": current_score,
        "runs_needed": runs_needed,
        "balls_remaining": balls_remaining,
        "required_run_rate": rrr,
    }
