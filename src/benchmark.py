import time
import tracemalloc

class Benchmark:
    """
    Clase para medir tiempo y memoria de operaciones en estructuras de datos.
    """

    @staticmethod
    def benchmark_operation(data_structure, operation, iterations=1000, *args):
        """
        Ejecuta una operación repetidamente y mide tiempo y memoria.

        Args:
            data_structure: Instancia de estructura de datos.
            operation (str): Operación a medir ('insert', 'delete', 'search').
            iterations (int): Número de repeticiones.
            *args: Argumentos para la operación.

        Returns:
            dict: Resultados con tiempo total, promedio y memoria.
        """
        tracemalloc.start()
        start_time = time.perf_counter()
        
        for _ in range(iterations):
            if operation == "insert":
                if hasattr(data_structure, "append"):
                    data_structure.append(*args)
                elif hasattr(data_structure, "push"):
                    data_structure.push(*args)
                elif hasattr(data_structure, "enqueue"):
                    data_structure.enqueue(*args)
            elif operation == "delete":
                if hasattr(data_structure, "delete"):
                    data_structure.delete(*args)
                elif hasattr(data_structure, "pop"):
                    data_structure.pop()
                elif hasattr(data_structure, "dequeue"):
                    data_structure.dequeue()
            elif operation == "search":
                if hasattr(data_structure, "search"):
                    data_structure.search(*args)
                elif hasattr(data_structure, "peek"):
                    data_structure.peek()
        
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        total_time_ms = (end_time - start_time) * 1000
        avg_time_ms = total_time_ms / iterations if iterations else 0
        
        return {
            "operation": operation,
            "iterations": iterations,
            "total_time_ms": total_time_ms,
            "avg_time_ms": avg_time_ms,
            "memory_mb": current / 1e6,
            "peak_memory_mb": peak / 1e6
        }

