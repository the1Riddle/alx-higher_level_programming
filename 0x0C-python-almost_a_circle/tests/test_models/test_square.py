#!/usr/bin/python3
"""unit test for square"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """the body of the class"""

    def test_init_success(self):
        s1 = Square(5)
        s2 = Square(10)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s2.id, 6)

    def test_init_without_args(self):

        self.assertRaises(TypeError, Square)

if __name__ == '__main__':
    unittest.main()
