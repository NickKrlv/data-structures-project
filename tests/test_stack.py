"""Здесь надо написать тесты с использованием unittest для модуля stack."""

import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push('data1')
        data = stack.pop()

        # стэк стал пустой
        self.assertIsNone(stack.top)

        # pop() удаляет элемент и возвращает данные удаленного элемента
        self.assertEqual(data, 'data1')

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        data = stack.pop()

        # теперь последний элемента содержит данные data1
        self.assertEqual(stack.top.data, 'data1')

        # данные удаленного элемента
        self.assertEqual(data, 'data2')


if __name__ == '__main__':
    unittest.main()
