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

        imp_l = QLabel("Важность")
        layout.addWidget(imp_l)

        self.imp_box = QComboBox()
        self.imp_box.setMinimumSize(QSize(150, 0))
        self.imp_box.addItem("Обычное")
        self.imp_box.addItem("Важное")
        self.imp_box.setCurrentIndex(self.main.task.is_imp)
        layout.addWidget(self.imp_box)

        h_box_layout = QHBoxLayout()

        p_btn = QPushButton('Сохранить')
        h_box_layout.addWidget(p_btn, 0)
        p_btn.clicked.connect(self.push)

        c_btn = QPushButton('Отмена')
        h_box_layout.addWidget(c_btn, 1)
        c_btn.clicked.connect(self.cancel)

        layout.addLayout(h_box_layout)
        self.setLayout(layout)

    def push(self):
        self.main.is_created = True
        self.main.task.name = self.name.text()
        self.main.task.description = self.desc.toPlainText()
        self.main.task.status_id = self.status_box.currentIndex()
        self.main.task.is_imp = self.imp_box.currentIndex()
        self.main.display()
        self.close()

    def cancel(self):
        self.main.display()
        self.close()

    def closeEvent(self, event):
        if self.main.is_created:
            super(Dialog, self).closeEvent(event)
        else:
            self.cancel()
