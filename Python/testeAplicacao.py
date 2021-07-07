#hello.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, \
  QWidget, QPushButton, QTableWidget, QTableWidgetItem, QInputDialog

app = QApplication([])
window = QMainWindow()

screen = QWidget()
layout = QGridLayout()
screen.setLayout(layout)

label = QLabel()
label.setText('Hello world!')

window.setCentralWidget(widget)
window.show()
app.exec_()

layout.addWidget(label, 0, 0)

window.setCentralWidget(widget)
window.show()
app.exec_()

