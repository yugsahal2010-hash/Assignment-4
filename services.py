from fastapi import HTTPException

def calculate_rrr(target: int, current_score: int, balls_remaining: int) -> dict:
    """
    Business Logic: Calculates the pressure metrics for a chase.
    Rule: Fail if target is 0 or negative (not a chase).
    """
    
    # 1. Graceful Failure Check
    if target <= 0:
        raise HTTPException(
            status_code=400, 
            detail="Required Run Rate is only applicable in a chase (2nd innings). Target must be > 0."
        )

    # 2. Calculate Runs Needed
    # If they've already passed the target, runs_needed is 0
    runs_needed = max(0, target - current_score)

    # 3. Calculate Required Run Rate
    # Formula: (Runs Needed / Overs Remaining) 
    # Since 1 over = 6 balls, formula is: (runs_needed / (balls_remaining / 6))
    if balls_remaining > 0:
        rrr = round((runs_needed / (balls_remaining / 6)), 2)
    else:
        # If no balls are left and runs are still needed, the rate is technically infinite
        # We return 0.0 or a high number; here we use 0.0 if won, or 99.9 if lost/tied
        rrr = 0.0 if runs_needed == 0 else 99.99

    return {
        "target": target,
        "current_score": current_score,
        "runs_needed": runs_needed,
        "balls_remaining": balls_remaining,
        "required_run_rate": rrr
    }