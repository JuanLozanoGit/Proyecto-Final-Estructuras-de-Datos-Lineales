import unittest
from src.colas.queue import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_enqueue_and_traverse(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.traverse(), [1, 2, 3])

    def test_dequeue_success(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        dequeued = self.queue.dequeue()
        self.assertEqual(dequeued, 1)
        self.assertEqual(self.queue.traverse(), [2])

    def test_dequeue_empty(self):
        dequeued = self.queue.dequeue()
        self.assertIsNone(dequeued)

    def test_peek(self):
        self.queue.enqueue(10)
        self.assertEqual(self.queue.peek(), 10)
        self.queue.dequeue()
        self.assertIsNone(self.queue.peek())

    def test_get_size(self):
        self.assertEqual(self.queue.get_size(), 0)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.get_size(), 1)

if __name__ == '__main__':
    unittest.main()

