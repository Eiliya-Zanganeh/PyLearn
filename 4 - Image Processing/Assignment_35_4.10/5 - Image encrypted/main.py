from functools import partial
import os

from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import cv2 as cv

from main_ui import Ui_MainWindow
import image_encryption


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.encrypt_image_input = None
        self.decrypt_image_input = None
        self.key = None
        self.file_name = None

        self.ui.encrypt_select_img_btn.clicked.connect(partial(self.select_file, self.ui.encrypt_input_lbl, 'encrypt'))
        self.ui.decrypt_select_img_btn.clicked.connect(partial(self.select_file, self.ui.decrypt_input_lbl, 'decrypt'))

        self.ui.select_key_btn.clicked.connect(self.select_key)

        self.ui.encrypt_image_btn.clicked.connect(self.encrypt_image)
        self.ui.decrypt_image_btn.clicked.connect(self.decrypt_image)

        if not os.path.exists('outputs'):
            os.mkdir('outputs')

    def select_file(self, label, tab):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp);;All Files (*)",
            options=options
        )
        if file_path:
            image = cv.imread(file_path, cv.IMREAD_UNCHANGED)
            if image is not None:
                file_name = file_path.split("/")[-1]
                file_name = file_name.split(".")[0]
                self.file_name = file_name
                if tab == 'encrypt':
                    self.encrypt_image_input = file_path
                elif tab == 'decrypt':
                    self.decrypt_image_input = file_path
                if image.shape[2] == 4:
                    image = cv.cvtColor(image, cv.COLOR_BGRA2BGR)
                image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
                self.apply_image_to_label(image, label)
            else:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Error opening file !")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setText("Image is not valid")
                msgBox.exec()

    def select_key(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Key", "", "key (*.npy);",
            options=options
        )
        if file_path:
            self.key = file_path
            file_name = file_path.split("/")[-1]
            self.ui.selected_key_lbl.setText(file_name)

    def apply_image_to_label(self, image_RGB, label):
        height, width, channel = image_RGB.shape
        label_width = label.width()
        label_height = int(label_width * height / width)
        resized_image = cv.resize(image_RGB, (label_width, label_height))
        q_image = QImage(resized_image.data, label_width, label_height, 3 * label_width, QImage.Format_RGB888)
        pixmap = QPixmap(q_image)
        label.setPixmap(pixmap)

    def encrypt_image(self):
        if self.encrypt_image_input:
            output_path = f'outputs/{self.file_name}'
            if not os.path.exists(output_path):
                os.mkdir(output_path)
            image, _ = image_encryption.encrypt(self.encrypt_image_input, output_path, self.file_name)
            self.apply_image_to_label(image, self.ui.encrypt_output_lbl)
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Image Encrypted !")
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText(f"Image Encrypted in {output_path}")
            msgBox.exec()
        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Image not Selected !")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(f"Please select an image")
            msgBox.exec()

    def decrypt_image(self):
        if self.decrypt_image_input and self.key:
            output_path = f'outputs/{self.file_name}'
            if not os.path.exists(output_path):
                os.mkdir(output_path)
            try:
                image = image_encryption.decrypt(self.decrypt_image_input, self.key, output_path, self.file_name)
            except ValueError as error:
                msgBox = QMessageBox()
                msgBox.setWindowTitle("Error in decryption image !")
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setText(str(error))
                msgBox.exec()
            image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
            self.apply_image_to_label(image, self.ui.decrypt_output_lbl)
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Image Decrypted !")
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText(f"Image Decrypted in {output_path}")
            msgBox.exec()
        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Image or key not Selected !")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(f"Please select an image or key")
            msgBox.exec()


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
