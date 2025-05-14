class Node:
    """
    Nodo para lista enlazada simple.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """
    Implementación de lista enlazada simple.
    """

    def __init__(self):
        """Inicializa la lista vacía."""
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """Devuelve True si la lista está vacía."""
        return self.head is None
    
    def append(self, data):
        """
        Agrega un nodo al final de la lista.

        Args:
            data: Valor a insertar.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def prepend(self, data):
        """
        Agrega un nodo al inicio de la lista.

        Args:
            data: Valor a insertar.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def delete(self, data):
        """
        Elimina el primer nodo que contiene el valor dado.

        Args:
            data: Valor a eliminar.

        Returns:
            bool: True si se eliminó, False si no se encontró.
        """
        if self.is_empty():
            return False
        
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        if current.next:
            current.next = current.next.next
            self.size -= 1
            return True
        return False
    
    def search(self, data):
        """
        Busca un valor en la lista.

        Args:
            data: Valor a buscar.

        Returns:
            bool: True si se encuentra, False si no.
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def traverse(self):
        """
        Recorre la lista y devuelve una lista con sus elementos.

        Returns:
            list: Elementos de la lista.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    def get_size(self):
        """
        Devuelve el tamaño de la lista.

        Returns:
            int: Número de elementos.
        """
        return self.size

