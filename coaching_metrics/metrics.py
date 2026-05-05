import datetime
from typing import List, Optional


def session_streak(dates: List[datetime.date]) -> int:
    """Return the current consecutive-day session streak."""
    if not dates:
        return 0
    sorted_dates = sorted(set(dates), reverse=True)
    today = datetime.date.today()
    streak = 0
    expected = today
    for d in sorted_dates:
        if d == expected:
            streak += 1
            expected -= datetime.timedelta(days=1)
        else:
            break
    return streak


def goal_completion_rate(goals: List[bool]) -> float:
    """Return the fraction of completed goals as a float 0.0–1.0."""
    if not goals:
        return 0.0
    return sum(goals) / len(goals)


def days_since_checkin(last_date: Optional[datetime.date], today: Optional[datetime.date] = None) -> Optional[int]:
    """Return days elapsed since last_date, or None if last_date is None."""
    if last_date is None:
        return None
    if today is None:
        today = datetime.date.today()
    if last_date > today:
        raise ValueError(f"last_date {last_date} is in the future")
    return (today - last_date).days
