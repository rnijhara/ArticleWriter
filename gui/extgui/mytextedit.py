from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QTextEdit
from PyQt4.QtCore import QEvent, SIGNAL


class MyTextEdit(QTextEdit):
    def __init__(self, *args):
        QTextEdit.__init__(self, *args)

    def event(self, event):
        if (event.type() == QEvent.KeyPress) and (int(event.modifiers() == QtCore.Qt.ControlModifier)):
            if event.key() == QtCore.Qt.Key_Space:
                self.emit(SIGNAL("ctrlSpacePressed"))
                return True
        return QTextEdit.event(self, event)
