# alert.py
from config import THRESHOLD_QUIET, THRESHOLD_NOISY

class AlertSystem:
    def check_status(self, db_level):
        if db_level > THRESHOLD_NOISY:
            return "NOISY", "🔴 Class is too noisy! Be quiet."
        elif db_level > THRESHOLD_QUIET:
            return "MODERATE", "🟡 Getting loud. Keep it down."
        else:
            return "QUIET", "🟢 Great! Classroom is quiet."

    def get_color(self, status):
        colors = {
            "QUIET": "green",
            "MODERATE": "yellow", 
            "NOISY": "red"
        }
        return colors.get(status, "white")
