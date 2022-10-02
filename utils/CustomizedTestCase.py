from unittest import TestCase
from random import random

class CustomizedTestCase(TestCase):
    @staticmethod
    def generate_test_values(num_vals: int):
        if num_vals == 0: 
            raise Exception("Number of test values has to be greater than zero.")
        elif num_vals == 1:
            return [random()]
        else:
            values = [random() for _ in range(0, num_vals)]
            return values
            
