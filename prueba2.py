import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot



class App(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = 'UPCH'
        self.left = 70
        self.top = 100
        self.width = 750
        self.height = 450
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.boton = Action(self)
        self.show()

class Action(QWidget):

	def __init__(self,parent):
		super(QWidget, self).__init__(parent)
		self.layout = QVBoxLayout(self)

		self.button = QPushButton("Comenzar")
		self.button.setToolTip("Carga")
		self.button.move(100,70)
		self.button.clicked.connect(self.on_click)
		self.layout.addWidget(self.button)
		self.setLayout(self.layout)
	@pyqtSlot()
	def on_click(self):
		print("PyQt5Bton is pressed")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())