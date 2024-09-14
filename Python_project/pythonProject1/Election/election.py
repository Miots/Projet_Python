import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QListWidget, QTextEdit, QInputDialog, QLabel, QMessageBox)

candidates = [
    {"name": "RAKOTO", "votes": 0},
    {"name": "RABE", "votes": 0},
]

class Election(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Election by Miots')
        self.setGeometry(100, 100, 400, 400)

        title_label = QLabel('Election', self)
        title_label.setStyleSheet('font-size: 20px; font-weight: bold;')

        self.candidates_list = QListWidget(self)
        for candidate in candidates:
            self.candidates_list.addItem(candidate["name"])

        self.vote_button = QPushButton('Voter', self)
        self.vote_button.setStyleSheet('background-color: rgb(78, 43, 3, 0.418); color: white; padding: 10px 24px; border: none; border-radius: 4px; cursor: pointer;')
        self.vote_button.clicked.connect(self.vote)

        self.results_button = QPushButton('Afficher les résultats', self)
        self.results_button.setStyleSheet('background-color: rgb(78, 43, 3, 0.418); color: white; padding: 10px 24px; border: none; border-radius: 4px; cursor: pointer;')
        self.results_button.clicked.connect(self.show_results)

        self.add_candidate_button = QPushButton('Ajouter un candidat', self)
        self.add_candidate_button.setStyleSheet('background-color: rgb(78, 43, 3, 0.418); color: white; padding: 10px 24px; border: none; border-radius: 4px; cursor: pointer;')
        self.add_candidate_button.clicked.connect(self.add_candidate)

        self.modify_candidate_button = QPushButton('Modifier le candidat', self)
        self.modify_candidate_button.setStyleSheet('background-color: rgb(78, 43, 3, 0.418); color: white; padding: 10px 24px; border: none; border-radius: 4px; cursor: pointer;')
        self.modify_candidate_button.clicked.connect(self.modify_candidate)

        self.results_label = QLabel('Résultats:', self)
        self.results_label.setStyleSheet('font-size: 16px; font-weight: bold;')
        self.results_label.hide()

        self.results_text = QTextEdit(self)
        self.results_text.setReadOnly(True)
        self.results_text.hide()

        layout = QVBoxLayout()
        layout.addWidget(title_label)
        layout.addWidget(self.candidates_list)
        layout.addWidget(self.vote_button)
        layout.addWidget(self.results_button)
        layout.addWidget(self.add_candidate_button)
        layout.addWidget(self.modify_candidate_button)
        layout.addWidget(self.results_label)
        layout.addWidget(self.results_text)
        self.setLayout(layout)

    def update_results(self):
        total_votes = sum(candidate["votes"] for candidate in candidates)
        self.results_text.clear()
        if total_votes > 0:
            for candidate in candidates:
                percentage = (candidate["votes"] / total_votes) * 100
                self.results_text.append(f"{candidate['name']} : {candidate['votes']} votes ({percentage:.2f}%)")
        else:
            self.results_text.append("Aucun vote enregistré pour le moment.")

    def vote(self):
        selected_candidate = self.candidates_list.currentRow()
        if selected_candidate != -1:
            candidates[selected_candidate]["votes"] += 1

    def show_results(self):
        self.update_results()
        self.results_label.show()
        self.results_text.show()

    def add_candidate(self):
        text, ok = QInputDialog.getText(self, "Ajouter un candidat", "Nom du candidat:")
        if ok and text.strip():
            candidates.append({"name": text.strip(), "votes": 0})
            self.candidates_list.addItem(text.strip())

    def modify_candidate(self):
        selected_candidate_index = self.candidates_list.currentRow()
        if selected_candidate_index != -1:
            new_name, ok = QInputDialog.getText(self, "Modifier le nom du candidat", "Nouveau nom du candidat:", text=candidates[selected_candidate_index]["name"])
            if ok and new_name.strip():
                candidates[selected_candidate_index]["name"] = new_name.strip()
                self.candidates_list.currentItem().setText(new_name.strip())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Attention!', "Êtes-vous sûr de vouloir quitter? Vos données peuvent être perdues",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = QApplication(sys.argv)
    ex = Election()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()