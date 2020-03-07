# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:01:43 2019

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

if hasattr(exampleObject, 'b'):
    print(exampleObject.b)