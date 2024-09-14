import tkinter as tk
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QMessageBox)
class Chrono:
    def __init__(self, master):
        self.master = master
        master.title("Chronomètre")
        master.configure(bg="black")
        self.time_elapsed = timedelta()
        self.is_running = False
        self.lap_times = []
        self.time_label = tk.Label(master, text="00:00:00:00", font=("Helvetica", 48), bg="black", fg="white")
        self.time_label.pack(pady=20)
        self.play_button = tk.Button(master, width=10, height=2, text="Play", command=self.start_stop, bg="black", fg="white")
        self.play_button.pack(side=tk.LEFT, padx=15)
        self.pause_button = tk.Button(master, width=10, height=2, text="Pause", command=self.pause_resume, bg="black", fg="white", state="disabled")
        self.pause_button.pack(side=tk.LEFT, padx=15)
        self.add_button = tk.Button(master, width=10, height=2, text="Ajouter", command=self.record_lap, bg="black", fg="white")
        self.add_button.pack(side=tk.LEFT, padx=15)
        self.reset_button = tk.Button(master, width=10, height=2, text="Recommencer", command=self.reset, bg="black", fg="white")
        self.reset_button.pack(side=tk.LEFT, padx=15)
        self.lap_listbox = tk.Listbox(master, width=20, height=10, bg="black", fg="white")
        self.lap_listbox.pack(side=tk.RIGHT, padx=10)
        self.update_time()

    def start_stop(self):
        if not self.is_running:
            self.start_time = datetime.now()
            self.is_running = True
            self.play_button.config(text="Stop", fg="white")
            self.pause_button.config(state="normal")
            self.master.after(10, self.update_time)
        else:
            self.time_elapsed += datetime.now() - self.start_time
            self.is_running = False
            self.play_button.config(text="Play", fg="white")
            self.pause_button.config(state="disabled")

    def pause_resume(self):
        if self.is_running:
            self.time_elapsed += datetime.now() - self.start_time
            self.is_running = False
            self.play_button.config(text="Play", fg="white")
            self.pause_button.config(text="Resume")
        else:
            self.start_time = datetime.now()
            self.is_running = True
            self.play_button.config(text="Stop", fg="white")
            self.pause_button.config(text="Pause")
            self.master.after(10, self.update_time)

    def record_lap(self):
        if self.is_running:
            lap_time = datetime.now() - self.start_time + self.time_elapsed
            self.lap_times.append(lap_time)
            self.lap_listbox.insert(tk.END, f"{len(self.lap_times)}. {self.format_time(lap_time)}")

    def reset(self):
        self.time_elapsed = timedelta()
        self.is_running = False
        self.lap_times = []
        self.time_label.config(text="00:00:00:00", fg="white")
        self.lap_listbox.delete(0, tk.END)
        self.play_button.config(text="Play", fg="white")
        self.pause_button.config(text="Pause", state="disabled")

    def update_time(self):
        if self.is_running:
            current_time = datetime.now() - self.start_time + self.time_elapsed
            self.time_label.config(text=self.format_time(current_time), fg="white")
            self.master.after(10, self.update_time)

    def format_time(self, time):
        hours = int(time.seconds // 3600)
        minutes = int((time.seconds % 3600) // 60)
        seconds = int(time.seconds % 60)
        milliseconds = int(time.microseconds / 10000)  # Convert microseconds to milliseconds
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:02d}"
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Attention!', "Êtes-vous sûr de vouloir quitter? Vos données peuvent être perdues",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
root = tk.Tk()
chronometer = Chrono(root)
root.mainloop()
