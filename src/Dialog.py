from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QComboBox, QPushButton, QDateEdit, QCheckBox
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

        imp_l = QLabel("Важность:")
        layout.addWidget(imp_l)

        self.imp_box = QComboBox()
        self.imp_box.setMinimumSize(QSize(150, 0))
        self.imp_box.addItem("Обычное")
        self.imp_box.addItem("Важное")
        self.imp_box.setCurrentIndex(self.main.task.is_imp)
        layout.addWidget(self.imp_box)

        self.have_date = QCheckBox(text="Дата:")
        self.have_date.setCheckState(self.main.task.have_dt)
        layout.addWidget(self.have_date)
        self.have_date.stateChanged.connect(self.date_state_change)

        date_l = QLabel("Дата:")
        layout.addWidget(date_l)

        self.date_edit = QDateEdit()
        self.date_edit.setDate(self.main.task.date)
        self.date_edit.setMinimumSize(QSize(150, 0))
        self.date_state_change()
        layout.addWidget(self.date_edit)

        button_layout = QHBoxLayout()

        p_btn = QPushButton('Сохранить')
        button_layout.addWidget(p_btn, 0)
        self.p_btn_pushed = False
        p_btn.clicked.connect(self.push)

        c_btn = QPushButton('Отмена')
        button_layout.addWidget(c_btn, 1)
        c_btn.clicked.connect(self.cancel)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def date_state_change(self):
        self.date_edit.setEnabled(self.have_date.isChecked())

    def push(self):
        self.main.task.name = self.name.text()
        self.main.task.description = self.desc.toPlainText()
        if self.main.task.status_id != self.status_box.currentIndex():
            self.main.task.status_id = self.status_box.currentIndex()
            self.main.status_changed = True
        self.main.task.is_imp = self.imp_box.currentIndex()
        self.main.task.have_dt = self.have_date.isChecked()
        self.main.task.date = self.date_edit.date().toPyDate()
        self.main.is_created = True
        self.p_btn_pushed = True
        self.main.display()
        self.close()

    def cancel(self):
        self.main.display()
        self.close()

    def closeEvent(self, event):
        if self.main.is_created and self.p_btn_pushed:
            super(Dialog, self).closeEvent(event)
        else:
            self.cancel()
