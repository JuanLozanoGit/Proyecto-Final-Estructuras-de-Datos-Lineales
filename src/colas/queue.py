class Node:
    """
    Nodo para cola simple.
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Queue:
    """
    Implementación de cola simple (FIFO).
    """

    def __init__(self):
        """Inicializa la cola vacía."""
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        """Devuelve True si la cola está vacía."""
        return self.head is None
    
    def enqueue(self, value):
        """
        Inserta un elemento al final de la cola.

        Args:
            value: Valor a insertar.
        """
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def dequeue(self):
        """
        Elimina y devuelve el elemento al frente de la cola.

        Returns:
            Valor del elemento o None si la cola está vacía.
        """
        if self.is_empty():
            return None
        dequeued_value = self.head.value
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return dequeued_value
    
    def peek(self):
        """
        Devuelve el elemento al frente sin eliminarlo.

        Returns:
            Valor del elemento o None si la cola está vacía.
        """
        if self.is_empty():
            return None
        return self.head.value
    
    def get_size(self):
        """
        Devuelve el tamaño de la cola.

        Returns:
            int: Número de elementos.
        """
        return self.size
    
    def traverse(self):
        """
        Devuelve una lista con los elementos de la cola.

        Returns:
            list: Elementos de la cola.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

