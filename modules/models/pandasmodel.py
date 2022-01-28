from PySide6 import QtCore
from PySide6.QtCore import Qt, QAbstractTableModel
from PySide6.QtGui import QStandardItemModel
import pandas as pd


class PandasModel(QAbstractTableModel):
    def __init__(self, data: pd.DataFrame, colprops: dict, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = data
        self._col_props = colprops
        self._col_names = list(self._data.columns)

        self.proxy = None

    def set_proxy_model(self, proxy):
        self.proxy = proxy

    def isempty(self, row):
        totlen = 0
        for item in row:
            totlen += len(item)
        if totlen == 0:
            return False
        else:
            return True

    def set_field_value(self, field, value):

        col = self._col_names.index(field)
        no_rows = self.rowCount()

        for i in range(no_rows):
            index = self.index(i, col)
            self.setData(index, value, Qt.EditRole)

    def update_view(self):
        self.beginResetModel()

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
            if role == Qt.EditRole:
                return str(self._data.iloc[index.row(), index.column()])

        return None

    def setData(self, index, value, role) -> bool:

        if not index.isValid():
            return False
        row = index.row()
        if row < 0 or row >= len(self._data.values):
            return False
        column = index.column()
        if column < 0 or column >= self._data.columns.size:
            return False

        self._data.iat[row, column] = value

        self.dataChanged.emit(index, index)

        return True

    def emit_changed(self):
        i1 = self.index(0, 0)
        i2 = self.index(self.rowCount() - 1, 0)
        self.dataChanged.emit(i1, i2)

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[section]
        if orientation == Qt.Horizontal and role == Qt.ToolTipRole:
            col_name = self._data.columns[section]
            # if 'tooltip' in self._fields_dict['model_fields'][col_name]:
            #     return self._fields_dict['model_fields'][col_name]['tooltip']

        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return section+1
        return None

    def flags(self, mi):
        """Reimplemented to set editable and movable status."""

        col_name = self._col_names[mi.column()]

        flags = (
                Qt.ItemIsSelectable
                | Qt.ItemIsEnabled
                | Qt.ItemIsDropEnabled
            )

        if self._col_props[col_name]['edit']:
            flags |= Qt.ItemIsEditable

        if self._col_props[col_name]['checkable']:
            flags |= Qt.ItemIsUserCheckable

        return flags

    def dropMimeData(self, mimedata, action, row, column, parent):

        data = self.decode_mimedata(mimedata)

        if len(data) == 1:
            self.setData(self.setData(parent, data[0], Qt.EditRole))
            return True

        p_index = self.proxy.mapFromSource(parent)

        p_start_row = p_index.row()
        p_column = p_index.column()

        for i in range(len(data)):

            _index = self.proxy.index(i + p_start_row, p_column)
            t_index = self.proxy.mapToSource(_index)

            self.setData(t_index, data[i], Qt.EditRole)

        return True

    def decode_mimedata(self, mimedata):
        _model = QStandardItemModel()
        _model.dropMimeData(mimedata, QtCore.Qt.CopyAction, 0, 0, QtCore.QModelIndex())
        rowcount = _model.rowCount()
        data = []

        for row in range(rowcount):
            item = _model.item(row, 0)
            data.append(item.text())

        return data

    # def removeRows(self, position, rows, parent=QtCore.QModelIndex()):
    #     labels = list(self._data.index.values)
    #
    #     self.beginRemoveRows(parent, position, position+rows-1)
    #     for r in range(position, position + rows):
    #         print(r, labels[r])
    #         self._data.drop(labels[r], inplace=True)
    #     self.endRemoveRows()
    #
    #     return True
    #
    # def dropMarkedRows(self):
    #     indexes = []
    #     for row in range(self.rowCount()):
    #         index = self.index(row, 0)
    #         if self.data(index, role=Qt.DisplayRole) == "1":
    #             indexes.append(index)
    #
    #     for index in reversed(sorted(indexes)):
    #         self.removeRows(index.row(), 1)
