from src import path
from src.DBEngine import DBEngine
from src.ToDoWidget import ToDoWidget
from src.Task import Task

import os
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QSpacerItem, QSizePolicy, QComboBox
from PyQt5.QtWidgets import QPushButton, QListWidget, QListWidgetItem


class MainWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setWindowIcon(QIcon(os.path.join(path, "img", 'icon.ico')))
        self.setGeometry(200, 200, 600, 600)
        self.setWindowTitle("Focus")
        self.DB = DBEngine()
        self.initUI()

    def initUI(self):
        self.gridLayout = QGridLayout(self)

        self.label = QLabel("Мои задания")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayout.addItem(QSpacerItem(87, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, 1, 1, 1)

        self.status_label = QLabel("Состояние:")
        self.status_label.setMinimumSize(QtCore.QSize(100, 20))
        self.gridLayout.addWidget(self.status_label, 0, 2, 1, 1)

        self.status_box = QComboBox(self)
        self.status_box.setMinimumSize(QtCore.QSize(100, 0))

        self.status_box.addItem("В процессе")
        self.status_box.addItem("Сделано")
        self.status_box.addItem("Просрочено")
        self.status_box.addItem("Все")
        self.status_box.setCurrentIndex(3)
        self.gridLayout.addWidget(self.status_box, 0, 3, 1, 3)
        self.status_box.currentIndexChanged.connect(self.customize_table)

        self.listWidget = QListWidget(self)
        self.load_table(self.DB.get_data(), clear_data=True)
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 6)

        self.new_task_btn = QPushButton(text="Новое задание")
        self.new_task_btn.setMinimumSize(QtCore.QSize(100, 50))
        self.gridLayout.addWidget(self.new_task_btn, 2, 0, 1, 2)
        self.new_task_btn.clicked.connect(self.new_task_action)

        self.mark_as_btn = QPushButton(text="Отметить как выполненное")
        self.mark_as_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.gridLayout.addWidget(self.mark_as_btn, 2, 2, 1, 2)
        self.mark_as_btn.clicked.connect(self.mark_as_action)

        self.delete_btn = QPushButton(text="Удалить выделенное")
        self.delete_btn.setMinimumSize(QtCore.QSize(150, 50))
        self.gridLayout.addWidget(self.delete_btn, 2, 4, 1, 2)
        self.delete_btn.clicked.connect(self.delete_action)

    def new_task_action(self):
        item = ToDoWidget(Task(), self)
        item.edit_btn.click()
        if item.is_created:
            item.is_added_to_List = True
            widget_item = QListWidgetItem(self.listWidget)
            widget_item.setSizeHint(item.sizeHint())
            self.listWidget.addItem(widget_item)
            self.listWidget.setItemWidget(widget_item, item)
        self.customize_table()

    def mark_as_action(self):
        widget = self.listWidget.itemWidget(self.listWidget.currentItem())
        if widget is not None:
            widget.task.status_id = 1
            widget.display()
        self.customize_table()

    def delete_action(self):
        self.listWidget.takeItem(self.listWidget.currentRow())

    def load_table(self, data, clear_data=False):
        self.listWidget.clear()
        for task in data:
            item = ToDoWidget(task, self)
            widget_item = QListWidgetItem(self.listWidget)
            widget_item.setSizeHint(item.sizeHint())
            self.listWidget.addItem(widget_item)
            self.listWidget.setItemWidget(widget_item, item)
        if clear_data:
            self.DB.clear_data()

    def customize_table(self):
        index = self.status_box.currentIndex()
        self.save_changes()
        data = self.DB.get_data()
        if index == 3:
            self.load_table(data, clear_data=True)
        else:
            self.load_table(filter(lambda x: x.status_id == index, data))
            self.DB.update_data(list(filter(lambda x: x.status_id != index, data)))

    def save_changes(self):
        self.DB.update_data([self.listWidget.itemWidget(self.listWidget.item(i)).task for i in range(self.listWidget.count())], mode="a")

    def closeEvent(self, event):
        self.save_changes()
        self.DB.close()
        super(MainWindow, self).closeEvent(event)
