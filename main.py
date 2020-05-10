import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QVBoxLayout, QPushButton
from gui.ui_mainwindow import Ui_MainWindow


from PySide2.QtCore import Qt, QAbstractTableModel, QModelIndex, Slot
from PySide2.QtGui import QColor, QBrush

class MyItem(QTableWidgetItem):

    myre = None

    def __init__(self, d):
        self.myre = d
        super().__init__(str(d))



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    window.ui.table_constructor.setColumnCount(3)
    window.ui.table_constructor.setHorizontalHeaderLabels(('recv', 'action', 'send'))

    window.ui.table_constructor.insertRow(window.ui.table_constructor.rowCount())

    i = MyItem({'a': 1, 'b': 2})
    i.setBackgroundColor(QColor('red'))
    window.ui.table_constructor.setItem(0, 0, i)
    window.ui.table_constructor.setItem(0, 1, MyItem({'v': 10, 'f': 1}))
    window.ui.table_constructor.setItem(0, 2, MyItem({'a': 1, 'b': 2}))


    def cell_was_clicked(row, column):
        print("Row %d and Column %d was clicked" % (row, column))
        # item = window.ui.table_constructor.item(row, column)
        item = window.ui.table_constructor.currentItem()
        print(type(item))
        if item is None:
            return
        window.ui.label_data.setText(item.text())

    @Slot()
    def butclic(*args):
        print(args)
        pos = window.ui.table_constructor.rowCount()
        print(pos)
        window.ui.table_constructor.insertRow(pos)

        item = MyItem({'tol': 'r', 'mol': 2})
        item.setBackgroundColor(QColor('red'))
        if 'pushButton' in args:
            window.ui.table_constructor.setItem(pos, 1, item)
        else:
            window.ui.table_constructor.setItem(pos, 0, item)

    window.ui.table_constructor.cellClicked.connect(cell_was_clicked)
    window.ui.pushButton.clicked.connect(butclic)
    window.ui.button_1.clicked.connect(lambda: butclic(window.ui.pushButton.objectName()))
    ly = QVBoxLayout()
    ly.addWidget(QPushButton('clikme'))


    window.show()

    sys.exit(app.exec_())

