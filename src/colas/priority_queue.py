class PriorityNode:
    """
    Nodo para cola de prioridad.
    """
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None

class PriorityQueue:
    """
    Implementación de cola de prioridad usando lista enlazada ordenada.
    """

    def __init__(self):
        """Inicializa la cola vacía."""
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """Devuelve True si la cola está vacía."""
        return self.head is None
    
    def enqueue(self, value, priority):
        """
        Inserta un elemento con prioridad.

        Args:
            value: Valor a insertar.
            priority (int): Prioridad (mayor valor = mayor prioridad).
        """
        new_node = PriorityNode(value, priority)
        
        if self.is_empty() or priority > self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.priority >= priority:
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
        
        self.size += 1
    
    def dequeue(self):
        """
        Elimina y devuelve el elemento con mayor prioridad.

        Returns:
            Valor del elemento o None si la cola está vacía.
        """
        if self.is_empty():
            return None
        
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value
    
    def peek(self):
        """
        Devuelve el elemento con mayor prioridad sin eliminarlo.

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
        Devuelve una lista de tuplas (valor, prioridad) en orden de prioridad.

        Returns:
            list: Elementos con sus prioridades.
        """
        elements = []
        current = self.head
        while current:
            elements.append((current.value, current.priority))
            current = current.next
        return elements

