from src.DBEngine import DBEngine
from src.ToDoWidget import ToDoWidget
from src.Task import Task

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QSpacerItem, QSizePolicy, QComboBox
from PyQt5.QtWidgets import QPushButton, QListWidget, QListWidgetItem


class MainWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setGeometry(200, 200, 500, 700)
        self.setWindowTitle("Focus To-Do")
        self.DB = DBEngine()
        self.initUI()

    def initUI(self):
        self.gridLayout = QGridLayout(self)

        self.label = QLabel("Мои задания")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayout.addItem(QSpacerItem(87, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 0,
                                1, 1, 1)

        self.status_label = QLabel("Состояние:")
        self.status_label.setMinimumSize(QtCore.QSize(100, 20))
        self.gridLayout.addWidget(self.status_label, 0, 2, 1, 1)

        self.status_box = QComboBox(self)
        self.status_box.setMinimumSize(QtCore.QSize(100, 0))

        self.status_box.addItem("Все")
        self.status_box.addItem("В процессе")
        self.status_box.addItem("Сделано")
        self.status_box.addItem("Просрочено")
        self.status_box.setCurrentIndex(0)
        self.gridLayout.addWidget(self.status_box, 0, 3, 1, 3)

        self.listWidget = QListWidget(self)
        self.load_table()
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 6)

        self.new_task_btn = QPushButton(self, text="Новое задание")
        self.new_task_btn.setMinimumSize(QtCore.QSize(100, 50))
        self.gridLayout.addWidget(self.new_task_btn, 2, 0, 1, 2)
        self.new_task_btn.clicked.connect(self.new_task_action)

        self.mark_as_btn = QPushButton(self, text="Отметить как выполненное")
        self.mark_as_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.gridLayout.addWidget(self.mark_as_btn, 2, 2, 1, 2)
        self.mark_as_btn.clicked.connect(self.mark_as_action)

        self.delete_btn = QPushButton(self, text="Удалить выделенное")
        self.delete_btn.setMinimumSize(QtCore.QSize(150, 50))
        self.gridLayout.addWidget(self.delete_btn, 2, 4, 1, 2)
        self.delete_btn.clicked.connect(self.delete_action)

    def new_task_action(self):
        Item = ToDoWidget(Task())
        Item.edit_btn.click()
        if Item.is_created:
            Item.is_added_to_List = True
            WidgetItem = QListWidgetItem(self.listWidget)
            WidgetItem.setSizeHint(Item.sizeHint())
            self.listWidget.addItem(WidgetItem)
            self.listWidget.setItemWidget(WidgetItem, Item)

    def mark_as_action(self):
        widget = self.listWidget.itemWidget(self.listWidget.currentItem())
        if widget is not None:
            widget.task.status_id = 1
            widget.display()

    def delete_action(self):
        self.listWidget.takeItem(self.listWidget.currentRow())

    def load_table(self):
        for task in self.DB.data:
            Item = ToDoWidget(task)
            WidgetItem = QListWidgetItem(self.listWidget)
            WidgetItem.setSizeHint(Item.sizeHint())
            self.listWidget.addItem(WidgetItem)
            self.listWidget.setItemWidget(WidgetItem, Item)

    def change_table(self):
        self.DB.data = [self.listWidget.itemWidget(self.listWidget.item(i)).task for i in
                        range(self.listWidget.count())]

    def closeEvent(self, event):
        self.change_table()
        self.DB.close()
        super(MainWindow, self).closeEvent(event)