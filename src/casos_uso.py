from pilas.linked_stack import LinkedStack
from colas.priority_queue import PriorityQueue
from colas.circular_queue import CircularQueue

class BrowserHistory:
    """
    Sistema de historial de navegación web usando pilas.
    """

    def __init__(self):
        self.back_stack = LinkedStack()
        self.forward_stack = LinkedStack()
        self.current_page = None
    
    def navigate(self, url):
        """
        Navega a una nueva URL.

        Args:
            url (str): URL a navegar.
        """
        if self.current_page:
            self.back_stack.push(self.current_page)
        self.current_page = url
        self.forward_stack = LinkedStack()
        print(f"Navegando a: {url}")
    
    def go_back(self):
        """
        Va a la página anterior.

        Returns:
            bool: True si pudo ir atrás, False si no.
        """
        if self.back_stack.is_empty():
            print("No hay páginas anteriores")
            return False
        
        self.forward_stack.push(self.current_page)
        self.current_page = self.back_stack.pop()
        print(f"Volviendo a: {self.current_page}")
        return True
    
    def go_forward(self):
        """
        Va a la página siguiente.

        Returns:
            bool: True si pudo ir adelante, False si no.
        """
        if self.forward_stack.is_empty():
            print("No hay páginas para avanzar")
            return False
        
        self.back_stack.push(self.current_page)
        self.current_page = self.forward_stack.pop()
        print(f"Avanzando a: {self.current_page}")
        return True
    
    def get_current_page(self):
        """Devuelve la página actual."""
        return self.current_page


class PrinterManager:
    """
    Sistema de gestión de impresión con cola de prioridad.
    """

    def __init__(self):
        self.print_queue = PriorityQueue()
    
    def add_job(self, document, priority):
        """
        Añade un trabajo de impresión.

        Args:
            document (str): Nombre del documento.
            priority (int): Prioridad del trabajo.
        """
        self.print_queue.enqueue(document, priority)
        print(f"Trabajo de impresión '{document}' añadido con prioridad {priority}")
    
    def process_next_job(self):
        """
        Procesa el siguiente trabajo de impresión.

        Returns:
            str o None: Documento impreso o None si no hay trabajos.
        """
        if self.print_queue.is_empty():
            print("No hay trabajos en la cola de impresión")
            return None
        
        document = self.print_queue.dequeue()
        print(f"Imprimiendo: {document}")
        return document
    
    def get_queue_status(self):
        """Muestra el estado actual de la cola de impresión."""
        jobs = self.print_queue.traverse()
        print(f"Estado de la cola: {len(jobs)} trabajos pendientes")
        for i, (doc, priority) in enumerate(jobs, 1):
            print(f"{i}. '{doc}' (prioridad: {priority})")
        return jobs


class CircularBuffer:
    """
    Buffer circular para procesamiento de datos en tiempo real.
    """

    def __init__(self, capacity=10):
        self.buffer = CircularQueue(capacity)
        self.capacity = capacity
    
    def write(self, data):
        """
        Escribe un dato en el buffer, sobrescribiendo si está lleno.

        Args:
            data: Dato a escribir.
        """
        if self.buffer.is_full():
            old_data = self.buffer.dequeue()
            print(f"Buffer lleno, sobrescribiendo dato: {old_data}")
        self.buffer.enqueue(data)
        print(f"Dato escrito en el buffer: {data}")
    
    def read(self):
        """
        Lee el dato más antiguo del buffer.

        Returns:
            Dato leído o None si el buffer está vacío.
        """
        if self.buffer.is_empty():
            print("Buffer vacío, no hay datos para leer")
            return None
        data = self.buffer.dequeue()
        print(f"Leyendo dato del buffer: {data}")
        return data
    
    def peek(self):
        """Observa el próximo dato sin eliminarlo."""
        return self.buffer.peek()
    
    def get_status(self):
        """Muestra el estado actual del buffer."""
        data = self.buffer.traverse()
        print(f"Buffer: {len(data)}/{self.capacity} ocupado")
        print(f"Contenido: {data}")
        return data

