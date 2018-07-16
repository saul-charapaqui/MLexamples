#ejemplo con VBoxLayout
#contenedor de Widgets hip alterna: que no abarque toda la pantalla y tener espacio para colocar mas cosas
import sys
from PyQt5 import QtGui, QtWidgets

class Window(QtWidgets.QWidget):#cada vez que se coloca self. es QWidget.
	def __init__(self):	
		QtWidgets.QWidget.__init__(self) 

		self.setWindowTitle("UPCH - GUI")
		left = 50 #left y top no dependen de los otros o moves de otros widgets
		top = 50
		width = 1100
		height = 550
		self.setGeometry(left, top, width, height)

		#print(help(QLabel))
		l1 = QtWidgets.QLabel(self)#se coloca el self para conectar con la ventana
		l1.setText("GUI")
		l1.move(550,0)# cuando se maximiza se desordena todo

		self.l2 = QtWidgets.QLabel(self)# se coloca self para que aparezca en la ventana creada con App QApplication
		self.l2.setPixmap(QtGui.QPixmap("peru.jpg"))
		self.l2.move(100,50)	

		b1 = QtWidgets.QPushButton("Inicio", self)
		b1.clicked.connect(self.cargar)
		b1.move(0,50)
		
		b2 = QtWidgets.QPushButton("B/N",self)
		b2.move(0,100)

		self.prueba()

	def cargar(self):
		print("cargar")

	def prueba(self):
		l3 = QtWidgets.QLabel()
		l3.setText("")
		print("hola")
		

app = QtWidgets.QApplication(sys.argv)#se crea la ventana
ex = Window()
ex.show()
sys.exit(app.exec())