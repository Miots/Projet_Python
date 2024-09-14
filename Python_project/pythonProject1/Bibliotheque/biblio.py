import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connexion à la base de données (ou création si elle n'existe pas)
connexion = sqlite3.connect('bibliotheque.db')
cursor = connexion.cursor()

# Création des tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS livres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titre TEXT,
        auteur TEXT,
        disponible BOOLEAN
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS membres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        email TEXT
    )
''')
connexion.commit()


# Fonctions de la base de données
def ajouter_livre(titre, auteur):
    cursor.execute('''
        INSERT INTO livres (titre, auteur, disponible) 
        VALUES (?, ?, ?)
    ''', (titre, auteur, True))
    connexion.commit()


def supprimer_livre(livre_id):
    cursor.execute('''
        DELETE FROM livres WHERE id = ?
    ''', (livre_id,))
    connexion.commit()


def modifier_livre(livre_id, titre, auteur):
    cursor.execute('''
        UPDATE livres SET titre = ?, auteur = ? WHERE id = ?
    ''', (titre, auteur, livre_id))
    connexion.commit()


def ajouter_membre(nom, email):
    cursor.execute('''
        INSERT INTO membres (nom, email) 
        VALUES (?, ?)
    ''', (nom, email))
    connexion.commit()


def supprimer_membre(membre_id):
    cursor.execute('''
        DELETE FROM membres WHERE id = ?
    ''', (membre_id,))
    connexion.commit()


def modifier_membre(membre_id, nom, email):
    cursor.execute('''
        UPDATE membres SET nom = ?, email = ? WHERE id = ?
    ''', (nom, email, membre_id))
    connexion.commit()


class Bibliotheque:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Bibliothèque by Miots")
        self.root.geometry("800x600")

        self.livres_frame = tk.LabelFrame(root, text="Livres")
        self.livres_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.titre_label = tk.Label(self.livres_frame, text="Titre:")
        self.titre_label.grid(row=0, column=0, padx=5, pady=5)
        self.titre_entry = tk.Entry(self.livres_frame)
        self.titre_entry.grid(row=0, column=1, padx=5, pady=5)

        self.auteur_label = tk.Label(self.livres_frame, text="Auteur:")
        self.auteur_label.grid(row=1, column=0, padx=5, pady=5)
        self.auteur_entry = tk.Entry(self.livres_frame)
        self.auteur_entry.grid(row=1, column=1, padx=5, pady=5)

        self.ajouter_livre_btn = tk.Button(self.livres_frame, text="Ajouter Livre", command=self.ajouter_livre)
        self.ajouter_livre_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.supprimer_livre_btn = tk.Button(self.livres_frame, text="Supprimer Livre", command=self.supprimer_livre)
        self.supprimer_livre_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.modifier_livre_btn = tk.Button(self.livres_frame, text="Modifier Livre", command=self.modifier_livre)
        self.modifier_livre_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.livres_listbox = tk.Listbox(self.livres_frame)
        self.livres_listbox.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.charger_livres()

        self.membres_frame = tk.LabelFrame(root, text="Membres")
        self.membres_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.nom_label = tk.Label(self.membres_frame, text="Nom:")
        self.nom_label.grid(row=0, column=0, padx=5, pady=5)
        self.nom_entry = tk.Entry(self.membres_frame)
        self.nom_entry.grid(row=0, column=1, padx=5, pady=5)

        self.email_label = tk.Label(self.membres_frame, text="Email:")
        self.email_label.grid(row=1, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.membres_frame)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        self.ajouter_membre_btn = tk.Button(self.membres_frame, text="Ajouter Membre", command=self.ajouter_membre)
        self.ajouter_membre_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.supprimer_membre_btn = tk.Button(self.membres_frame, text="Supprimer Membre",
                                              command=self.supprimer_membre)
        self.supprimer_membre_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.modifier_membre_btn = tk.Button(self.membres_frame, text="Modifier Membre", command=self.modifier_membre)
        self.modifier_membre_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.membres_listbox = tk.Listbox(self.membres_frame)
        self.membres_listbox.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.charger_membres()

        # Configure les colonnes et les lignes pour l'expansion
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.livres_frame.grid_rowconfigure(5, weight=1)
        self.membres_frame.grid_rowconfigure(5, weight=1)

    def ajouter_livre(self):
        titre = self.titre_entry.get()
        auteur = self.auteur_entry.get()
        if titre and auteur:
            ajouter_livre(titre, auteur)
            self.charger_livres()
        else:
            messagebox.showwarning("Entrée invalide", "Veuillez entrer le titre et l'auteur.")

    def supprimer_livre(self):
        selection = self.livres_listbox.curselection()
        if selection:
            livre_id = self.livres_listbox.get(selection[0]).split()[0]
            supprimer_livre(livre_id)
            self.charger_livres()
        else:
            messagebox.showwarning("Sélection invalide", "Veuillez sélectionner un livre à supprimer.")

    def modifier_livre(self):
        selection = self.livres_listbox.curselection()
        if selection:
            livre_id = self.livres_listbox.get(selection[0]).split()[0]
            titre = self.titre_entry.get()
            auteur = self.auteur_entry.get()
            if titre and auteur:
                modifier_livre(livre_id, titre, auteur)
                self.charger_livres()
            else:
                messagebox.showwarning("Entrée invalide", "Veuillez entrer le titre et l'auteur.")
        else:
            messagebox.showwarning("Sélection invalide", "Veuillez sélectionner un livre à modifier.")

    def ajouter_membre(self):
        nom = self.nom_entry.get()
        email = self.email_entry.get()
        if nom and email:
            ajouter_membre(nom, email)
            self.charger_membres()
        else:
            messagebox.showwarning("Entrée invalide", "Veuillez entrer le nom et l'email.")

    def supprimer_membre(self):
        selection = self.membres_listbox.curselection()
        if selection:
            membre_id = self.membres_listbox.get(selection[0]).split()[0]
            supprimer_membre(membre_id)
            self.charger_membres()
        else:
            messagebox.showwarning("Sélection invalide", "Veuillez sélectionner un membre à supprimer.")

    def modifier_membre(self):
        selection = self.membres_listbox.curselection()
        if selection:
            membre_id = self.membres_listbox.get(selection[0]).split()[0]
            nom = self.nom_entry.get()
            email = self.email_entry.get()
            if nom and email:
                modifier_membre(membre_id, nom, email)
                self.charger_membres()
            else:
                messagebox.showwarning("Entrée invalide", "Veuillez entrer le nom et l'email.")
        else:
            messagebox.showwarning("Sélection invalide", "Veuillez sélectionner un membre à modifier.")

    def charger_livres(self):
        self.livres_listbox.delete(0, tk.END)
        cursor.execute('SELECT id, titre, auteur FROM livres')
        for livre in cursor.fetchall():
            self.livres_listbox.insert(tk.END, f"{livre[0]} - {livre[1]} ({livre[2]})")

    def charger_membres(self):
        self.membres_listbox.delete(0, tk.END)
        cursor.execute('SELECT id, nom, email FROM membres')
        for membre in cursor.fetchall():
            self.membres_listbox.insert(tk.END, f"{membre[0]} - {membre[1]} ({membre[2]})")


root = tk.Tk()
app = Bibliotheque(root)
root.mainloop()

connexion.close()
