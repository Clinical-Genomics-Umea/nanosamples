from PySide6.QtCore import Qt, QAbstractTableModel


class TableModel(QAbstractTableModel):
    def __init__(self):
        super(TableModel, self).__init__()

        self.headers = ["Scientist name", "Birthdate", "Contribution"]
        self.data = [["Newton", "1643-01-04", "Classical mechanics"],
                     ["Einstein", "1879-03-14", "Relativity"],
                     ["Darwin", "1809-02-12", "Evolution"]]

    def rowCount(self, parent=None):
        # How many rows are there?
        return len(self.data)

    def columnCount(self, parent=None):
        # How many columns?
        return len(self.headers)

    def data(self, index, role):
        if role != Qt.DisplayRole:
            return ""
        # What's the value of the cell at the given index?
        return self.rows[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return ""
        # What's the header for the given column?
        return self.headers[section]

    def setData(self, index, value, role) -> bool:
        row = index.row()
        column = index.column()
        self.data[row][column] = value
        self.dataChanged.emit(index, index)

        return True

