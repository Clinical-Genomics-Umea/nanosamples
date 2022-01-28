from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionButton, QStyle, QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QEvent, QSize


class IconCheckBoxDelegate(QStyledItemDelegate):
    """
    A delegate that places a fully functioning QCheckBox cell of the column to which it's applied.
    Since regular QStandardItem checkboxes do not accept styling, icons must be used.


    """
    def __init__(self, parent):
        super(IconCheckBoxDelegate, self).__init__(parent)
        self._icon = QIcon()
        self._icon.addFile(":/icons/AppIcons/check_box_24dp.png", QSize(), QIcon.Normal, QIcon.On)
        self._icon.addFile(":/icons/AppIcons/check_box_outline_blank_24dp.png", QSize(), QIcon.Normal, QIcon.Off)

    def createEditor(self, parent, option, index):
        """
        Important, otherwise an editor is created if the user clicks in this cell.
        """
        return None

    def paint(self, painter, option, index):
        """
        Paint a checkbox without the label.

        To create a checkable, transparent pushbutton CE_PushButtonLabel MUST be used.
        CE_PushButton creates a non-paintable, ugly button

        """
        value = index.model().data(index, Qt.EditRole)
        _button = QStyleOptionButton()

        _button.rect = option.rect
        _button.iconSize = QSize(20, 20)
        _button.icon = self._icon
        _button.features |= QStyleOptionButton.Flat
        if int(value) == 0:
            _button.state |= QStyle.State_Off
        else:
            _button.state |= QStyle.State_On

        QApplication.style().drawControl(QStyle.CE_PushButtonLabel, _button, painter)

    def editorEvent(self, event, model, option, index):
        '''
        Change the data in the model and the state of the checkbox
        if the user presses the left mousebutton and this cell is editable. Otherwise do nothing.
        '''
        if not int(index.flags() & Qt.ItemIsEditable) > 0:
            return False

        if event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
            # Change the checkbox-state
            self.setModelData(None, model, index)
            return True

        return False

    def setModelData(self, editor, model, index):
        '''
        The user wanted to change the old state in the opposite.
        '''

        print("set data")

        model.setData(index, 1 if int(index.data()) == 0 else 0, Qt.EditRole)
