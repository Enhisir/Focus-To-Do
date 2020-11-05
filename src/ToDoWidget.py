import os
from src import path
from src.Dialog import Dialog

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap


class ToDoWidget(QWidget):
    def __init__(self, task, parent=None):
        super(QWidget, self).__init__(parent)
        self.is_created = False
        self.pics = {
            0: QPixmap(os.path.join(path, "img", "in progress.png")),
            1: QPixmap(os.path.join(path, "img", "done.png")),
            2: QPixmap(os.path.join(path, "img", "failed.jpg")),
        }
        self.task = task
        self.HBoxLayout = QHBoxLayout()

        self.status_icon = QLabel()
        self.status_icon.setMinimumSize(50, 50)
        self.status_icon.setMaximumSize(50, 50)
        self.HBoxLayout.addWidget(self.status_icon, 0)

        self.name = QLabel(self)
        self.HBoxLayout.addWidget(self.name, 1)

        self.is_imp = QLabel(self)
        self.HBoxLayout.addWidget(self.is_imp, 2)

        self.display()

        self.edit_btn = QPushButton(self, text="Открыть")
        self.edit_btn.setMaximumSize(100, 20)
        self.HBoxLayout.addWidget(self.edit_btn, 3)
        self.edit_btn.clicked.connect(Dialog(self).exec)

        self.setLayout(self.HBoxLayout)

    def display(self):
        self.status_icon.setPixmap(self.pics[self.task.status_id])
        if len(self.task.name) > 30:
            self.name.setText(self.task.name[:27] + "...")
        else:
            self.name.setText(self.task.name)
        self.is_imp.setText("Важное" if self.task.is_imp == 1 else "")
