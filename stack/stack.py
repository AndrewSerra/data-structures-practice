#!/usr/bin/env python3

# Data Structure: Stack
# Description:
#   This is a LIFO (Last-in-first-out) data structure

class Stack:
    def __init__(self) -> None:
        self.items = []

    def __str__(self) -> str:
        return str(self.items)

    def append(self, item) -> None:
        self.items.append(item)
        return

    def pop(self):
        return self.items.pop()

    def peek(self):
        item_list_len = len(self.items)
        if item_list_len == 0:
            return None
        else:
            return self.items[len(self.items)-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def reset(self) -> None:
        self.items = []
        return

    
