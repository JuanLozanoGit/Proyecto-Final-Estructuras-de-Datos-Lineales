class ArrayStack:
    """
    Implementación de pila usando arreglo dinámico.
    """

    def __init__(self, capacity=10):
        """
        Inicializa la pila.

        Args:
            capacity (int): Capacidad inicial del arreglo.
        """
        self.items = [None] * capacity
        self.capacity = capacity
        self.size = 0
    
    def is_empty(self):
        """Devuelve True si la pila está vacía."""
        return self.size == 0
    
    def is_full(self):
        """Devuelve True si la pila está llena."""
        return self.size == self.capacity
    
    def push(self, data):
        """
        Inserta un elemento en la cima de la pila.

        Args:
            data: Valor a insertar.
        """
        if self.is_full():
            self._resize(2 * self.capacity)
        self.items[self.size] = data
        self.size += 1
    
    def pop(self):
        """
        Elimina y devuelve el elemento en la cima de la pila.

        Returns:
            Valor del elemento o None si la pila está vacía.
        """
        if self.is_empty():
            return None
        self.size -= 1
        data = self.items[self.size]
        self.items[self.size] = None
        
        if 0 < self.size < self.capacity // 4:
            self._resize(self.capacity // 2)
            
        return data
    
    def peek(self):
        """
        Devuelve el elemento en la cima sin eliminarlo.

        Returns:
            Valor del elemento o None si la pila está vacía.
        """
        if self.is_empty():
            return None
        return self.items[self.size - 1]
    
    def get_size(self):
        """
        Devuelve el tamaño de la pila.

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
            new_items[i] = self.items[i]
        self.items = new_items
        self.capacity = new_capacity
    
    def traverse(self):
        """
        Devuelve una lista con los elementos de la pila (de base a cima).

        Returns:
            list: Elementos de la pila.
        """
        return [self.items[i] for i in range(self.size)]

