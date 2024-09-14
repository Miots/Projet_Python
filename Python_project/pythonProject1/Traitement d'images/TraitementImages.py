import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QComboBox
from PyQt5.QtGui import QPixmap, QImage, QTransform

class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Traitement d'image by Miots")
        self.setGeometry(100, 100, 800, 600)
        self.setFixedSize(800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.boutons_layout = QVBoxLayout()
        self.layout.addLayout(self.boutons_layout)

        self.label_image = QLabel()
        self.layout.addWidget(self.label_image)

        self.bouton_charger_image = QPushButton("Selectionner une image")
        self.bouton_charger_image.clicked.connect(self.charger_image)
        self.boutons_layout.addWidget(self.bouton_charger_image)

        self.combo_effet = QComboBox()
        self.combo_effet.addItems(["Inverser les couleurs", "Noir et blanc", "Mirroir vertical", "Mirroir horizontal"])
        self.boutons_layout.addWidget(self.combo_effet)

        self.bouton_appliquer_effet = QPushButton("Appliquer les modifications")
        self.bouton_appliquer_effet.clicked.connect(self.appliquer_effet)
        self.boutons_layout.addWidget(self.bouton_appliquer_effet)

        self.bouton_reinitialiser = QPushButton("Réinitialiser l'image")
        self.bouton_reinitialiser.clicked.connect(self.reinitialiser_image)
        self.boutons_layout.addWidget(self.bouton_reinitialiser)

        self.chemin_image = None
        self.image_originale = None

    def charger_image(self):
        chemin, _ = QFileDialog.getOpenFileName(self, "Sélectionnez une image", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if chemin:
            self.chemin_image = chemin
            pixmap = QPixmap(chemin)
            self.image_originale = pixmap
            self.label_image.setPixmap(pixmap.scaledToWidth(min(800, pixmap.width())))

    def appliquer_effet(self):
        if self.chemin_image:
            effet = self.combo_effet.currentText()
            if effet == "Inverser les couleurs":
                self.inverser_couleurs()
            elif effet == "Noir et blanc":
                self.noir_et_blanc()
            elif effet == "Mirroir vertical":
                self.rotation_gauche()
            elif effet == "Mirroir horizontal":
                self.rotation_droit()
        else:
            print("Aucune image selectionnée.")

    def inverser_couleurs(self):
        image = QImage(self.chemin_image)
        image.invertPixels()
        pixmap = QPixmap.fromImage(image)
        self.label_image.setPixmap(pixmap.scaledToWidth(min(800, pixmap.width())))

    def noir_et_blanc(self):
        image = QImage(self.chemin_image)
        image = image.convertToFormat(QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(image)
        self.label_image.setPixmap(pixmap.scaledToWidth(min(800, pixmap.width())))

    def rotation_gauche(self):
        image = QImage(self.chemin_image)
        image = image.mirrored(True, False)  # Miroir gauche
        pixmap = QPixmap.fromImage(image)
        self.label_image.setPixmap(pixmap.scaledToWidth(min(800, pixmap.width())))

    def rotation_droit(self):
        image = QImage(self.chemin_image)
        image = image.mirrored(False, True)  # Miroir droit
        pixmap = QPixmap.fromImage(image)
        self.label_image.setPixmap(pixmap.scaledToWidth(min(800, pixmap.width())))

    def reinitialiser_image(self):
        if self.image_originale:
            self.label_image.setPixmap(self.image_originale.scaledToWidth(min(800, self.image_originale.width())))
        else:
            print("Aucune image chargée.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Fenetre()
    window.show()
    sys.exit(app.exec_())
