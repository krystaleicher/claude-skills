from dataclasses import dataclass
from typing import Optional


MAX_TEXT_LENGTH = 500


@dataclass
class CheckIn:
    mood: int
    top_win: str
    biggest_challenge: str
    commitment: str


def validate_checkin(data: dict) -> tuple[bool, Optional[str]]:
    """Validate a weekly check-in submission. Returns (is_valid, error_message)."""
    mood = data.get("mood")
    if mood is None:
        return False, "Mood is required"
    if not isinstance(mood, int) or not (1 <= mood <= 5):
        return False, "Mood must be an integer between 1 and 5"

    for field in ("top_win", "biggest_challenge", "commitment"):
        value = data.get(field, "").strip()
        if not value:
            return False, f"{field.replace('_', ' ').title()} is required"
        if len(value) > MAX_TEXT_LENGTH:
            return False, f"{field.replace('_', ' ').title()} must be under {MAX_TEXT_LENGTH} characters"

    return True, None


def build_checkin(data: dict) -> CheckIn:
    """Build a CheckIn object from validated data. Call validate_checkin first."""
    return CheckIn(
        mood=data["mood"],
        top_win=data["top_win"].strip(),
        biggest_challenge=data["biggest_challenge"].strip(),
        commitment=data["commitment"].strip(),
    )
