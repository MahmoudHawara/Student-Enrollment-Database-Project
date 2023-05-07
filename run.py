
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # load the UI from the generated Python script
        from courseEdition import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ################################################################################
        ###### to get The New Size and change the second header ########################
        ################################################################################
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_timer)
        self.timer.start(100)
        # Store the last known size of the window
        self.last_size = self.size()

    def on_timer(self):
        # This function is called every 100ms by the timer
        if self.width() != self.last_size.width():
            inc = 0.5 * (self.width() - self.last_size.width())
            self.ui.logo_2.setMinimumWidth(self.ui.logo_2.minimumWidth() + int(inc))
            self.last_size = self.size()
        ################################################################################

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())