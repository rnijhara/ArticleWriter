from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QListWidget
from PyQt4.QtCore import QEvent, SIGNAL


class MyListWidget(QListWidget):
    def __init__(self, *args):
        QListWidget.__init__(self, *args)

    def event(self, event):
        if (event.type() == QEvent.KeyPress) and (int(event.modifiers() == QtCore.Qt.ControlModifier)):
            if event.key() == QtCore.Qt.Key_E:
                self.emit(SIGNAL("ctrlEPressed"))
                return True
        return QListWidget.event(self, event)
