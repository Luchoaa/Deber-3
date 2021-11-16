class node:
    def __init__(self, data = None, next = None):

        
        
        self.data = data
        self.next = next


class Lista_enlazada: 
    def __init__(self):
        self.head = None
    
    def agregar_al_inicio(self, data):
        
        self.head = node(data=data, next=self.head)  

    def esta_vacio(self):
        return self.head == None

    def agregar_al_final(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)
    
   
    def borrar_nodo(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    
    def devolver_ultimo_nodo(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data

    
    def imprimir_lista( self ):
        node = self.head
        while node != None:
            print(node.data, end =" -> ")
            node = node.next
        print("\n")
        

        


listaA = Lista_enlazada()
listaB = Lista_enlazada()
listaC = Lista_enlazada()

a= input('ingrese el primer valor: ')
b= input('ingrese el sergundo valor: ')

val1= int(a)
val2= int(b)


_listaA = list(a)
_listaB = list(b)


for i in _listaA:
    listaA.agregar_al_final(i)
    




for j in _listaB:
    listaB.agregar_al_final(j)



    

c = val1 -val2
valC= str(c)
_listaC = list(valC)



for k in _listaC:
    listaC.agregar_al_final(k)

    

listaA.imprimir_lista()
listaB.imprimir_lista()
listaC.imprimir_lista()

