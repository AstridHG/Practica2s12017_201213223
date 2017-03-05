from flask import Flask, request, Response
import subprocess
from graphviz import Digraph
app = Flask("Ejemplo")

class Nodo:
	def __init__(self, dato):
		self.dato = dato
		self.siguiente = None
		self.anterior = None
	
	
class ListaSimple:
	def __init__(self):
		self.inicio = None
		self.ultimo = None

	def vacia(self):
		return self.inicio == None
	

	def agregar(self, dato):
	 c = 0
   	 if self.vacia() == True:
   	 	self.inicio = self.ultimo = Nodo(dato)
   
   	 else:
   	 	aux = self.ultimo 

   	 	self.ultimo = aux.siguiente = Nodo(dato)
   	 c = c + 1


   	def recorrer(self):
   	 	aux= self.inicio
   	 	while aux != None:
   	 		print(aux.dato)
   	 		aux = aux.siguiente

   	def eliminar(self, pos):
   		if self.vacia() == True:
   			return"Lista Vacia"
   			print "Lista Vacia"
   		else:
   			if int(pos) == 0:
   				tem = self.inicio.siguiente
   				self.inicio = None
   				self.inicio = tem
   				return "Eliminado"
   				print "Eliminado"
   			else:
   				tem1 = self.inicio
   				con = 0
   				while tem1 != None:
   					con = con + 1
   					tem1 = tem1.siguiente
   				if con < int(pos):
   					return "Fuera de rango"
   					print "Fuera de rango"
   				else:
   					tem2 = self.inicio
   					con1 = 0
   					while tem2 != None:
   						con1 = con1 + 1
   						tem2 = tem2.siguiente
   					if con1 == int(pos):
   						self.ultimo = None
   						return "Eliminado"
   						print "Eliminado"
   					else:
   						temp1 = self.inicio
   						contador1 = 0
   						while temp1 != None:
   							if contador1 == int(pos)-1:
   								tem3 = temp1.siguiente
   								tem4 = tem3.siguiente
   								tem3 = None
   								temp1.siguiente = tem4
   							temp1 = temp1.siguiente
   							contador1 = contador1 + 1
   						return "eliminado"
   						print "Eliminado"

   	def busqueda(self, dato):
   		bus = self.inicio
   		
   		
   		cont = 0
   		bandera = False

   		while bus != None:
   			if bus.dato == str(dato):
   				bandera = True
   				break
   			else:
   				cont = cont + 1
   				bandera = False
   			bus = bus.siguiente
   		if bandera == False:
   			return "No hay dato"
   			print "No hay dato"
   		else: 
   			return "hay elemento" + str(cont)
   			print " hay elemento "
   			


   	def GraficaLista(self):
   		dot = Digraph(comment = 'GraficaLista')
   		dot
   		
   		aux = self.inicio
   		c = 0
   		if aux== None:
   			print "lista vacia"
   		
   	 	else:
   	 		while aux.siguiente != None:
   	 			dot.node(aux.dato)
   	 
   	 			dot.node(aux.siguiente.dato)
   	 		
   	 			dot.edge(str(aux.dato),str(aux.siguiente.dato))
   	 			aux = aux.siguiente
   	 	
   	 		dot.render('test-output/ListaSimple.dot', view=False)
   		
#------------------------------------------------------------------------------------------------------------------------------------------------- 
class Cola:
	def __init__(self):
		self.inicio = None
		self.ultimo = None

	def vacia(self):
		return self.inicio == None	

	def ingresarCola(self, dato):
		nuevo = Nodo(dato)
		nuevo.dato=dato
		nuevo.siguiente=None

	        if self.vacia() == True:
	        	self.inicio = nuevo
		        self.ultimo = nuevo
	        else:
		        self.ultimo.siguiente = nuevo
		        self.ultimo = nuevo

	def recorrer(self):
		nuevo78 = self.inicio
		if self.vacia() == True:
			print "cola vacia"
		else:
			while nuevo78 != None:
				print(nuevo78.dato)
				nuevo78 = nuevo78.siguiente

	 

	def sacarCola(self):

		if self.vacia() != True:
			dato = self.inicio.dato
		if self.vacia()==True:
			self.inicio = None
			self.ultimo = None
		else:
			self.inicio = self.inicio.siguiente

			return dato

	
	def GraficarCola(self):
   		dot = Digraph(comment = 'GraficaColas')
   		dot
   		
   		aux = self.inicio
   		 
   		if aux== None:
   			print "Cola vacia"
   		
   	 	else:
   	 		while aux.siguiente != None:
   	 			dot.node(str(aux.dato))
   	 			dot.node(str(aux.siguiente.dato))
   	 			dot.edge(str(aux.dato),str(aux.siguiente.dato))
   	 			aux = aux.siguiente
   	 		
   	 		dot.render('test-output/Cola.dot', view=False)
   		
#---------------------------------------------------------------------------------------------------------------------------------
class Pila:
	def __init__(self):
		self.inicio = None
		self.ultimo = None


	def vacia(self):
		return self.ultimo == None

	def ingresarPila(self, dato):
		

		if self.vacia() == True:
			self.inicio = self.ultimo = Nodo(dato)
		else:
			temporal = Nodo(dato)
			temporal.anterior = self.ultimo
			self.ultimo = temporal
			print "agregado"

		


	def sacarPila(self):

		if self.vacia() == True:
			print "La pila esta vacia"
		else:
			tm=self.ultimo
			q = self.ultimo.anterior
			self.ultimo = None
			self.ultimo = q
			print "elemento saliente" + str(tm.dato)


   	def GraficarPila(self):
   		dot = Digraph(comment = 'GraficaPila')
   		dot
   		
   		aux = self.ultimo
   		 
   		if aux== None:
   			print "Pila vacia"
   		
   	 	else:
   	 		while aux.anterior != None:
   	 			dot.node(str(aux.dato))
   	 			dot.node(str(aux.anterior.dato))
   	 			dot.edge(str(aux.dato),str(aux.anterior.dato))
   	 			aux = aux.anterior
   	 		
   	 		dot.render('test-output/Pila.dot', view=False)
		

class MatrizNodo:

	def __init__(self, entrada, entradainicial, entradafinal):	
		self.entrada = entrada
		self.adelante = None
		self.atras = None
		self.arriba = None
		self.abajo = None
		self.derecha = None
		self.izquierda = None
		self.entradainicial = entradainicial
		self.entradafinal = entradafinal


	

class Matriz:

	def __init__(self):

		self.iniciofila = None #@correo
		self.ultimofila = None #@correo
		self.iniciocolumna = None #letra
		self.ultimocolumna = None #letra

	def MatrizVacia(self):
		return self.iniciofila == None


	def ingresarMatriz(self, direccion, fila, columna):
		if self.MatrizVacia() == True:
			nue = MatrizNodo(direccion, None, None)
			self.iniciofila = self.ultimofila = MatrizNodo(fila, None ,None)
			self.iniciocolumna = self.ultimocolumna = MatrizNodo(columna, None, None)
			self.iniciofila.entradainicial = self.iniciofila.entradafinal = self.ultimofila.entradainicial = self.ultimofila.entradafinal = self.iniciocolumna.entradainicial = self.iniciocolumna.entradafinal= self.ultimocolumna.entradainicial = self.ultimocolumna.entradafinal = nue
  			self.iniciofila.abajo = self.ultimofila.abajo = self.iniciocolumna.siguiente = self.ultimocolumna.siguiente = nue
  			self.iniciofila.entradainicial.arriba = self.iniciofila.entradafinal.arriba = self.ultimofila.entradainicial.arriba = self.ultimofila.entradafinal.arriba = self.iniciofila
  			self.iniciocolumna.entradainicial.anterior = self.iniciocolumna.entradafinal.anterior = self.ultimocolumna.entradainicial.anterior = self.ultimocolumna.entradafinal.anterior = self.iniciocolumna
  			self.iniciofila.siguiente = self.ultimofila.siguiente = None
  			self.iniciocolumna.abajo = self.ultimocolumna.abajo = None
  			return "Ingresado:" +nue.entrada + "Arriba:" +nue.arriba.entrada + "Anterior:" +nue.anterior.entrada
  		else:
  			return "Matriz llena en su primera posicion"


  	def recorrerMatriz(self):
  		s = ""
  		nue1 = self.iniciofila
  		while nue1 != None:
  			s = s + "Dominio:" +nue1.entrada
  			nue1 = nue1.siguiente
  		nue1 = self.iniciocolumna
  		while nue2 != None:
  			s = s + "Letra:" + nue2.entrada
  			nue2 = nue2.abajo
  		return s    

			
lis = ListaSimple()
col = Cola()
pila = Pila()
matriz = Matriz()

@app.route('/insertarLista',methods=['POST']) 
def insertarLista():
	dato = str(request.form['dato'])
	
	lis.agregar(str(dato))
	lis.recorrer()
	lis.GraficaLista()

	return "se agrego a la lista:"+str(dato)
	print "se agrego a la Lista :"+str(dato)
	


@app.route('/eliminarLista',methods=['POST']) 
def eliminarLista():
	dato = int(request.form['dato'])
	print dato
	lis.eliminar(int(dato))
	lis.recorrer()
	lis.GraficaLista()
	return "Dato Eliminado Pos:"+str(dato)
	print "Dato Eliminado Pos:"+str(dato)
	

@app.route('/insertarCola',methods=['POST']) 
def insertarCola():
	dato = int(request.form['dato'])
	print dato
	col.ingresarCola(int(dato))
	col.GraficarCola()
	col.recorrer()
	return "Se agrego a Cola:"+ str(dato)

	print "se agrego a Cola :"+ str(dato)
	



@app.route('/insertarPila',methods=['POST']) 
def insertarPila():
	dato = int(request.form['dato'])
	print dato

	pila.ingresarPila(int(dato))
	pila.GraficarPila()
	return "se agrego a Pila:" +str(dato)
	print "se agrego a Pila :"+ str(dato)
	


@app.route('/saleCola',methods=['POST']) 
def saleCola():
	dato = col.sacarCola()
	col.GraficarCola()
	return "Dato que sale:"+ str(dato)

	

@app.route('/salePila',methods=['POST']) 
def salePila():
	dato = pila.sacarPila()
	pila.GraficarPila()

	return "Dato que sale:" +str(dato)
	



@app.route('/buscarLista',methods=['POST']) 
def buscarLista():
	dato = str(request.form['dato'])
	print dato
	lis.busqueda(str(dato))
	print "buscar :"+str(dato)
	
	return 'ok'

@app.route('/insertarMatriz',methods=['POST']) 
def insertarMatriz():
	entradatemp = str(request.form["entrada"])
	filatemp = str(request.form["fila"])
	columnatemp = str(request.form["columna"])
	return matriz.ingresarMatriz(entradatemp, filatemp, columnatemp)

	
	 


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')














        	


  


