# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:59:38 2019

@author: Juan Carlos
"""

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

exampleObject = ExampleClass(1)

print(exampleObject.a)
print(exampleObject.b)