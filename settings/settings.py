import sys
import json

from PyQt6.QtCore import Qt,QVariant
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QPushButton 
)


# Подкласс QMainWindow для настройки основного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()

        self.filename = ""

        self.application_type = QComboBox()
        self.application_type.addItem("Zoom",QVariant("Zoom"))
        self.application_type.addItem("Teams",QVariant("Teams"))
        
        self.programm_filedialog = QFileDialog()
        self.programm_filedialog.fileSelected.connect(self.programm_filedialog_fileselected)

        button_open_filedialog = QPushButton ("Select path to programm")
        button_open_filedialog.clicked.connect(self.button_open_filedialog_clicked)

        button_write_file = QPushButton ("Save")
        button_write_file.clicked.connect(self.button_write_file_clicked)

        layout.addWidget(self.application_type)
        layout.addWidget(button_open_filedialog)
        layout.addWidget(button_write_file)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def button_open_filedialog_clicked(self):
        self.programm_filedialog.exec()

    def button_write_file_clicked(self):
        data = {
            "programm": self.application_type.currentText(),
            "path": self.filename,
            "join_cord_x": 0,
            "join_cord_y": 0,
            "first_launch": True,
            "videocheckbox_cord_x": 0,
            "videocheckbox_cord_y": 0,
            "connect_cord_x": 0,
            "connect_cord_y": 0,
            "connectfinal_cord_x": 0,
            "connectfinal_cord_y": 0,
        }
        with open('settings.json', 'w') as f:
            json.dump(data, f)
        print(data)

    def programm_filedialog_fileselected(self,filename):
        self.filename = filename

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()