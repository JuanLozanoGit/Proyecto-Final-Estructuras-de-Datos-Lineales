class Node:
    """
    Nodo para lista circular simple.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    """
    Implementación de lista circular simple.
    """

    def __init__(self):
        """Inicializa la lista vacía."""
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """Devuelve True si la lista está vacía."""
        return self.head is None
    
    def append(self, value):
        """
        Agrega un nodo al final de la lista circular.

        Args:
            value: Valor a insertar.
        """
        new_node = Node(value)
        if self.is_empty():
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        self.size += 1
    
    def prepend(self, value):
        """
        Agrega un nodo al inicio de la lista circular.

        Args:
            value: Valor a insertar.
        """
        new_node = Node(value)
        if self.is_empty():
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            current.next = new_node
            self.head = new_node
        self.size += 1
    
    def delete(self, value):
        """
        Elimina el primer nodo que contiene el valor dado.

        Args:
            value: Valor a eliminar.

        Returns:
            bool: True si se eliminó, False si no se encontró.
        """
        if self.is_empty():
            return False
        
        if self.head.value == value:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next != self.head and current.next.value != value:
            current = current.next
        
        if current.next != self.head:
            current.next = current.next.next
            self.size -= 1
            return True
        return False
    
    def search(self, value):
        """
        Busca un valor en la lista circular.

        Args:
            value: Valor a buscar.

        Returns:
            bool: True si se encuentra, False si no.
        """
        if self.is_empty():
            return False
        
        current = self.head
        while True:
            if current.value == value:
                return True
            current = current.next
            if current == self.head:
                break
        return False
    
    def traverse(self):
        """
        Recorre la lista circular y devuelve sus elementos.

        Returns:
            list: Elementos de la lista circular.
        """
        elements = []
        if self.is_empty():
            return elements
        
        current = self.head
        while True:
            elements.append(current.value)
            current = current.next
            if current == self.head:
                break
        return elements
    
    def get_size(self):
        """
        Devuelve el tamaño de la lista circular.

        Returns:
            int: Número de elementos.
        """
        return self.size

