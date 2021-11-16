class Node:

  def __init__(self, priority, info):
    self.info = info
    self.priority = priority

class PriorityQueue:

  def __init__(self):
    self.queue = list()


  def insertar(self, node):
    if self.tamanio() == 0:
      self.queue.append(node)
    else:
      for x in range(0, self.tamanio()):
        if node.priority >= self.queue[x].priority:
          if x == (self.tamanio()-1):
            self.queue.insert(x+1, node)
          else:
            continue
        else:
          self.queue.insert(x, node)
          return True

  def borrar(self):
    return self.queue.pop(0)

  def mostrar(self):
    for x in self.queue:
      print( str(x.info)+" - "+str(x.priority))

  def tamanio(self):
    return len(self.queue)
    

cola1 = PriorityQueue()


cola1.insertar(Node(10,"Damian"))
cola1.insertar(Node(5,"Alejandro"))
cola1.insertar(Node(1,"Jorge"))
cola1.insertar(Node(3,"Daniela"))
cola1.insertar(Node(12,"Arturo"))
cola1.insertar(Node(8,"Carlos"))


cola1.mostrar()



