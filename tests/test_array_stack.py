import unittest
from src.pilas.array_stack import ArrayStack

class TestArrayStack(unittest.TestCase):

    def setUp(self):
        self.stack = ArrayStack(capacity=2)

    def test_push_and_traverse(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)  # Esto debe hacer resize
        self.assertEqual(self.stack.traverse(), [1, 2, 3])

    def test_pop_success(self):
        self.stack.push(1)
        self.stack.push(2)
        popped = self.stack.pop()
        self.assertEqual(popped, 2)
        self.assertEqual(self.stack.traverse(), [1])

    def test_pop_empty(self):
        popped = self.stack.pop()
        self.assertIsNone(popped)

    def test_peek(self):
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)
        self.stack.pop()
        self.assertIsNone(self.stack.peek())

    def test_get_size(self):
        self.assertEqual(self.stack.get_size(), 0)
        self.stack.push(1)
        self.assertEqual(self.stack.get_size(), 1)

if __name__ == '__main__':
    unittest.main()

