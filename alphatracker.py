import psutil
import time
import json
from datetime import datetime
from collections import defaultdict

class AlphaTracker:
    def __init__(self, log_interval=60):
        self.log_interval = log_interval
        self.app_usage_stats = defaultdict(lambda: {"usage_time": 0, "last_active": None})

    def track_usage(self):
        try:
            while True:
                active_app = self.get_active_window()
                if active_app:
                    self.log_usage(active_app)
                time.sleep(self.log_interval)
        except KeyboardInterrupt:
            self.save_stats()
            print("Stopped tracking and saved stats.")

    def get_active_window(self):
        try:
            import win32gui
            window = win32gui.GetForegroundWindow()
            window_title = win32gui.GetWindowText(window)
            return window_title
        except ImportError:
            print("Error: win32gui module is required on Windows to get the active window.")
            return None
    
    def log_usage(self, active_app):
        current_time = time.time()
        if self.app_usage_stats[active_app]["last_active"]:
            duration = current_time - self.app_usage_stats[active_app]["last_active"]
            self.app_usage_stats[active_app]["usage_time"] += duration
        self.app_usage_stats[active_app]["last_active"] = current_time

    def save_stats(self):
        # Clean up last active times
        for app in self.app_usage_stats:
            self.app_usage_stats[app]["last_active"] = None

        # Save stats to a JSON file
        with open("app_usage_stats.json", "w") as file:
            json.dump(self.app_usage_stats, file, indent=4)
        print("Usage statistics saved to app_usage_stats.json")

    def load_stats(self):
        try:
            with open("app_usage_stats.json", "r") as file:
                self.app_usage_stats = json.load(file)
        except FileNotFoundError:
            print("No existing statistics found. Starting fresh.")
    
    def display_insights(self):
        print("Application Usage Insights:")
        for app, stats in self.app_usage_stats.items():
            usage_time = self.format_duration(stats["usage_time"])
            print(f"{app}: {usage_time}")

    def format_duration(self, duration):
        hours, remainder = divmod(duration, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

if __name__ == "__main__":
    tracker = AlphaTracker(log_interval=60)
    tracker.load_stats()
    tracker.track_usage()