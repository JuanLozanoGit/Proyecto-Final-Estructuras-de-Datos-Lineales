import unittest
from src.listas.singly_linked_list import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = SinglyLinkedList()

    def test_append_and_traverse(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.assertEqual(self.list.traverse(), [1, 2, 3])

    def test_prepend(self):
        self.list.prepend(0)
        self.list.prepend(-1)
        self.assertEqual(self.list.traverse(), [-1, 0])

    def test_delete_success(self):
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        result = self.list.delete(2)
        self.assertTrue(result)
        self.assertEqual(self.list.traverse(), [1, 3])

    def test_delete_failure(self):
        self.list.append(1)
        result = self.list.delete(99)
        self.assertFalse(result)

    def test_search_success(self):
        self.list.append(5)
        self.assertTrue(self.list.search(5))

    def test_search_failure(self):
        self.list.append(5)
        self.assertFalse(self.list.search(10))

    def test_get_size(self):
        self.assertEqual(self.list.get_size(), 0)
        self.list.append(1)
        self.assertEqual(self.list.get_size(), 1)

if __name__ == '__main__':
    unittest.main()

