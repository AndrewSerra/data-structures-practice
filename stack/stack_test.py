#!/usr/bin/env python3
import unittest
from .stack import Stack
from utils.CustomizedTestCase import CustomizedTestCase
from random import random

class StackTest(CustomizedTestCase):
    def test_stack_creation(self):
        stack = Stack()

        # Test initialization is empty
        self.assertEqual(stack.size(), 0)
        # Test string to print is empty array
        self.assertEqual(str(stack), "[]")

    def test_stack_append(self):
        stack = Stack()
        insert_val = 8

        # Test initialization is empty
        self.assertEqual(stack.size(), 0)

        stack.append(insert_val)

        # Test append changed stack size
        self.assertEqual(stack.size(), 1)
        # Test appended element is final one 
        self.assertEqual(stack.peek(), insert_val)
        # Test stack empty is false
        self.assertFalse(stack.is_empty())

        return

    def test_stack_pop(self):
        stack = Stack()
        insert_values = self.generate_test_values(10)

        for value in insert_values:
            stack.append(value)

        # Test the size of the stack to equal the size of test array
        self.assertEqual(stack.size(), len(insert_values))
        # Test the stack being false when called is_empty
        self.assertFalse(stack.is_empty())
        # Test the last element match the test vector last element
        self.assertEqual(stack.peek(), insert_values[-1])

        # Remove last element
        pop_value = stack.pop()

        # Test the size has decreased by one
        self.assertEqual(stack.size(), len(insert_values)-1)
        # Test the stack being false when called is_empty
        self.assertFalse(stack.is_empty())
        # Test the last element match the test vector last element
        self.assertEqual(stack.peek(), insert_values[-2])
        # Test the pop value to match test vector last element
        self.assertEqual(pop_value, insert_values[-1])

        return

    def test_stack_peek(self):
        stack = Stack()
        insert_values = self.generate_test_values(10)
        
        for (idx, value) in list(enumerate(insert_values)):
            stack.append(value)
            # Test the last element being updated, correctly displayed in peek
            self.assertEqual(stack.peek(), value)
            # Test length of updated stack
            self.assertEqual(stack.size(), idx+1)
            # Test stack not returning empty
            self.assertFalse(stack.is_empty())
        
        return

    def test_stack_empty(self):
        stack = Stack()

        # Test stack being empty
        self.assertTrue(stack.is_empty())
        # Test stack length is zero
        self.assertEqual(stack.size(), 0)
        
        return

    def test_stack_length(self):
        stack_1 = Stack()
        generated_num = int(random() * 10)
        length_1 = 1 if int(random() * 10) == 0 else generated_num
        test_vals_1 = self.generate_test_values(length_1)

        for value in test_vals_1:
            stack_1.append(value)

        # Test size of first stack to be equal to random length
        self.assertEqual(stack_1.size(), length_1)

        stack_2 = Stack()
        generated_num = int(random() * 10)
        length_2 = 1 if int(random() * 10) == 0 else generated_num
        test_vals_2 = self.generate_test_values(length_2)

        for value in test_vals_2:
            stack_2.append(value)

        # Test size of second stack to be equal to random length
        self.assertEqual(stack_2.size(), length_2)

        return

    def test_stack_reset(self):
        stack = Stack()
        test_size = 10
        insert_values = self.generate_test_values(test_size)

        for value in insert_values:
            stack.append(value)

        # Test the size of the appended stack
        self.assertEqual(stack.size(), test_size)

        stack.reset()

        # Test the stack has resetted to be empty
        self.assertTrue(stack.is_empty())
        # Test the stack size is zero
        self.assertEqual(stack.size(), 0)

        return

if __name__ == "__main__":
    unittest.main()
