import datetime
import pytest
from coaching_metrics.metrics import session_streak, goal_completion_rate, days_since_checkin


# --- session_streak ---

class TestSessionStreak:
    def _today(self):
        return datetime.date.today()

    def _days_ago(self, n):
        return self._today() - datetime.timedelta(days=n)

    def test_empty_list_returns_zero(self):
        assert session_streak([]) == 0

    def test_streak_of_one_today(self):
        assert session_streak([self._today()]) == 1

    def test_streak_of_two_consecutive_days(self):
        assert session_streak([self._today(), self._days_ago(1)]) == 2

    def test_streak_of_five_consecutive_days(self):
        dates = [self._days_ago(i) for i in range(5)]
        assert session_streak(dates) == 5

    def test_broken_streak_returns_zero_when_today_missing(self):
        # Yesterday and two days ago but NOT today — streak is 0
        assert session_streak([self._days_ago(1), self._days_ago(2)]) == 0

    def test_gap_in_middle_counts_only_from_today(self):
        # Today + 3 days ago (gap on days 1 and 2) — streak is 1
        assert session_streak([self._today(), self._days_ago(3)]) == 1

    def test_duplicate_dates_deduplicated(self):
        # Same date twice should not inflate the streak
        assert session_streak([self._today(), self._today()]) == 1

    def test_unordered_input_handled(self):
        dates = [self._days_ago(2), self._today(), self._days_ago(1)]
        assert session_streak(dates) == 3

    def test_future_date_breaks_streak_walk(self):
        # Future date sorts before today and breaks the descending walk — streak is 0.
        # Callers should filter future dates before passing to session_streak.
        future = self._today() + datetime.timedelta(days=1)
        assert session_streak([future, self._today()]) == 0

    def test_single_old_date_returns_zero(self):
        assert session_streak([self._days_ago(30)]) == 0


# --- goal_completion_rate ---

class TestGoalCompletionRate:
    def test_empty_list_returns_zero(self):
        assert goal_completion_rate([]) == 0.0

    def test_all_completed_returns_one(self):
        assert goal_completion_rate([True, True, True]) == 1.0

    def test_all_missed_returns_zero(self):
        assert goal_completion_rate([False, False, False]) == 0.0

    def test_half_completed(self):
        assert goal_completion_rate([True, False]) == pytest.approx(0.5)

    def test_two_thirds_completed(self):
        assert goal_completion_rate([True, True, False]) == pytest.approx(2 / 3)

    def test_single_true(self):
        assert goal_completion_rate([True]) == 1.0

    def test_single_false(self):
        assert goal_completion_rate([False]) == 0.0

    def test_result_between_zero_and_one(self):
        rate = goal_completion_rate([True, False, True, False, True])
        assert 0.0 <= rate <= 1.0

    def test_large_list(self):
        goals = [True] * 90 + [False] * 10
        assert goal_completion_rate(goals) == pytest.approx(0.9)


# --- days_since_checkin ---

class TestDaysSinceCheckin:
    def _today(self):
        return datetime.date.today()

    def _days_ago(self, n):
        return self._today() - datetime.timedelta(days=n)

    def test_none_input_returns_none(self):
        assert days_since_checkin(None) is None

    def test_today_returns_zero(self):
        assert days_since_checkin(self._today(), today=self._today()) == 0

    def test_one_day_ago(self):
        assert days_since_checkin(self._days_ago(1), today=self._today()) == 1

    def test_seven_days_ago(self):
        assert days_since_checkin(self._days_ago(7), today=self._today()) == 7

    def test_thirty_days_ago(self):
        assert days_since_checkin(self._days_ago(30), today=self._today()) == 30

    def test_explicit_today_parameter(self):
        ref = datetime.date(2024, 1, 10)
        last = datetime.date(2024, 1, 3)
        assert days_since_checkin(last, today=ref) == 7

    def test_future_date_raises_value_error(self):
        future = self._today() + datetime.timedelta(days=5)
        with pytest.raises(ValueError):
            days_since_checkin(future, today=self._today())
