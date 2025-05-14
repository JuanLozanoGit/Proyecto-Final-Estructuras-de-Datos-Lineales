import unittest
from src.colas.priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.queue = PriorityQueue()

    def test_enqueue_and_traverse(self):
        self.queue.enqueue("job1", 1)
        self.queue.enqueue("job2", 3)
        self.queue.enqueue("job3", 2)
        expected = [("job2", 3), ("job3", 2), ("job1", 1)]
        self.assertEqual(self.queue.traverse(), expected)

    def test_dequeue_success(self):
        self.queue.enqueue("job1", 1)
        self.queue.enqueue("job2", 3)
        dequeued = self.queue.dequeue()
        self.assertEqual(dequeued, "job2")
        expected = [("job1", 1)]
        self.assertEqual(self.queue.traverse(), expected)

    def test_dequeue_empty(self):
        dequeued = self.queue.dequeue()
        self.assertIsNone(dequeued)

    def test_peek(self):
        self.queue.enqueue("job1", 1)
        self.assertEqual(self.queue.peek(), "job1")
        self.queue.dequeue()
        self.assertIsNone(self.queue.peek())

    def test_get_size(self):
        self.assertEqual(self.queue.get_size(), 0)
        self.queue.enqueue("job1", 1)
        self.assertEqual(self.queue.get_size(), 1)

if __name__ == '__main__':
    unittest.main()

