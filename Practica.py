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
	 
   	 if self.vacia() == True:
   	 	self.inicio = self.ultimo = Nodo(dato)
   
   	 else:
   	 	aux = self.ultimo 

   	 	self.ultimo = aux.siguiente = Nodo(dato)
   	 


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

	def __init__(self, entrada, entradainicial, entradafinal, orden):	
		self.entrada = entrada
		self.adelante = None
		self.atras = None
		self.arriba = None
		self.abajo = None
		self.siguiente = None
		self.anterior = None
		self.entradainicial = entradainicial
		self.entradafinal = entradafinal
		self.orden = orden


	

class Matriz:

	def __init__(self):

		self.iniciofila = None #@correo
		self.ultimofila = None #@correo
		self.iniciocolumna = None #letra
		self.ultimocolumna = None #letra

	def MatrizVacia(self):
		return self.iniciofila == None


	def ingresarMatriz(self, direccion, fila, columna, orden1):
		s = ""
		if self.MatrizVacia() == True:
			nue = MatrizNodo(direccion, None, None , orden1)
			self.iniciofila = self.ultimofila = MatrizNodo(fila, None ,None, None)
			self.iniciocolumna = self.ultimocolumna = MatrizNodo(columna, None, None, orden1)
			self.iniciofila.entradainicial = self.iniciofila.entradafinal = self.ultimofila.entradainicial = self.ultimofila.entradafinal = self.iniciocolumna.entradainicial = self.iniciocolumna.entradafinal= self.ultimocolumna.entradainicial = self.ultimocolumna.entradafinal = nue
  			self.iniciofila.abajo = self.ultimofila.abajo = self.iniciocolumna.siguiente = self.ultimocolumna.siguiente = nue
  			self.iniciofila.entradainicial.arriba = self.iniciofila.entradafinal.arriba = self.ultimofila.entradainicial.arriba = self.ultimofila.entradafinal.arriba = self.iniciofila
  			self.iniciocolumna.entradainicial.anterior = self.iniciocolumna.entradafinal.anterior = self.ultimocolumna.entradainicial.anterior = self.ultimocolumna.entradafinal.anterior = self.iniciocolumna
  			self.iniciofila.siguiente = self.ultimofila.siguiente = None
  			self.iniciocolumna.abajo = self.ultimocolumna.abajo = None
  			return "Dato:" +nue.entrada + "Ar:" +nue.arriba.entrada + "An:" +nue.anterior.entrada
  		
  		else:
  			nuevaCabecera = MatrizNodo(fila, None, None, None)
  			temp = self.iniciofila
  			Creado = False
  			while temp != None:
  				if nuevaCabecera == temp.entrada:
  					Creado = True
  				temp = temp.siguiente

  			if Creado == True:
  				Creado = True
  			else:
  				nuevaCabecera.anterior = self.ultimofila
  				self.ultimofila.siguiente = nuevaCabecera
  				self.ultimofila = nuevaCabecera
  				s = "Dominio Creado"

  			nuevaCabeceraL = MatrizNodo(columna, None, None, orden1)
  			templ = self.iniciocolumna
  			CreadoL = False
  			while templ != None:
  				if int(templ.orden) == int(templ.orden):
  					CreadoL = True
  				templ = templ.abajo
  			if CreadoL == True:
  				s = s + "Letra encontrada"
  			else:
  				if int(orden1)< int(self.iniciocolumna.orden):
  					tempm = self.iniciocolumna
  					self.iniciocolumna = CreadoL
  					self.iniciocolumna.abajo = tempm
  					tempm.arriba = self.iniciocolumna
  					s = s + "\n Se agrego Letra al inicio"

  				elif int(orden1) > int(self.ultimocolumna.orden):
  					CreadoL.arriba = self.ultimocolumna
  					self.ultimocolumna.abajo = CreadoL
  					self.ultimocolumna = CreadoL
  					s = s + "\n Se agrego al final"
  				else:
  					tempm1 = self.iniciocolumna
  					while tempm1 != None:
  						if int(orden1)<int(tempm1.orden):
  							CreadoL.arriba = tempm1.arriba
  							tempm1.arriba.abajo = CreadoL
  							CreadoL.abajo = tempm1
  							tempm1.arriba = CreadoL
  							CreadoLetra = True
  							s = s + "\n Letra agregada"
  							break
  						tempm1 = tempm1.abajo

  					if CreadoLetra ==True:
  						s = s + "\n Se agrego antes la letra"
  					else: 
  						tempm2 = self.ultimocolumna
  						while tempm2 != None:
  							if int(orden1) > int(tempm2.orden):
  								CreadoL.arriba = tempm2.arriba
  								tempm2.arriba.abajo = CreadoL
  								CreadoL.abajo = tempm2
  								tempm2.arriba = CreadoL
  								CreadoLetra = True
  								s = s + "\nLetra Agregada"
  								break
  							tempm2 = tempm2.abajo
       		nuevoIngreso = MatrizNodo(columna, None, None, orden1)

       		te = self.iniciocolumna
       		while te != None:
       			if str(te.entrada)== str(columna):
       				tef = self.iniciofila
       				while tef != None:
       					if str(tef.entrada) == str(fila):
       						if te.entradainicial == None:
       							if tef.entradainicial.entradainicial == None:
       								te.entradainicial = te.entradafinal = tef.entradainicial = tef.entradafinal = nuevoIngreso
       								te.siguiente = tef.abajo = nuevoIngreso
       								nuevoIngreso.arriba = tef
       								nuevoIngreso.anterior = te
            						#
            						s = "Ingresado:" + str(nuevoIngreso.entrada) + "Dominio:" + nuevoIngreso.arriba.entrada + "Letra:" + nuevoIngreso.anterior.entrada
            				else:
            					if int(orden1) < int(tef.entradainicial.orden):
            						te.entradainicial = te.entradafinal = nuevoIngreso
            						te.siguiente = nuevoIngreso
            						nuevoIngreso.anterior = te
            						tef.abajo = nuevoIngreso
            						tef.entradainicial.arriba= nuevoIngreso
            						nuevoIngreso.abajo = tef.entradainicial
            						nuevoIngreso.arriba = tef
            						tef.entradainicial = nuevoIngreso
            						s = "Ingresado:" +str(nuevoIngreso.entrada) + "Arriba" + nuevoIngreso.arriba.entrada + "Letra" + nuevoIngreso.anterior.entrada
            					elif int(orden1) > int(tef.entradafinal.orden):
            						te.entradainicial = te.entradafinal = nuevoIngreso
            						te.siguiente = nuevoIngreso
            						nuevoIngreso.anterior = te
            						nuevoIngreso.arriba = tef.entradafinal
            						tef.entradafinal.abajo = nuevoIngreso
            						tef.entradafinal = nuevoIngreso
            						s = "Ingresado:" + str(nuevoIngreso.entrada) + "Arriba:"+nuevoIngreso.arriba.entrada + "Letra:" + nuevoIngreso.anterior.entrada
            					else:
            						nte = tef.entradainicial
            						while nte != None:

            							if int(orden1) < int(nte.orden):
            								te.entradainicial = te.entradafinal = nuevoIngreso
            								te.siguiente = nuevoIngreso
            								nuevoIngreso.anterior = te
            								nte.arriba.abajo = nuevoIngreso
            								nuevoIngreso.arriba = nte.arriba
            								nuevoIngreso.abajo = nte
            								nte.arriba = nuevoIngreso
            								s = "Ingresado:" +str(nuevoIngreso.entrada) + "Arriba:" +nuevoIngreso.arriba.entrada + "Letra:"+nuevoIngreso.anterior.entrada
            							nte = nte.abajo
            			else:
            				if tef.entradainicial == None:
            					te.entradafinal.siguiente = tef.entradainicial = tef.entradafinal = nuevoIngreso
            					nuevoIngreso.anterior = te.entradafinal
            					te.entradafinal = nuevoIngreso
            					nuevoIngreso.arriba = tef

            				else:
            					ing = False
            					tempm3 = tef.entradainicial
            					while tempm3 != None:
            						if str(tempm3.orden) == str(orend1):
            							if tem.entradainicial == None:
            								tempm3.entradainicial == tempm3.entradafinal == nuevoIngreso
            								tempm3.atras = nuevoIngreso
            								nuevoIngreso.adelante= tempm3
            								ing = True
            							else:
            								tempm3.entradafinal.atras = nuevoIngreso
            								nuevoIngreso.adelante = tempm3.entradafinal
            								tempm3.entradafinal = nuevoIngreso
            								ing = True
            						tempm3 = tempm3.abajo
            					if ing == False:
            						if int(orden1) < int(tef.entradafinal.orden):
            							nuevoIngreso.arriba = tef
            							nuevoIngreso.abajo = tef.entradafinal
            							tef.abajo = nuevoIngreso
            							tef.entradafinal.arriba = nuevoIngreso
            							ing = True
            						elif int(orden1) > int(tef.entradafinal.orden):
            							tef.entradafinal.abajo = nuevoIngreso
            							nuevoIngreso.arriba = tef.entradafinal
            							tef.entradafinal = nuevoIngreso
            							ing = True
            						else:
            							p=tef.entradainicial
            							while p != None:
            								if int(orden1) < int(p.orden):
            									p.arriba.abajo = nuevoIngreso
            									nuevoIngreso.arriba = p.arriba 
            									nuevoIngreso.abajo = p
            									p.arriba = nuevoIngreso
            									ing = True 
            									break
           										
           									c = c.abajo
           							if tef == self.iniciofila:
           								sigm= False
           								j = tef.siguiente
           								while j != None:
           									y = j.entradainicial
           									while y !=None:
           										if str(y.orden) == str(orden1):
           											sigm = True
            										break
            									y = y.abajo
            								j = j.siguiente
            							if sigm == True:
            								busc = True
            								rec = tef.siguiente
            								while rec != None:
            									ss = rec.entradainicial
            									if busc == True:
            										while ss != None:
            											if str(s.orden) == str(orden1):
           													sigm = True
           													busc = False
           													if ss == te.entradainicial:
           														ss.anterior.siguiente = nuevoIngreso
           														nuevoIngreso.anterior = ss.anterior
           														nuevoIngreso.siguiente = ss
           														ss.anterior = nuevoIngreso
           														te.entradainicial = nuevoIngreso
           													else:
           														ss.anterior.siguiente = nuevoIngreso
           														nuevoIngreso.anterior = ss.anterior
           														nuevoIngreso.siguiente = ss
            													ss.anterior = nuevoIngreso

            												
            												
            											ss = ss.abajo
            									rec = rec.siguiente
            					elif tef == self.ultimofila:
            							sigm = False
            							j = tef.anterior
            							while j != None:
            								y = j.entradainicial
            								while y != None:
            									if str(y.orden) == str (orden1):
            										sigm = True
            										break
           										y = y.abajo
           									j = j.anterior
           								if sigm == True:
           									busc = True
           									r = tef.anterior
           									while r != None:
           										ss = r.entradainicial
           										if busc == True:
           											while ss != None:
           												if str(s.orden) == str(orden1):
           													sigm = True
            												busc = False
            												if ss == te.entradafinal:
            													ss.siguiente = nuevoIngreso
            													nuevoIngreso.anterior = ss
            													te.entradafinal = nuevoIngreso
            													s = "Ingresado" + nuevoIngreso.entrada+ "anterior" + nuevoIngreso.anterior.entrada + "siguiente: No tiene arriba" + nuevoIngreso.arriba.entrada
            												break
            											ss = s.abajo
            									rec = rec.anterior
            					else:
            						ena = False
            						ens = False

            						j = tef.anterior
            				 		while j != None:
            							y = j.entradainicial
            							while y != None:
            								if str(y.orden) == str(orden1):
            									ena = True
            							    	break
            							   	y = y.abajo

            							  
            							j = j.Anterior

            						pe = tef.anterior
            						while pe != None:
            							t = pe.entradainicial
            							while t != None:
            								if str(t.orden) == str(orden1):
            									ens = True
            							    	break
            							    	t = t.abajo
            							pe = pe.siguiente
            						busc2 = True
            						if ena == True:
            							j = tef.anterior
            							while j != None:
           								    if busc2 == True:
            								   	y = j.entradainicial
            								   	while y != None:
            								   		if str(y.orden) == str(orden1):
            								   			ena = True
            								   			busc2 = False
            							    			nuevoIngreso.anterior = y
            							    			nuevoIngreso.siguiente = y.siguiente
            							    			y.siguiente.anterior = nuevoIngreso
            							    			y.siguiente = nuevoIngreso
            							    			s = "Se ingreso:" +nuevoIngreso.entrada + "anterior" +nuevoIngreso.anterior.entrada
            							    			break
            							    		y = y.abajo
            							  	  	j = j.anterior
            						busc2 = True

            						if ens == True:
            							j = tef.siguiente
            							while j != None:
            								if busc2 == True:
            								   	y = j.entradainicial
            							    	while y != None:
            							    		if  str(y.orden) == str(orden1):
            							    			ens = True
            							    			busc2 = False
            							    			nuevoIngreso.anterior = y.anterior
            							    			y.anterior.siguiente = nuevoIngreso
            							    			y.anterior = nuevoIngreso
            							    			nuevoIngreso.siguiente = y
            							    			break
           								    		y = y.abajo
           								   		j = j.siguiente
            						else:
            							nuevoIngreso = None
            							s = s + "no tiene siguiente"

            			tef = tef.siguiente
    			te = te.abajo
		return s

	def GraficaMatriz(self):
		dot = Digraph(comment = 'GraficaMatriz')
		dot

		aux= self.iniciofila
		aux1 = self.iniciocolumna

		if aux == None:
			return "Matriz Vacia"

		else:
			while aux.siguiente !=None:
				dot.Node(aux.entrada)
				dot.Node(aux.siguiente.entrada)
				dot.edge(str(aux.entrada), str(aux.siguiente.entrada))
				aux = aux.siguiente
			auxn = self.ultimofila
			while auxn.anterior != None:
				dot.Node(aux.entrada)
				dot.Node(auxn.anterior.entrada)
				dot.edge(str(auxn.entrada),str(auxn.anterior.entrada))
				auxn = auxn.anterior
			dot.render('test-output/Matriz.dot', view=False)


	













  	

			
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
	orden1temp = str(request.form["orden1"])
	matriz.GraficaMatriz()
	
	return matriz.ingresarMatriz(entradatemp, filatemp, columnatemp, orden1temp)

	
	 


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')














        	


  


