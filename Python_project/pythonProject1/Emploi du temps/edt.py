import tkinter as tk
from datetime import datetime, timedelta

class Course:
    def __init__(self, nom, salle, classe, prof, debut, fin, jour):
        self.nom = nom
        self.salle = salle
        self.classe = classe
        self.prof = prof
        self.debut = debut
        self.fin = fin
        self.jour = jour

    def display_info(self, parent):
        info_window = tk.Toplevel(parent)
        info_window.title(self.nom)
        info_label = tk.Label(info_window, text=f"""
Matière : {self.nom}
Jour : {self.jour}
Heure : {self.debut} - {self.fin}
Professeur : {self.prof}
""", font=("Arial", 14))
        info_label.pack(padx=20, pady=20)

class EmploiduTemps(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Emploi du temps")
        self.courses = [
            Course("Mathématiques", "A002", "L2IRDE", "Mme Jacky", "08h00", "10h00", "Lundi"),
            Course("Java", "A003", "L2IRD2", "Mr Tojo", "10h30", "12h30", "Mardi"),
            Course("Python", "B200", "L2IRD2", "Mr Tojo", "14h00", "16h00", "Mercredi"),
            Course("Francais", "LABO", "L2IRD2", "Mme Julia", "16h30", "18h30", "Jeudi")
        ]
        self.jour_colors = ["grey", "grey", "grey", "grey", "grey", "grey"]
        self.create_jour_selection()

    def create_jour_selection(self):
        jour_frame = tk.Frame(self)
        jour_frame.pack(pady=20)
        jour_label = tk.Label(jour_frame, text="Choisissez un jour :", font=("Arial", 12, "bold"))
        jour_label.grid(row=0, column=0, padx=10, pady=5)

        jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]

        for i, jour in enumerate(jours):
            jour_button = tk.Button(jour_frame, text=jour, command=lambda d=jour: self.create_schedule_table(d),
                                           font=("Arial", 12), fg="white", bg=self.jour_colors[i])
            jour_button.grid(row=1, column=i, padx=10, pady=5)

    def create_schedule_table(self, jour):
        self.selected_jour = jour
        table_frame = tk.Frame(self)
        table_frame.pack(pady=20)

        header_labels = ["Matière", "Salle", "Classe", "Enseignant"]
        for i, label in enumerate(header_labels):
            header_label = tk.Label(table_frame, text=label, font=("Arial", 12, "bold"))
            header_label.grid(row=0, column=i, padx=10, pady=5)

        for i, course in enumerate(self.courses, start=1):
            if course.jour == jour:
                course_label = tk.Button(table_frame, text=f"{course.nom}",
                                         command=lambda c=course: c.display_info(self), font=("Arial", 12),
                                         fg=self.jour_colors[["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi",
                                                             "Samedi"].index(jour)])
                course_label.grid(row=i, column=0, padx=10, pady=5)
                salle_label = tk.Label(table_frame, text=course.salle, font=("Arial", 12))
                salle_label.grid(row=i, column=1, padx=10, pady=5)
                class_label = tk.Label(table_frame, text=course.classe, font=("Arial", 12))
                class_label.grid(row=i, column=2, padx=10, pady=5)
                prof_label = tk.Label(table_frame, text=course.prof, font=("Arial", 12))
                prof_label.grid(row=i, column=3, padx=10, pady=5)

if __name__ == "__main__":
    app = EmploiduTemps()
    app.mainloop()