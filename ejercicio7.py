class Pila:

     def __init__(self):
         self.items = []

     def estaVacia(self):
         return self.items == []

     def incluir(self, item):

        self.items.append(item)
         

     def extraer(self):
         return self.items.pop()
         
     def inspeccionar(self):
         
         salida = self.items
                 
         return salida

     def tamano(self):
         return len(self.items)


class Pilas:

    def __init__(self, tam):
        self.pilas = []
        self.pilas.append(Pila())

        self.tamanio = tam
        
        
    def ingresar(self, item):


        #self.pilas[len(self.pilas)-1].incluir(item)

        if self.pilas[len(self.pilas)-1].tamano()==self.tamanio:

            self.pilas.append(Pila())
            self.pilas[len(self.pilas)-1].incluir(item)
            
        else:
            self.pilas[len(self.pilas)-1].incluir(item)


    def eliminar(self):

        if self.pilas[len(self.pilas)-1].tamano()==0:
            self.pilas.pop()
            self.pilas[len(self.pilas)-1].extraer()
        else: 
            self.pilas[len(self.pilas)-1].extraer()

        #self.pilas[len(self.pilas)-1].extraer()

       
    def mostrar(self):
        #total = ""

        for incre in self.pilas:
            print(incre.inspeccionar())
        #return total
        #self.pilas[len(self.pilas)-1].inspeccionar()

   

print("programa pilas")


#print("pila unica mostrada ejemplo aplicacion")
#pila2 = Pila()
#pila2.incluir(12)
#pila2.incluir(9)
#pila2.incluir(7)

#print(pila2.inspeccionar())

#pila2.extraer()

#rint(pila2.inspeccionar())

#print("instanciacion de la clase pilas que acululara las pilas de datos ")
#entrada = input("ingrese el tamaño que necesita pra cada pila de datos")

print( "se crea la lista de pilas")

pila1 = Pilas(3)

print("ingresamos los datos  en las pilas")
pila1.ingresar(12)
pila1.ingresar(2)
pila1.ingresar(10)
pila1.ingresar(6)
pila1.ingresar(3)
pila1.ingresar(4)
pila1.ingresar(1)
pila1.ingresar(18)
pila1.ingresar(7)


pila1.mostrar()

pila1.eliminar()
pila1.eliminar()
pila1.eliminar()

print("despues de eliminar 3 elementos")
pila1.mostrar()
