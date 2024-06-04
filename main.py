from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("uShell")
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        monitor_width = QGuiApplication.primaryScreen().geometry().width()
        monitor_height = QGuiApplication.primaryScreen().geometry().height()
        self.setFixedSize(monitor_width, monitor_height * 0.025)
        self.move(0, monitor_height - self.height())

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.start = QPushButton("Start")
        # set keyboard shortcut
        self.start.setShortcut("Ctrl+Esc")
        self.layout.addWidget(self.start)

        self.layout.addStretch()

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

# better rewrite this
