from PySide6.QtCore import Qt, QSortFilterProxyModel, QModelIndex


class MultiSortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, *args, **kwargs):
        QSortFilterProxyModel.__init__(self, *args, **kwargs)
        self.multifilters = {}
        self.checkedfilter = False

    def setCheckedFilter(self):
        self.checkedfilter = True
        self.invalidateFilter()

    def clearCheckedFilter(self):
        self.checkedfilter = False
        self.invalidateFilter()

    def setFilterByColumns(self, columns, regex):
        for column in columns:
            self.multifilters[column] = regex
            self.invalidateFilter()

    def clearFilters(self):
        self.multifilters = {}
        self.invalidateFilter()

    def multifilterrow(self, source_row, source_parent):
        results = []
        for key, regex in self.multifilters.items():
            text = ''
            index = self.sourceModel().index(source_row, key, source_parent)
            if index.isValid():
                text = str(self.sourceModel().data(index, Qt.DisplayRole))
                if text is None:
                    text = ''

            if regex.match(text).hasMatch():
                results.append(True)
            else:
                results.append(False)

        return any(results)

    def checkedfilterrow(self, source_row, source_parent):
        index = self.sourceModel().index(source_row, 0, source_parent)
        if index.isValid():
            text = str(self.sourceModel().data(index, Qt.DisplayRole))
            if text is None:
                text = "0"

            if text == "1":
                return True

        return False

    def filterAcceptsRow(self, source_row, source_parent):
        mres = True
        if self.multifilters:
            mres = self.multifilterrow(source_row, source_parent)

        cres = True
        if self.checkedfilter:
            cres = self.checkedfilterrow(source_row, source_parent)

        if mres and cres:
            return True
        else:
            return False

    def dropMarkedRows(self):
        indexes = []
        for row in range(self.rowCount()):
            index = self.index(row, 0)
            if self.data(index, role=Qt.DisplayRole) == "1":
                indexes.append(index)

        for index in reversed(sorted(indexes)):
            self.removeRow(index.row())


class MarkedFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, *args, **kwargs):
        QSortFilterProxyModel.__init__(self, *args, **kwargs)
        self.filter = False

    def setFilter(self):
        self.filter = True
        self.invalidateFilter()

    def clearFilter(self):
        self.filter = False
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        index = self.sourceModel().index(source_row, 0, source_parent)
        value = self.sourceModel().data(index, Qt.DisplayRole)

        if self.filter and value == 1:
            return True

        elif not self.filter:
            return True

        return False


class ActiveFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, *args, **kwargs):
        QSortFilterProxyModel.__init__(self, *args, **kwargs)
        self.setFilterFixedString("False")
        self.setFilterKeyColumn(1)

    def invalidate_sort(self):
        self.invalidate()
        # self.setFilterFixedString("False")
        # self.setFilterKeyColumn(0)

    def lessThan(self, left: QModelIndex, right: QModelIndex):
        """
        Reimplemented to ensure that

        :param left: index left
        :param right: index right
        :return: True or False
        """

        left_row = left.row()
        right_row = right.row()
        model = left.model()

        prime_left = model.index(left_row, 0)
        prime_right = model.index(right_row, 0)

        left_value = prime_left.data()
        right_value = prime_right.data()

        if left_value != "100" or right_value != "100":
            return

        if left.data() < right.data():
            return True

        return False


class InActiveFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, *args, **kwargs):
        QSortFilterProxyModel.__init__(self, *args, **kwargs)
        self.setFilterFixedString("True")
        self.setFilterKeyColumn(1)
