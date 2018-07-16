import sys
from PyQt5 import QtWidgets
from time import sleep

class master(QtWidgets.QWidget):#QtWidgets --> QPushButton, QWidget no se que es
	def __init__(self):
		super().__init__()
		self.setWindowTitle("UPCH")
		
		self.initUI()

	def initUI(self):
		b1 = QtWidgets.QPushButton("Carga",self)
		b1.move(100,0)
		b1.clicked.connect(self.pressedb1)

		self.l1 = QtWidgets.QLabel(self)
		self.l1.setText("      "*5)
		self.l1.move(10,10)

		self.a = 0

		self.show()

	def pressedb1(self):
		#self.l1.setText("ahora si salió")
		self.a+=1
		if self.a%2==0:
			self.l1.setText("par")
		else:
			self.l1.setText("impar")
		print("se presiono")






w = QtWidgets.QApplication(sys.argv)
App = master()
sys.exit(w.exec())
