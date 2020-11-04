from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QComboBox, QPushButton
from PyQt5.QtCore import QSize


class Dialog(QDialog):
    def __init__(self, root):
        super().__init__(root)
        self.setWindowTitle("Редактор заданий")
        self.main = root
        layout = QVBoxLayout()

        name_l = QLabel('Название:')
        layout.addWidget(name_l)

        self.name = QLineEdit()
        self.name.setText(self.main.task.name)
        layout.addWidget(self.name)

        desc_l = QLabel('Описание:')
        layout.addWidget(desc_l)

        self.desc = QTextEdit()
        self.desc.setText(self.main.task.description)
        layout.addWidget(self.desc)

        status_l = QLabel("Статус задания:")
        layout.addWidget(status_l)

        self.status_box = QComboBox()
        self.status_box.setMinimumSize(QSize(150, 0))
        self.status_box.addItem("В процессе")
        self.status_box.addItem("Сделано")
        self.status_box.addItem("Просрочено")
        self.status_box.setCurrentIndex(self.main.task.status_id)
        layout.addWidget(self.status_box)

        HBoxLayout = QHBoxLayout()

        pBtn = QPushButton('Сохранить')
        HBoxLayout.addWidget(pBtn, 0)
        pBtn.clicked.connect(self.push)

        cBtn = QPushButton('Отмена')
        HBoxLayout.addWidget(cBtn, 1)
        cBtn.clicked.connect(self.cancel)

        layout.addLayout(HBoxLayout)
        self.setLayout(layout)

    def push(self):
        self.main.task.name = self.name.text()
        self.main.task.description = self.desc.toPlainText()
        self.main.task.status_id = self.status_box.currentIndex()
        self.main.display()
        self.close()

    def cancel(self):
        if not self.main.is_added_to_List:
            self.main.is_created = False
        self.main.display()
        self.close()
