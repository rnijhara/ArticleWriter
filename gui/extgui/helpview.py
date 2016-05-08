from PyQt4 import QtGui
from PyQt4.QtGui import QTextEdit


class HelpViewer(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.initUI()

    def initUI(self):
        self.help = QTextEdit(self)
        self.help.setReadOnly(True)
        layout = QtGui.QGridLayout()
        layout.addWidget(self.help, 0, 0)
        help_file = open("C:\\Users\\Rex\\PycharmProjects\\ArticleWriter\\gui\\help.writer")
        self.help.textCursor().insertHtml(help_file.read())
        self.help.moveCursor(QtGui.QTextCursor.Start)
        self.setWindowTitle("Help")
        self.setGeometry(120, 120, 1030, 600)
        self.setLayout(layout)
