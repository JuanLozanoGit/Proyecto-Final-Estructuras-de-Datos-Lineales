class CircularQueue:
    """
    Implementación de cola circular basada en arreglo.
    """

    def __init__(self, capacity=10):
        """
        Inicializa la cola circular.

        Args:
            capacity (int): Capacidad inicial.
        """
        self.items = [None] * capacity
        self.capacity = capacity
        self.size = 0
        self.front = 0
        self.rear = -1
    
    def is_empty(self):
        """Devuelve True si la cola está vacía."""
        return self.size == 0
    
    def is_full(self):
        """Devuelve True si la cola está llena."""
        return self.size == self.capacity
    
    def enqueue(self, value):
        """
        Inserta un elemento al final de la cola.

        Args:
            value: Valor a insertar.
        """
        if self.is_full():
            self._resize(2 * self.capacity)
        
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = value
        self.size += 1
    
    def dequeue(self):
        """
        Elimina y devuelve el elemento al frente de la cola.

        Returns:
            Valor del elemento o None si la cola está vacía.
        """
        if self.is_empty():
            return None
        
        value = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        
        if 0 < self.size < self.capacity // 4:
            self._resize(self.capacity // 2)
            
        return value
    
    def peek(self):
        """
        Devuelve el elemento al frente sin eliminarlo.

        Returns:
            Valor del elemento o None si la cola está vacía.
        """
        if self.is_empty():
            return None
        return self.items[self.front]
    
    def get_size(self):
        """
        Devuelve el tamaño de la cola.

        Returns:
            int: Número de elementos.
        """
        return self.size
    
    def _resize(self, new_capacity):
        """
        Cambia el tamaño del arreglo interno.

        Args:
            new_capacity (int): Nueva capacidad.
        """
        new_items = [None] * new_capacity
        for i in range(self.size):
            new_items[i] = self.items[(self.front + i) % self.capacity]
        
        self.items = new_items
        self.capacity = new_capacity
        self.front = 0
        self.rear = self.size - 1 if self.size > 0 else -1
    
    def traverse(self):
        """
        Devuelve una lista con los elementos de la cola.

        Returns:
            list: Elementos de la cola.
        """
        elements = []
        for i in range(self.size):
            elements.append(self.items[(self.front + i) % self.capacity])
        return elements

