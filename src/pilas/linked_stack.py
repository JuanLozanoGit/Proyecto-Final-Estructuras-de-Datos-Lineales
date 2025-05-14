class Node:
    """
    Nodo para pila enlazada.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    """
    Implementación de pila usando lista enlazada.
    """

    def __init__(self):
        """Inicializa la pila vacía."""
        self.top = None
        self.size = 0
    
    def is_empty(self):
        """Devuelve True si la pila está vacía."""
        return self.top is None
    
    def push(self, data):
        """
        Inserta un elemento en la cima de la pila.

        Args:
            data: Valor a insertar.
        """
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        """
        Elimina y devuelve el elemento en la cima de la pila.

        Returns:
            Valor del elemento o None si la pila está vacía.
        """
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data
    
    def peek(self):
        """
        Devuelve el elemento en la cima sin eliminarlo.

        Returns:
            Valor del elemento o None si la pila está vacía.
        """
        if self.is_empty():
            return None
        return self.top.data
    
    def get_size(self):
        """
        Devuelve el tamaño de la pila.

        Returns:
            int: Número de elementos.
        """
        return self.size
    
    def traverse(self):
        """
        Devuelve una lista con los elementos de la pila (de cima a base).

        Returns:
            list: Elementos de la pila.
        """
        elements = []
        current = self.top
        while current:
            elements.append(current.data)
            current = current.next
        return elements

