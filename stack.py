#!/usr/bin/env python
# -*- coding: utf-8 -*-


class StackOverflowError(RuntimeError):
    pass


class StackIsEmptyError(RuntimeError):
    pass


class Stack:
    def __init__(self, size):
        self.storage = [0] * size
        self.head = -1

    def push(self, v):
        if (self.head + 1) < len(self.storage):
            self.storage[self.head + 1] = v
            self.head += 1
        else:
            raise StackOverflowError()

    def pop(self):
        if (self.head >= 0):
            e = self.storage[self.head]
            self.head -= 1
            return e
        else:
            raise StackIsEmptyError()
            
    def peek(self):
        return self.storage[self.head]      

    def __len__(self):
        return self.head + 1