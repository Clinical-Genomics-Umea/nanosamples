from PySide6.QtWidgets import QToolBox, QTextEdit, QTableWidget, QTableWidgetItem, \
    QHeaderView, QAbstractItemView, QListView
from PySide6.QtCore import QStringListModel


class IndexPicker(QToolBox):
    def __init__(self, parent=None):
        super().__init__(parent)

    def add_indexes(self, name: str, indexes: dict):
        w = QTableWidget()
        w.setDragEnabled(True)

        num_rows = len(indexes)
        num_cols = 1

        w.setRowCount(num_rows)
        w.setColumnCount(num_cols)

        w.setHorizontalHeaderItem(0, QTableWidgetItem("barcode"))

        for i, key in enumerate(indexes):
            barcode_name = QTableWidgetItem(key)
            w.setItem(i, 0, barcode_name)

        w.horizontalHeader().setStretchLastSection(True)
        w.verticalHeader().hide()
        w.horizontalHeader().hide()

        self.addItem(w, name)


class IndexListPicker(QToolBox):
    def __init__(self, parent=None):
        super().__init__(parent)

    def add_indexes(self, name: str, indexes: dict):
        str_list = list(indexes.keys())
        w = CustomListWidget(str_list)
        self.addItem(w, name)


class CustomListWidget(QListView):
    def __init__(self, list, parent=None):
        super().__init__(parent)
        self.model = QStringListModel(list)
        self.setModel(self.model)
        self.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.setDragEnabled(True)
