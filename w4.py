
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QWidget, QPushButton, QHBoxLayout

class MyTable(QTableWidget):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        self.init_ui()
        
    def init_ui(self):
        # Set the column count of the table
        self.setColumnCount(2)
        # Set the row count of the table
        self.setRowCount(2)

        # Create a QPushButton widget and set its text and size policy
        button = QPushButton("Click Me")
        # button.setSizePolicy(QPushButton.SizePolicy.Minimum, QPushButton.SizePolicy.Fixed)
        
        # Create a QWidget widget and set its layout to a QHBoxLayout
        widget = QWidget()
        layout = QHBoxLayout(widget)
        
        # Add the QPushButton widget to the QHBoxLayout
        layout.addWidget(button)
        # Set the spacing and margin of the QHBoxLayout
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Set the cell widget of the table to the QWidget
        self.setCellWidget(0, 1, widget)
        
if __name__ == '__main__':
    app = QApplication([])
    table = MyTable(2, 2)
    table.show()
    app.exec_()

