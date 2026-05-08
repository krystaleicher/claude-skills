import pytest
from checkin.validator import validate_checkin, build_checkin, CheckIn, MAX_TEXT_LENGTH


VALID_DATA = {
    "mood": 3,
    "top_win": "Finished the report",
    "biggest_challenge": "Time management",
    "commitment": "I will block two hours each morning",
}


# --- validate_checkin ---

class TestValidateCheckin:

    # Happy path
    def test_valid_submission_returns_true(self):
        ok, err = validate_checkin(VALID_DATA)
        assert ok is True
        assert err is None

    def test_mood_min_boundary_valid(self):
        ok, _ = validate_checkin({**VALID_DATA, "mood": 1})
        assert ok is True

    def test_mood_max_boundary_valid(self):
        ok, _ = validate_checkin({**VALID_DATA, "mood": 5})
        assert ok is True

    # Mood errors
    def test_missing_mood_returns_error(self):
        data = {k: v for k, v in VALID_DATA.items() if k != "mood"}
        ok, err = validate_checkin(data)
        assert ok is False
        assert "Mood is required" in err

    def test_mood_zero_is_invalid(self):
        ok, err = validate_checkin({**VALID_DATA, "mood": 0})
        assert ok is False
        assert "1 and 5" in err

    def test_mood_six_is_invalid(self):
        ok, err = validate_checkin({**VALID_DATA, "mood": 6})
        assert ok is False

    def test_mood_as_string_is_invalid(self):
        ok, err = validate_checkin({**VALID_DATA, "mood": "3"})
        assert ok is False

    def test_mood_as_float_is_invalid(self):
        ok, err = validate_checkin({**VALID_DATA, "mood": 3.0})
        assert ok is False

    def test_mood_none_explicit_returns_error(self):
        ok, err = validate_checkin({**VALID_DATA, "mood": None})
        assert ok is False
        assert "Mood is required" in err

    # Required text fields
    def test_empty_top_win_returns_error(self):
        ok, err = validate_checkin({**VALID_DATA, "top_win": ""})
        assert ok is False
        assert "Top Win" in err

    def test_whitespace_only_top_win_returns_error(self):
        ok, err = validate_checkin({**VALID_DATA, "top_win": "   "})
        assert ok is False

    def test_empty_biggest_challenge_returns_error(self):
        ok, err = validate_checkin({**VALID_DATA, "biggest_challenge": ""})
        assert ok is False
        assert "Biggest Challenge" in err

    def test_empty_commitment_returns_error(self):
        ok, err = validate_checkin({**VALID_DATA, "commitment": ""})
        assert ok is False
        assert "Commitment" in err

    def test_missing_text_field_key_returns_error(self):
        data = {k: v for k, v in VALID_DATA.items() if k != "top_win"}
        ok, err = validate_checkin(data)
        assert ok is False

    # Length validation
    def test_top_win_at_max_length_is_valid(self):
        ok, _ = validate_checkin({**VALID_DATA, "top_win": "a" * MAX_TEXT_LENGTH})
        assert ok is True

    def test_top_win_over_max_length_is_invalid(self):
        ok, err = validate_checkin({**VALID_DATA, "top_win": "a" * (MAX_TEXT_LENGTH + 1)})
        assert ok is False
        assert "500" in err

    def test_commitment_over_max_length_is_invalid(self):
        ok, err = validate_checkin({**VALID_DATA, "commitment": "x" * (MAX_TEXT_LENGTH + 1)})
        assert ok is False

    # Empty dict
    def test_empty_dict_returns_error(self):
        ok, err = validate_checkin({})
        assert ok is False


# --- build_checkin ---

class TestBuildCheckin:

    def test_returns_checkin_instance(self):
        result = build_checkin(VALID_DATA)
        assert isinstance(result, CheckIn)

    def test_fields_mapped_correctly(self):
        result = build_checkin(VALID_DATA)
        assert result.mood == VALID_DATA["mood"]
        assert result.top_win == VALID_DATA["top_win"]
        assert result.biggest_challenge == VALID_DATA["biggest_challenge"]
        assert result.commitment == VALID_DATA["commitment"]

    def test_text_fields_are_stripped(self):
        data = {**VALID_DATA, "top_win": "  great week  ", "commitment": "  do more  "}
        result = build_checkin(data)
        assert result.top_win == "great week"
        assert result.commitment == "do more"

    def test_mood_stored_as_int(self):
        result = build_checkin(VALID_DATA)
        assert isinstance(result.mood, int)
