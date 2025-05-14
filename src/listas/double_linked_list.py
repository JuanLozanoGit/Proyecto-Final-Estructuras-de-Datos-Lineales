class Node:
    """
    Nodo para lista enlazada doble.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """
    Implementación de lista enlazada doble.
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
            new_node.prev = current
        self.size += 1
    
    def prepend(self, data):
        """
        Agrega un nodo al inicio de la lista.

        Args:
            data: Valor a insertar.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
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
            if self.head:
                self.head.prev = None
            self.size -= 1
            return True
        
        current = self.head
        while current and current.data != data:
            current = current.next
        
        if current:
            if current.next:
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next
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
        Recorre la lista de inicio a fin.

        Returns:
            list: Elementos de la lista.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    def traverse_reverse(self):
        """
        Recorre la lista de fin a inicio.

        Returns:
            list: Elementos de la lista en orden inverso.
        """
        elements = []
        if self.is_empty():
            return elements
        
        current = self.head
        while current.next:
            current = current.next
        
        while current:
            elements.append(current.data)
            current = current.prev
        return elements
    
    def get_size(self):
        """
        Devuelve el tamaño de la lista.

        Returns:
            int: Número de elementos.
        """
        return self.size

