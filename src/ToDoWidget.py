import os
from src import path
from src.Dialog import Dialog

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap


class ToDoWidget(QWidget):
    def __init__(self, task, parent=None):
        super(QWidget, self).__init__(parent)
        self.is_added_to_List = False
        self.is_created = True
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

        self.display()

        self.edit_btn = QPushButton(self, text="Открыть")
        self.edit_btn.setMaximumSize(100, 20)
        self.HBoxLayout.addWidget(self.edit_btn, 2)
        self.edit_btn.clicked.connect(Dialog(self).exec)

        self.setLayout(self.HBoxLayout)

    def display(self):
        self.name.setText(self.task.name)
        self.status_icon.setPixmap(self.pics[self.task.status_id])


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = ToDoWidget(Task(nm="sdgdfgh dhfghd dfhdfhdf", ds="aadssss", st=1))
#     ex.show()
#     sys.exit(app.exec_())
