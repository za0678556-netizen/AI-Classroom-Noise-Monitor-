# main.py
import tkinter as tk
from sensor import NoiseSensor
from alert import AlertSystem
from ui import NoiseUI
from analytics import ClassroomAnalytics
from config import LOG_FILE

class App:
    def __init__(self, root):
        self.root = root
        self.sensor = NoiseSensor()
        self.alert = AlertSystem()
        self.ui = NoiseUI(root)
        self.analytics = ClassroomAnalytics(LOG_FILE)
        self.update()

    def update(self):
        db = self.sensor.get_db_level()
        status, message = self.alert.check_status(db)
        color = self.alert.get_color(status)
        self.ui.update_display(db, status, message, color)
        self.analytics.add_record(db, status)
        self.root.after(1000, self.update)

    def on_close(self):
        self.sensor.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
