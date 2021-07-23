class Node:
    """
    Un objeto para almacenar un solo nodo de una linked list.
    Modela dos atributos - el dato almacenado y el vínculo al siguiente nodo en la lista.
    """

    data = None # Para manterner los datos que se almacenan
    next_node = None # Para apuntar al siguiente nodo

    def __init__(self, data):
        self.data = data

    def __repr__(self): # Sirve para proveer una representación de cadena al objeto cuando se inspecciona en la consola
        return '<Node data: %s>' % self.data
        

class LinkedList: # Va a definir un head,
    """
    Singly linked list
    """

    def __init__(self):
        # Este atributo modela al único nodo del cuál la lista va a tener referencia,
        # dado que cada nodo apunta al siguiente, podemos ir de nodo en nodo hasta 
        # alcanzar el nodo requerido, este proceso es llamado list traversal
        self.head = None

    
    # Método para verificar si la lista está vacía
    def is_empty(self):
        return self.head == None

    # El método para calcular el tamaño de la lista es mediante un recorrido de los nodos hasta llegar a un tail node
    def size(self):
        """
        Regresa el número de nodos en la lista
        Takes O(n) time
        """
        current = self.head
        count = 0

        while current: # Esta expresión es igual a while current != None
            count += 1
            current = current.next_node
        
        return count

    def add(self, data):
        """
        Como está operación es una simple reasignacion de las propiedades head y next node, entonces toma tiempo constante
        Adds new Node containing data at head of the list
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head # Se guarda la referencia al nodo que era la cabeza, al atributo new_node del nodo recien creado, si no hay nodo en la cabeza new_node = None
        self.head = new_node # La nueva cabeza de la lista es el nodo recien añadido

    
    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Returns the node or 'None' if not found
        Takes O(n) time
        """

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node

        return None


    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion takes O(1) time but finding the node at the 
        insertion point takes O(n) time

        Takes overall O(n) time
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)
            position = index # Cada que se llama a current = current.next_node, se decrementa el valor de position en 1, cuando el valor sea cero, se ha llegado al nodo que está actualmente en la posición que queremos insertar el nuevo valor
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1
            
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    
    def remove(self, key):
        """
        Remove Node containing data that matches the key
        Returns the node or None if key doesn't exist
        Takes O(n) time
        """
        current = self.head
        previous =  None # Para guardar la referencia al nodo previo conforme se atraviesa la lista
        found = False # Servirá como una stopping condition
        # El ciclo atravesará la lista mientras found sea False, cuando se encuentre el valor, found tomará el valor True y el ciclo terminará
        while current and not found:
            if current.data == key and current is self.head: # Se ejecuta si el valor a remover está en la head
                found = True
                self.head = current.next_node

            elif current.data == key: # Cuando el valor de key es igual al valor de otro nodo que no está en head
                found = True
                previous.next_node = current.next_node # La referencia al siguiente nodo después de previous es la del nodo después del nodo que se va a remover
            else:
                previous = current # Para hacer un seguimiento del nodo previo
                current = current.next_node # El nodo actual es el siguiente del nodo analizado, para seguir atravesando la lista
            
        return current

    
    def remove_index(self, index):
        """
        Remove Node at specified index
        Returns the node or None if the index is greater than the last index in the list
        Takes O(n) time
        """
        current = self.head
        position = index
        if index > (self.size() - 1):
            return None
        elif index == 0:
            self.head = current.next_node
        else:    
            while position >= 1:
                previous = current
                current = current.next_node
                position -= 1   
            previous.next_node = current.next_node

        return current

    
    def read_index(self, index):
        """
        Return the data stored at the specified index of the list
        Takes O(n) time, porque en el peor de los casos recorre toda la lista elemento por elemento
        """
        current = self.head
        if index == 0:
            return current.data
        elif index >= self.size() :
            return None
        else:
            position = 0
            while position < index:
                current = current.next_node
                position += 1
            return current.data



    def __repr__(self):
        """
        Return a string representation of the list
        Takes O(n) time, porque recorre toda la lista
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append('[Head: %s]' % current.data)
            elif current.next_node is None:
                nodes.append('[Tail: %s]' % current.data)
            else:
                nodes.append('[%s]' % current.data)
            current = current.next_node

        return '-> '.join(nodes)

