# analytics.py
import json
from collections import defaultdict
from datetime import datetime

class ClassroomAnalytics:
    def __init__(self, log_file="noise_log.json"):
        self.log_file = log_file
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.log_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.log_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_record(self, db_level, status):
        record = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "db": db_level,
            "status": status
        }
        self.data.append(record)
        self.save_data()

    def get_daily_report(self):
        report = defaultdict(list)
        for record in self.data:
            day = record["timestamp"].split(" ")[0]
            report[day].append(record["db"])

        summary = {}
        for day, levels in report.items():
            avg_db = sum(levels) / len(levels)
            summary[day] = round(avg_db, 2)
        return summary

    def get_peak_noise(self):
        if not self.data:
            return 0
        return max(record["db"] for record in self.data)
